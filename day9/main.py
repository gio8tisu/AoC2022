import argparse
import sys
from typing import TextIO, NamedTuple
from enum import Enum
from math import sqrt


class Direction(str, Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class Position(NamedTuple):
    x: int
    y: int


class Motion(NamedTuple):
    direction: Direction
    length: int


def main(motions_file: TextIO, part: int):
    if part == 1:
        motions = read_motions(motions_file)
        visited_positions = find_visited_positions(motions)
        print(len(visited_positions))
    else:
        raise ValueError(f"Invalid part: {part}")


def read_motions(motions_file: TextIO) -> list[Motion]:
    motions = []
    for line in motions_file.readlines():
        direction, length = line.strip().split(" ")
        motions.append(Motion(Direction(direction), int(length)))
    return motions


def find_visited_positions(motions: list[Motion]) -> set[Position]:
    visited_positions = set()
    head_position = Position(0, 0)
    tail_position = Position(0, 0)
    for motion in motions:
        head_position, tail_position = do_motion(
            head_position, tail_position, motion, visited_positions)
    return visited_positions


def do_motion(head_position: Position, tail_position: Position, motion: Motion, visited_positions: set[Position]) -> tuple[Position, Position]:
    for _ in range(motion.length):
        head_position = move_head(head_position, motion.direction)
        tail_position = move_tail(tail_position, head_position)
        visited_positions.add(tail_position)
    return head_position, tail_position


def move_head(head_position: Position, direction: Direction) -> Position:
    if direction == Direction.UP:
        return Position(head_position.x, head_position.y + 1)
    elif direction == Direction.DOWN:
        return Position(head_position.x, head_position.y - 1)
    elif direction == Direction.LEFT:
        return Position(head_position.x - 1, head_position.y)
    elif direction == Direction.RIGHT:
        return Position(head_position.x + 1, head_position.y)
    else:
        raise ValueError(f"Invalid direction: {direction}")


def move_tail(tail_position: Position, head_position: Position) -> Position:
    diff_x, diff_y = head_position.x - tail_position.x, head_position.y - tail_position.y
    if sqrt(diff_x ** 2 + diff_y ** 2) < 2:
        return tail_position
    if diff_x == 0:
        if diff_y > 0:
            return Position(tail_position.x, tail_position.y + 1)
        else:
            return Position(tail_position.x, tail_position.y - 1)
    if diff_y == 0:
        if diff_x > 0:
            return Position(tail_position.x + 1, tail_position.y)
        else:
            return Position(tail_position.x - 1, tail_position.y)
    if diff_x > 0 and diff_y > 0:
        return Position(tail_position.x + 1, tail_position.y + 1)
    if diff_x > 0 and diff_y < 0:
        return Position(tail_position.x + 1, tail_position.y - 1)
    if diff_x < 0 and diff_y > 0:
        return Position(tail_position.x - 1, tail_position.y + 1)
    return Position(tail_position.x - 1, tail_position.y - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
