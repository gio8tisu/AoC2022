import argparse
import sys
from typing import Generator, TextIO, Callable
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    throw: Callable[[bool], int]
    inspected_items: int = 0


NUM_ROUNDS_PART_1 = 20
NUM_ROUNDS_PART_2 = 10000
MODULO = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19


def main(notes_file: TextIO, part: int):
    monkeys = read_notes(notes_file)
    if part == 1:
        play_game(monkeys, NUM_ROUNDS_PART_1, lambda x: x // 3)
    elif part == 2:
        play_game(monkeys, NUM_ROUNDS_PART_2, lambda x: x % MODULO)
    else:
        raise ValueError(f"Invalid part: {part}")
    level = find_level_of_monkey_bussines(monkeys)
    print(level)


def play_game(monkeys: list[Monkey], num_rounds: int, manage_worry: Callable[[int], int]):
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey_items, monkey.items = monkey.items, []
            for item in monkey_items:
                new_item = monkey.operation(item)
                new_item = manage_worry(new_item)
                test = monkey.test(new_item)
                monkeys[monkey.throw(test)].items.append(new_item)
                monkey.inspected_items += 1


def find_level_of_monkey_bussines(monkeys: list[Monkey]) -> int:
    sorted_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspected_items, reverse=True)
    return sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items


def read_notes(notes_file: TextIO) -> list[Monkey]:
    monkeys = []
    for monkey_notes in iter_monkey_notes(notes_file):
        monkey = parse_monkey_notes(monkey_notes)
        monkeys.append(monkey)
    return monkeys


def iter_monkey_notes(notes_file: TextIO) -> Generator[str, None, None]:
    line = next(notes_file)
    while line is not None:
        monkey = ""
        while line is not None and line != "\n":
            monkey += line
            line = next(notes_file, None)
        yield monkey
        line = next(notes_file, None)


def parse_monkey_notes(monkey_notes: str) -> Monkey:
    lines = monkey_notes.splitlines()
    starting_items = parse_starting_items(lines[1])
    operation = parse_operation(lines[2])
    test = parse_test(lines[3])
    throw = parse_throw(lines[4], lines[5])
    return Monkey(starting_items, operation, test, throw)


def parse_starting_items(line: str) -> list[int]:
    items = line.split(": ")[1].split(", ")
    return [int(item) for item in items]


def parse_operation(line: str) -> Callable[[int], int]:
    operation_str = line.split(": ")[1].split(" = ")[1]
    def operation(old: int) -> int:
        return eval(operation_str)
    return operation


def parse_test(line: str) -> Callable[[int], bool]:
    test_str = line.split(": ")[1]
    if test_str.startswith("divisible by "):
        divisor = int(test_str.split("divisible by ")[1])
        def test_divisible(dividend: int) -> bool:
            if dividend % divisor == 0:
                return True
            return False
        return test_divisible
    raise ValueError(f"Invalid test: {line}")


def parse_throw(line1: str, line2: str) -> Callable[[bool], int]:
    monkey_true = int(line1.split("monkey ")[1])
    monkey_false = int(line2.split("monkey ")[1])
    def throw(test: bool) -> int:
        if test:
            return monkey_true
        return monkey_false
    return throw


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
