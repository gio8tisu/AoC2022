import argparse
import sys
from typing import TextIO
from dataclasses import dataclass


@dataclass
class AssignmentPair:
    first_elf: list[int]
    second_elf: list[int]


def main(assignment_pairs_file: TextIO, part: int):
    assignment_pairs = read_assignment_pairs(assignment_pairs_file)
    if part == 1:
        overlapping_pairs = find_fully_contained_pairs(assignment_pairs)
    elif part == 2:
        overlapping_pairs = find_overlapping_at_all_pairs(assignment_pairs)
    else:
        raise ValueError(f"Invalid part: {part}")
    print(len(overlapping_pairs))


def read_assignment_pairs(assignment_pairs_file: TextIO) -> list[AssignmentPair]:
    assignment_pairs = []
    for line in assignment_pairs_file.readlines():
        assignment_pairs.append(create_assignment_pair(line.strip()))
    return assignment_pairs


def create_assignment_pair(line: str) -> AssignmentPair:
    first_pair_range, second_pair_range = line.split(",")
    first_pair_start, first_pair_stop = first_pair_range.split("-")
    second_pair_start, second_pair_stop = second_pair_range.split("-")
    return AssignmentPair(
        first_elf=list(range(int(first_pair_start), int(first_pair_stop) + 1)),
        second_elf=list(range(int(second_pair_start), int(second_pair_stop) + 1)),
    )


def find_fully_contained_pairs(assignment_pairs: list[AssignmentPair]) -> list[AssignmentPair]:
    fully_contained_pairs = []
    for assignment_pair in assignment_pairs:
        if is_fully_contained(assignment_pair):
            fully_contained_pairs.append(assignment_pair)
    return fully_contained_pairs


def find_overlapping_at_all_pairs(assignment_pairs: list[AssignmentPair]) -> list[AssignmentPair]:
    overlapping_pairs = []
    for assignment_pair in assignment_pairs:
        if is_overlapped(assignment_pair):
            overlapping_pairs.append(assignment_pair)
    return overlapping_pairs


def is_fully_contained(assignment_pair: AssignmentPair) -> bool:
    return (assignment_pair.first_elf[0] <= assignment_pair.second_elf[0] and assignment_pair.first_elf[-1] >= assignment_pair.second_elf[-1]
            or assignment_pair.second_elf[0] <= assignment_pair.first_elf[0] and assignment_pair.second_elf[-1] >= assignment_pair.first_elf[-1])


def is_overlapped(assignment_pair: AssignmentPair) -> bool:
    return (assignment_pair.first_elf[0] <= assignment_pair.second_elf[0] and assignment_pair.first_elf[-1] >= assignment_pair.second_elf[0]
            or assignment_pair.second_elf[0] <= assignment_pair.first_elf[0] and assignment_pair.second_elf[-1] >= assignment_pair.first_elf[0])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
