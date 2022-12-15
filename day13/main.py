import argparse
import sys
from typing import TextIO, Generator, TypeAlias, Iterable, Union
from itertools import chain


Packet: TypeAlias = list[Union[int, "Packet"]]


def main(packets_file: TextIO, part: int):
    if part == 1:
        packet_pairs = read_packets_part_1(packets_file)
        packets_in_right_order = find_packets_in_right_order(packet_pairs)
        print(sum(packets_in_right_order))
    elif part == 2:
        packet_pairs = read_packets_part_2(packets_file)
        packet_pairs.append([[2]])
        packet_pairs.append([[6]])
        sort_packets(packet_pairs)
        divider_packets_indices = find_divider_packets(packet_pairs)
        assert len(divider_packets_indices) == 2
        print(divider_packets_indices[0] * divider_packets_indices[1])
    else:
        raise ValueError(f"Invalid part: {part}")


def read_packets_part_1(packets_file: TextIO) -> Generator[tuple[Packet, Packet], None, None]:
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


def read_packets_part_2(packets_file: TextIO) -> list[Packet]:
    packets = []
    for line in packets_file.readlines():
        if line == "\n":
            continue
        packets.append(parse_packet(line.strip()))
    return packets


def parse_packet(packet: str) -> Packet:
    return eval(packet)


def find_packets_in_right_order(packet_pairs: Iterable[tuple[Packet, Packet]]) -> list[int]:
    ordered_indices = []
    for i, (left, right) in enumerate(packet_pairs, start=1):
        if is_packet_in_right_order(left, right):
            ordered_indices.append(i)
    return ordered_indices


def sort_packets(packet_pairs: list[Packet]):
    # Bubble sort.
    while True:
        swapped = False
        for i in range(len(packet_pairs) - 1):
            if not is_packet_in_right_order(packet_pairs[i], packet_pairs[i + 1]):
                packet_pairs[i], packet_pairs[i + 1] = packet_pairs[i + 1], packet_pairs[i]
                swapped = True
        if not swapped:
            break


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


def find_divider_packets(packets: list[Packet]) -> list[int]:
    divider_packets = []
    for i, packet in enumerate(packets, start=1):
        if is_divider_packet(packet):
            divider_packets.append(i)
    return divider_packets


def is_divider_packet(packet: Packet) -> bool:
    if isinstance(packet, int):
        return False
    return packet == [[2]] or packet == [[6]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
