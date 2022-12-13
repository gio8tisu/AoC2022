import argparse
import sys
from typing import TextIO
from queue import PriorityQueue
from dataclasses import dataclass


@dataclass
class Coordinate:
    row: int
    col: int

    def __add__(self, other):
        return Coordinate(self.row + other.row, self.col + other.col)

    def __hash__(self):
        return hash((self.row, self.col))


def main(height_map_file: TextIO, part: int):
    if part == 1:
        height_map, source_coordinates, target_coordinates = parse_height_map(height_map_file)
        shortest_path_distance = find_shortest_path(height_map, source_coordinates, target_coordinates)
        print(shortest_path_distance)
    else:
        raise ValueError(f"Invalid part: {part}")


def find_shortest_path(height_map: list[list[int]], source: Coordinate, target_coordinate: Coordinate) -> int:
    """Find the shortest path from source to target using Dijkstra's algorithm.

    Could be optimized by using A* algorithm.
    """
    visited = set()

    D = [[99999 for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    D[source.row][source.col] = 0

    queue: PriorityQueue[tuple[int, int, int]] = PriorityQueue()
    queue.put((0, source.row, source.col))

    while not queue.empty():
        _, row, col = queue.get()
        current_vertex = Coordinate(row, col)
        visited.add(current_vertex)

        for direction in (Coordinate(0, 1), Coordinate(0, -1), Coordinate(1, 0), Coordinate(-1, 0)):
            neighbor = current_vertex + direction
            if neighbor.row < 0 or neighbor.row >= len(height_map):
                continue
            if neighbor.col < 0 or neighbor.col >= len(height_map[0]):
                continue
            # Can only go one step up or many steps down.
            if height_map[neighbor.row][neighbor.col] <= height_map[current_vertex.row][current_vertex.col] + 1:
                if neighbor not in visited:
                    old_cost = D[neighbor.row][neighbor.col]
                    new_cost = D[current_vertex.row][current_vertex.col] + 1
                    if new_cost < old_cost:
                        queue.put((new_cost, neighbor.row, neighbor.col))
                        D[neighbor.row][neighbor.col] = new_cost

    return D[target_coordinate.row][target_coordinate.col]


def parse_height_map(height_map_file: TextIO) -> tuple[list[list[int]], Coordinate, Coordinate]:
    height_map = []
    source = None
    target = None
    for row, line in enumerate(height_map_file.readlines()):
        height_map.append([])
        for col, char in enumerate(line.strip("\n")):
            if char == "S":
                source = Coordinate(row, col)
            elif char == "E":
                target = Coordinate(row, col)
            height_map[-1].append(parse_height(char))
    if source is None or target is None:
        raise ValueError("Missing source or target")
    return height_map, source, target


def parse_height(char: str):
    if char == "S":
        return 0
    elif char == "E":
        return 25
    return ord(char) - ord("a")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
