import argparse
import sys
from typing import TextIO, Generator, Iterable, Optional, Union
from dataclasses import dataclass
from enum import Enum


TOTAL_DISK_SPACE = 70000000
NEEDED_SPACE_FOR_UPDATE = 30000000


def main(terminal_output_file: TextIO, part: int):
    inputs_outputs = read_inputs_and_outputs(terminal_output_file)
    filesystem = create_filesystem(inputs_outputs)
    assert filesystem is not None, "No filesystem created"
    if part == 1:
        dirs = find_directories_with_max_total_size(filesystem.root, 100000)
        print(sum([d.size for d in dirs]))
    elif part == 2:
        if filesystem.free_space >= NEEDED_SPACE_FOR_UPDATE:
            return
        space_to_free_up = NEEDED_SPACE_FOR_UPDATE - filesystem.free_space
        sizes = get_directories_sizes(filesystem.root)
        for size in sizes:
            if size >= space_to_free_up:
                print(size)
                break
    else:
        raise ValueError(f"Invalid part: {part}")


class CommandType(str, Enum):
    CD = "cd"
    LS = "ls"


@dataclass
class Input:
    command_type: CommandType
    arguments: list[str]


@dataclass
class InputOutput:
    input: Input
    output: list[str]


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Optional["Directory"]
    contents: list[Union["Directory", File]]

    @property
    def size(self) -> int:
        return sum([content.size for content in self.contents])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Directory):
            return False
        return self.name == other.name and self.contents == other.contents


class FileSystem:
    total_disk_space: int
    root: Directory
    current: Directory

    def __init__(self, total_disk_space: int, root: Directory | None = None):
        self.root = root or Directory("/", None, [])
        self.current = self.root
        self.total_disk_space = total_disk_space

    @property
    def used_space(self) -> int:
        return self.root.size

    @property
    def free_space(self) -> int:
        return self.total_disk_space - self.root.size

    def cd(self, path: str) -> None:
        if path == "..":
            assert self.current.parent is not None, "Cannot go up from root"
            self.current = self.current.parent
        else:
            if path.startswith("/"):
                path = path[1:]
                self.current = self.root
            next_directory, *rest = path.split("/")
            while next_directory:
                for content in self.current.contents:
                    if content.name == next_directory:
                        assert isinstance(
                            content, Directory), "Cannot cd into a file"
                        self.current = content
                        break
                if rest:
                    next_directory = rest.pop(0)
                    self.cd(next_directory)
                else:
                    next_directory = None

    def add_content(self, content: File | Directory) -> None:
        self.current.contents.append(content)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FileSystem):
            return False
        return self.root == other.root

    def __repr__(self) -> str:
        return f"FileSystem(root={self.root}, current={self.current})"

    def __str__(self) -> str:
        return self._dir_str(self.root)

    def _file_str(self, file: File, indent: int = 0) -> str:
        return f"{'  ' * indent}- {file.name} (file, size={file.size})\n"

    def _dir_str(self, dir: Directory, indent: int = 0) -> str:
        result = f"{'  ' * indent}- {dir.name} (dir, size={dir.size})\n"
        for content in dir.contents:
            if isinstance(content, Directory):
                result += self._dir_str(content, indent + 1)
            else:
                result += self._file_str(content, indent + 1)
        return result


def read_inputs_and_outputs(terminal_output_file: TextIO) -> Generator[InputOutput, None, None]:
    current_input: Input | None = None
    current_output: list[str] = []
    for line in terminal_output_file.readlines():
        if line.startswith("$"):
            if current_input is not None:
                yield InputOutput(input=current_input, output=current_output)
            current_input = parse_input(line)
            current_output = []
        else:
            current_output.append(line.strip())
    if current_input is not None:
        yield InputOutput(input=current_input, output=current_output)


def parse_input(line: str) -> Input:
    _, command, *arguments = line.split()
    return Input(command_type=CommandType(command), arguments=arguments)


def create_filesystem(inputs_outputs: Iterable[InputOutput]) -> FileSystem | None:
    filesystem: FileSystem | None = None
    for input_output in inputs_outputs:
        if input_output.input.command_type == CommandType.CD:
            if filesystem is None and input_output.input.arguments[0] == "/":
                filesystem = FileSystem(total_disk_space=TOTAL_DISK_SPACE) 
            elif filesystem is None:
                raise ValueError("First command must be cd /")
            else:
                filesystem.cd(input_output.input.arguments[0])
        elif input_output.input.command_type == CommandType.LS:
            if filesystem is None:
                raise ValueError("First command must be cd /")
            for line in input_output.output:
                if line.startswith("dir"):
                    _, name = line.split(" ")
                    content = Directory(name, filesystem.current, [])
                else:
                    size, name = line.split(" ")
                    content = File(name=name, size=int(size))
                filesystem.add_content(content)
    return filesystem


def find_directories_with_max_total_size(directory: Directory, n: int) -> list[Directory]:
    result: list[Directory] = []
    if directory.size <= n:
        result.append(directory)
    for d in directory.contents:
        if isinstance(d, Directory):
            result += find_directories_with_max_total_size(d, n)
    return result


def get_directories_sizes(directory: Directory) -> list[int]:
    result: list[int] = []
    result.append(directory.size)
    for d in directory.contents:
        if isinstance(d, Directory):
            result += get_directories_sizes(d)
    return sorted(result)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    main(args.file, args.part)
