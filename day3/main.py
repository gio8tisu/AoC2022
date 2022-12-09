import sys
from typing import TextIO
import argparse
from dataclasses import dataclass


@dataclass
class Rucksack:
    first_compartment: list[str]
    second_compartment: list[str]

    @property
    def contents(self) -> list[str]:
        return self.first_compartment + self.second_compartment


def main1(list_of_contents: TextIO):
    rucksacks = read_list_of_contents_in_rucksacks(list_of_contents)
    duplicates = find_duplicates(rucksacks)
    sum_ = sum_content_priorities(duplicates)
    print(sum_)


def main2(list_of_contents: TextIO):
    rucksacks = read_list_of_contents_in_rucksacks(list_of_contents)
    grouped_rucksacks = group_rucksacks(rucksacks)
    badges = find_badges(grouped_rucksacks)
    sum_ = sum_content_priorities(badges)
    print(sum_)


def read_list_of_contents_in_rucksacks(list_of_contents: TextIO) -> list[Rucksack]:
    rucksacks = []
    for line in list_of_contents:
        rucksack = create_rucksack(line)
        rucksacks.append(rucksack)
    return rucksacks


def create_rucksack(line: str) -> Rucksack:
    contents = [char for char in line]
    half_index  = len(contents) // 2
    return Rucksack(contents[:half_index], contents[half_index:])


def find_duplicates(rucksacks: list) -> list:
    duplicates = []
    for rucksack in rucksacks:
        duplicate = find_duplicate(rucksack)
        duplicates.append(duplicate)
    return duplicates


def find_duplicate(rucksack: Rucksack) -> str:
    for content in rucksack.first_compartment:
        if content in rucksack.second_compartment:
            return content
    return ""


def sum_content_priorities(duplicates: list) -> int:
    sum_ = 0
    for duplicate in duplicates:
        sum_ += content_to_int(duplicate)
    return sum_


def content_to_int(content: str) -> int:
    if str.islower(content):
        return ord(content) - 96
    return ord(content) - 65 + 27


def group_rucksacks(rucksacks: list) -> list[list]:
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])
    return groups


def find_badges(grouped_rucksacks: list[list[Rucksack]]) -> list[str]:
    return [find_badge(group) for group in grouped_rucksacks]


def find_badge(group: list[Rucksack]) -> str:
    for content in group[0].contents:
        if all(content in rucksack.contents for rucksack in group[1:]):
            return content
    return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    if args.part == 1:
        main1(args.file)
    elif args.part == 2:
        main2(args.file)
    else:
        print("Unknown part")
