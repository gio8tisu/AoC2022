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
    motions = read_motions(motions_file)
    if part == 1:
        visited_positions = find_visited_positions(motions, 2)
        print(len(visited_positions))
    elif part == 2:
        visited_positions = find_visited_positions(motions, 10)
        print(len(visited_positions))
    else:
        raise ValueError(f"Invalid part: {part}")


def read_motions(motions_file: TextIO) -> list[Motion]:
    motions = []
    for line in motions_file.readlines():
        direction, length = line.strip().split(" ")
        motions.append(Motion(Direction(direction), int(length)))
    return motions


def find_visited_positions(motions: list[Motion], num_knots: int) -> set[Position]:
    visited_positions = set()
    knot_positions = [Position(0, 0) for _ in range(num_knots)]
    for motion in motions:
        do_motion(knot_positions, motion, visited_positions)
    return visited_positions


def do_motion(knot_positions: list[Position], motion: Motion, visited_positions: set[Position]):
    for _ in range(motion.length):
        for i in range(len(knot_positions)):
            if i == 0:
                knot_positions[i] = move_head(knot_positions[i], motion.direction)
            else:
                knot_positions[i] = move_knot(knot_positions[i], knot_positions[i - 1])
        visited_positions.add(knot_positions[-1])


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


def move_knot(knot_position: Position, head_position: Position) -> Position:
    diff_x, diff_y = head_position.x - knot_position.x, head_position.y - knot_position.y
    if sqrt(diff_x ** 2 + diff_y ** 2) < 2:
        return knot_position
    if diff_x == 0:
        if diff_y > 0:
            return Position(knot_position.x, knot_position.y + 1)
        else:
            return Position(knot_position.x, knot_position.y - 1)
    if diff_y == 0:
        if diff_x > 0:
            return Position(knot_position.x + 1, knot_position.y)
        else:
            return Position(knot_position.x - 1, knot_position.y)
    if diff_x > 0 and diff_y > 0:
        return Position(knot_position.x + 1, knot_position.y + 1)
    if diff_x > 0 and diff_y < 0:
        return Position(knot_position.x + 1, knot_position.y - 1)
    if diff_x < 0 and diff_y > 0:
        return Position(knot_position.x - 1, knot_position.y + 1)
    return Position(knot_position.x - 1, knot_position.y - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
