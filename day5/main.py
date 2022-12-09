import argparse
import sys
from typing import TextIO, TypeAlias, Protocol


Stack: TypeAlias = list[str]
CrateConfiguration: TypeAlias = list[Stack]


class Crane(Protocol):
    def move_crate(self, crate_configuration: CrateConfiguration, number: int, from_: int, to_: int):
        ...


def main(crate_configuration_and_procedure_file: TextIO, part: int):
    crane = crate_crane_from_part(part)
    crate_configuration, procedure = read_crate_configuration_and_procedure(crate_configuration_and_procedure_file)
    crate_configuration = execute_procedure(crate_configuration, procedure, crane)
    print("".join(s[-1] for s in crate_configuration))


def read_crate_configuration_and_procedure(crate_configuration_file: TextIO):
    crates_drawing = ""
    procedure: list[str] = []
    for line in crate_configuration_file.readlines():
        if line.startswith("move"):
            procedure.append(line.strip())
        elif line != "\n":
            crates_drawing += line

    crate_configuration = create_crates_configuration(crates_drawing)
    return crate_configuration, procedure


def create_crates_configuration(crates_drawing: str) -> CrateConfiguration:
    # Iterate from last line to first line.
    reversed_lines = reversed(crates_drawing.splitlines())
    number_of_stacks = len(next(reversed_lines).split())
    crate_configuration: CrateConfiguration = [[] for _ in range(number_of_stacks)]

    for line in reversed_lines:
        line = line.replace("[", "").replace("]", "").replace("    ", "  ").strip("\n")
        for i, c in enumerate(line):
            if c != " ":
                crate_configuration[i // 2].append(c)

    return crate_configuration


def execute_procedure(crate_configuration: CrateConfiguration, procedure: list[str], crane: Crane) -> CrateConfiguration:
    """
    Example:
    procedure = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]
    """
    for move in procedure:
        _, number, _, from_, _, to_ = move.split()
        number = int(number)
        from_ = int(from_)
        to_ = int(to_)
        crane.move_crate(crate_configuration, number, from_, to_)
    return crate_configuration


class CranePart1:
    def move_crate(self, crate_configuration: CrateConfiguration, number: int, from_: int, to_: int):
        for _ in range(number):
            crate_configuration[to_ - 1].append(crate_configuration[from_ - 1].pop())


class CranePart2:
    def move_crate(self, crate_configuration: CrateConfiguration, number: int, from_: int, to_: int):
        crates_to_move = crate_configuration[from_ - 1][-number:]
        crate_configuration[from_ - 1] = crate_configuration[from_ - 1][:-number]
        crate_configuration[to_ - 1].extend(crates_to_move)


def crate_crane_from_part(part: int) -> Crane:
    if part == 1:
        return CranePart1()
    elif part == 2:
        return CranePart2()
    else:
        raise ValueError(f"Invalid part: {part}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
