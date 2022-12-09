import argparse
import sys
from typing import TextIO, TypeAlias
from itertools import product


TreeGrid: TypeAlias = list[list[int]]


def main(map_file: TextIO, part: int):
    grid = read_map_file_as_grid(map_file)
    if part == 1:
        visible_trees = count_visible_trees(grid)
        print(visible_trees)
    else:
        raise ValueError(f"Invalid part: {part}")


def read_map_file_as_grid(map_file: TextIO) -> TreeGrid:
    grid: TreeGrid = []
    for line in map_file.readlines():
        row = [int(c) for c in line.strip()]
        grid.append(row)
        assert len(row) == len(grid[0]), "All rows must have the same length"
    return grid


def count_visible_trees(trees: TreeGrid) -> int:
    visible_trees = 0
    num_rows = len(trees)
    num_cols = len(trees[0])
    for i, j in product(range(num_rows), range(num_cols)):
        if is_visible(trees, i, j):
            visible_trees += 1

    return visible_trees


def is_visible(trees: TreeGrid, i: int, j: int) -> bool:
    current_tree = trees[i][j]
    num_rows = len(trees)
    num_cols = len(trees[0])
    if i == 0 or j == 0 or i == num_rows - 1 or j == num_cols - 1:
        return True
    if all(trees[k][j] < current_tree for k in range(0, i)):
        return True
    if all(trees[k][j] < current_tree for k in range(i + 1, num_rows)):
        return True
    if all(trees[i][l] < current_tree for l in range(0, j)):
        return True
    if all(trees[i][l] < current_tree for l in range(j + 1, num_cols)):
        return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
