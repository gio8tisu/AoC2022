import argparse
import sys
from typing import TextIO, TypeAlias


Coordinate: TypeAlias = tuple[int, int]


def main(cave_rocks_file: TextIO, part: int):
    if part == 1:
        cave = create_cave(cave_rocks_file)
        sand_grains = start_sand_pouring(cave)
        print(sand_grains)
    elif part == 2:
        raise NotImplementedError("Part 2 not implemented yet")
    else:
        raise ValueError(f"Invalid part: {part}")


class FlowIntoAbyss(Exception):
    pass


class Cave:
    rocks: set[Coordinate]
    sand: set[Coordinate]

    def __init__(self):
        self.rocks = set()
        self.sand = set()

    def add_rock_structure(self, path: list[Coordinate]):
        start = None
        for coordinate in path:
            if start is None:
                start = coordinate
            else:
                self._add_rock_line(start, coordinate)
                start = coordinate

    def _add_rock_line(self, start: Coordinate, end: Coordinate):
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.rocks.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.rocks.add((x, y1))
        else:
            raise ValueError("Not a line")

    def pour_sand(self):
        sand_grain = (500, 0)
        while True:
            x, y = sand_grain
            if not any(y < y2 for _, y2 in self.rocks):
                raise FlowIntoAbyss()
            if not (x, y + 1) in self.rocks | self.sand:
                sand_grain = (x, y + 1)
            elif not (x - 1, y + 1) in self.rocks | self.sand:
                sand_grain = (x - 1, y + 1)
            elif not (x + 1, y + 1) in self.rocks | self.sand:
                sand_grain = (x + 1, y + 1)
            else:
                break
        self.sand.add(sand_grain)


def create_cave(cave_rocks_file: TextIO) -> Cave:
    # Example line: 498,4 -> 498,6 -> 496,6
    cave = Cave()
    for line in cave_rocks_file:
        path = []
        for coordinate in line.strip().split(" -> "):
            x, y = coordinate.split(",")
            path.append((int(x), int(y)))
        cave.add_rock_structure(path)
    return cave


def start_sand_pouring(cave: Cave) -> int:
    while True:
        try:
            cave.pour_sand()
        except FlowIntoAbyss:
            break
    return len(cave.sand)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
