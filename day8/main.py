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
    elif part == 2:
        scenic_scores = find_scenic_scores(grid)
        max_scenic_score = max(scenic_scores)
        print(max_scenic_score)
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


def find_scenic_scores(trees: TreeGrid) -> list[int]:
    num_rows = len(trees)
    num_cols = len(trees[0])
    scenic_scores = []
    for i, j in product(range(num_rows), range(num_cols)):
        scenic_score = tree_scenic_score(trees, i, j)
        scenic_scores.append(scenic_score)
    return scenic_scores


def tree_scenic_score(trees: TreeGrid, i: int, j: int) -> int:
    up = count_trees_in_up_direction(trees, i, j)
    down = count_trees_in_down_direction(trees, i, j)
    right = count_trees_in_right_direction(trees, i, j)
    left = count_trees_in_left_direction(trees, i, j)
    return up * down * right * left


def count_trees_in_up_direction(trees: TreeGrid, i: int, j: int) -> int:
    current_tree = trees[i][j]
    for k in range(i - 1, -1, -1):
        if trees[k][j] >= current_tree:
            return i - k
    return i


def count_trees_in_down_direction(trees: TreeGrid, i: int, j: int) -> int:
    current_tree = trees[i][j]
    for k in range(i + 1, len(trees)):
        if trees[k][j] >= current_tree:
            return k - i
    return len(trees) - i - 1


def count_trees_in_right_direction(trees: TreeGrid, i: int, j: int) -> int:
    current_tree = trees[i][j]
    for l in range(j + 1, len(trees[0])):
        if trees[i][l] >= current_tree:
            return l - j
    return len(trees[0]) - j - 1


def count_trees_in_left_direction(trees: TreeGrid, i: int, j: int) -> int:
    current_tree = trees[i][j]
    for l in range(j - 1, -1, -1):
        if trees[i][l] >= current_tree:
            return j - l
    return j


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
