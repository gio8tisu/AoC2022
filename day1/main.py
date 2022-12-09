import sys
from typing import TextIO


def main(calories: TextIO, part: int):
    calories_list = read_calories_as_lists(calories)
    total_calories = get_top_n_calories(calories_list, 1 if part == 1 else 3)
    print(total_calories)


def read_calories_as_lists(calories: TextIO) -> list[list[int]]:
    calories_list = [[]]
    for l in calories.readlines():
        line = l.strip("\n")
        if line == "":
            calories_list.append([])
            continue
        try:
            calories_list[-1].append(int(line))
        except ValueError:
            print("Invalid input", line)
            raise
    return calories_list


def get_max_calories(calories_list: list[list[int]]) -> int:
    return max([sum(elf_calories) for elf_calories in calories_list])


def get_top_n_calories(calories_list: list[list[int]], top: int) -> int:
    return sum(sorted([sum(elf_calories) for elf_calories in calories_list])[-top:])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
