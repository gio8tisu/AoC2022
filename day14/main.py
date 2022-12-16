import argparse
import sys
from typing import TextIO, TypeAlias


Coordinate: TypeAlias = tuple[int, int]


def main(cave_rocks_file: TextIO, part: int):
    if part == 1:
        cave = create_cave(cave_rocks_file, False)
    elif part == 2:
        cave = create_cave(cave_rocks_file, True)
    else:
        raise ValueError(f"Invalid part: {part}")
    start_sand_pouring(cave)
    print(cave.sand_grains)


class FlowIntoAbyss(Exception):
    pass


class Cave:
    obstacles: set[Coordinate]
    sand_grains: int
    has_floor: bool
    floor_level = float("inf")

    def __init__(self, has_floor: bool = False):
        self.obstacles = set()
        self.sand_grains = 0
        self.has_floor = has_floor

    def add_rock_structure(self, path: list[Coordinate]):
        start = None
        for coordinate in path:
            if start is None:
                start = coordinate
            else:
                self._add_rock_line(start, coordinate)
                start = coordinate
        if self.has_floor:
            self.floor_level = max(y for _, y in self.obstacles) + 2

    def _add_rock_line(self, start: Coordinate, end: Coordinate):
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.obstacles.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.obstacles.add((x, y1))
        else:
            raise ValueError("Not a line")

    def pour_sand(self):
        sand_grain = (500, 0)
        while True:
            x, y = sand_grain
            if not self.has_floor and not any(y < y2 for _, y2 in self.obstacles):
                raise FlowIntoAbyss()
            if not (x, y + 1) in self.obstacles and y + 1 < self.floor_level:
                sand_grain = (x, y + 1)
            elif not (x - 1, y + 1) in self.obstacles and y + 1 < self.floor_level:
                sand_grain = (x - 1, y + 1)
            elif not (x + 1, y + 1) in self.obstacles and y + 1 < self.floor_level:
                sand_grain = (x + 1, y + 1)
            else:
                break
        self.obstacles.add(sand_grain)
        self.sand_grains += 1


def create_cave(cave_rocks_file: TextIO, has_floor: bool) -> Cave:
    cave = Cave(has_floor)
    for line in cave_rocks_file:
        path = []
        for coordinate in line.strip().split(" -> "):
            x, y = coordinate.split(",")
            path.append((int(x), int(y)))
        cave.add_rock_structure(path)
    return cave


def start_sand_pouring(cave: Cave):
    while (500, 0) not in cave.obstacles:
        try:
            cave.pour_sand()
        except FlowIntoAbyss:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
