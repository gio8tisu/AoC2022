import argparse
import sys
from typing import TextIO


class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.buffer: list[str] = []
        self.position = 0

    def add(self, char: str):
        if len(self.buffer) < self.size:
            self.buffer.append(char)
        else:
            self.buffer[self.position] = char
            self.position = (self.position + 1) % self.size

    def __len__(self):
        return self.size


def main(data_stream_file: TextIO, part: int):
    data_stream = data_stream_file.readline().strip()
    queue = create_queue(part)
    start_marker_positorion = get_start_marker_position(data_stream, queue)
    print(start_marker_positorion)


def get_start_marker_position(data_stream: str, queue) -> int:
    for i in range(queue.size):
        queue.add(data_stream[i])

    for i, char in enumerate(data_stream[queue.size:], start=queue.size):
        # Return index if all items in buffer are unique.
        if len(set(queue.buffer)) == queue.size:
            return i
        queue.add(char)
    raise ValueError("No start marker found")


def create_queue(part: int) -> CircularQueue:
    if part == 1:
        return CircularQueue(4)
    elif part == 2:
        return CircularQueue(14)
    else:
        raise ValueError("Part must be 1 or 2")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
