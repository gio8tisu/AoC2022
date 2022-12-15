import argparse
import sys
from typing import TextIO, Generator, TypeAlias, Iterable, Union


Packet: TypeAlias = list[Union[int, "Packet"]]


def main(packets_file: TextIO, part: int):
    if part == 1:
        packet_pairs = read_packets(packets_file)
        packets_in_right_order = find_packets_in_right_order(packet_pairs)
        print(sum(packets_in_right_order))
    elif part == 2:
        raise NotImplementedError("Part 2 not implemented")
    else:
        raise ValueError(f"Invalid part: {part}")


def read_packets(packets_file: TextIO) -> Generator[tuple[Packet, Packet], None, None]:
    left = right = None
    for line in packets_file.readlines():
        if line == "\n":
            left = right = None
            continue
        if left is None:
            left = parse_packet(line.strip())
        elif right is None:
            right = parse_packet(line.strip())
            yield left, right
        else:
            raise ValueError("Invalid input")
    if left is not None and right is not None:
        yield left, right


def parse_packet(packet: str) -> Packet:
    return eval(packet)


def find_packets_in_right_order(packet_pairs: Iterable[tuple[Packet, Packet]]) -> list[int]:
    ordered_indices = []
    for i, (left, right) in enumerate(packet_pairs, start=1):
        if is_packet_in_right_order(left, right):
            ordered_indices.append(i)
    return ordered_indices


def is_packet_in_right_order(left: Packet, right: Packet) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            return left < right
        return None
    if isinstance(left, int) and isinstance(right, list):
        return is_packet_in_right_order([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return is_packet_in_right_order(left, [right])
    for l, r in zip(left, right):
        is_ordered = is_packet_in_right_order(l, r)
        if is_ordered is not None:
            return is_ordered
    if len(left) != len(right):
        return len(left) < len(right)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
