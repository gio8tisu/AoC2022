import argparse
import sys
from typing import TextIO
from enum import Enum
from dataclasses import dataclass


class InstructionType(str, Enum):
    NO_OP = "noop"
    ADD_X = "addx"


@dataclass
class Instruction:
    type: InstructionType
    argument: int | None = None


def main(program_file: TextIO, part: int):
    program = read_program(program_file)
    if part == 1:
        interesting_cycles = [20, 60, 100, 140, 180, 220]
        x_values = execute_program_part_1(program, interesting_cycles)
        print(sum(c * x for c, x in zip(interesting_cycles, x_values)))
    elif part == 2:
        display = execute_program_part_2(program)
        print()
        print(display)
    else:
        raise ValueError(f"Invalid part: {part}")


def read_program(motions_file: TextIO) -> list[Instruction]:
    instructions = []
    for line in motions_file.readlines():
        split_line = line.strip().split(" ")
        instruction_type = InstructionType(split_line[0])
        if instruction_type == InstructionType.NO_OP:
            instructions.append(Instruction(instruction_type))
        elif instruction_type == InstructionType.ADD_X:
            instructions.append(Instruction(instruction_type, int(split_line[1])))
        else:
            raise ValueError(f"Invalid instruction type: {instruction_type}")
    return instructions


def execute_program_part_1(program: list[Instruction], interesting_cycles: list[int]) -> list[int]:
    interesting_cycles_x_value = []
    x = 1
    clock = 1
    program_iter = iter(program)
    instruction = next(program_iter, None)
    while instruction is not None:
        if clock in interesting_cycles:
            interesting_cycles_x_value.append(x)
        if instruction.type == InstructionType.ADD_X:
            clock += 1
            if clock in interesting_cycles:
                interesting_cycles_x_value.append(x)
            assert instruction.argument is not None
            x += instruction.argument
        instruction = next(program_iter, None)
        clock += 1
    if clock in interesting_cycles:
        interesting_cycles_x_value.append(x)
    return interesting_cycles_x_value


def execute_program_part_2(program: list[Instruction]) -> str:
    display = ""
    x = 1
    clock = 1
    program_iter = iter(program)
    instruction = next(program_iter, None)
    while instruction is not None:
        display += draw_pixel(x, clock)
        if instruction.type == InstructionType.ADD_X:
            clock += 1
            display += draw_pixel(x, clock)
            assert instruction.argument is not None
            x += instruction.argument
        instruction = next(program_iter, None)
        clock += 1
    return display


def draw_pixel(x: int, clock: int) -> str:
    result = "."
    c = (clock - 1) % 40
    if x - 1 <= c <= x + 1:
        result = "#"
    if c == 39:
        result += "\n"
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
