import unittest

from main import find_directories_with_max_total_size, parse_input, Input, CommandType, FileSystem, File, Directory, create_filesystem, InputOutput, read_inputs_and_outputs


class TestParseInput(unittest.TestCase):
    def test_ls(self):
        input = "$ ls"
        result = parse_input(input)
        expected = Input(command_type=CommandType.LS, arguments=[])
        self.assertEqual(result, expected)

    def test_cd_no_args(self):
        input = "$ cd"
        result = parse_input(input)
        expected = Input(command_type=CommandType.CD, arguments=[])
        self.assertEqual(result, expected)

    def test_cd_args(self):
        input = "$ cd /"
        result = parse_input(input)
        expected = Input(command_type=CommandType.CD, arguments=["/"])
        self.assertEqual(result, expected)


class TestFileSystem(unittest.TestCase):
    def test_cd_absolute(self):
        root = Directory("/", None, [])
        expected = Directory("a", root, [])
        root.contents.append(expected)
        filesystem = FileSystem(0, root)
        filesystem.cd("/a")
        self.assertEqual(filesystem.current, expected)

    def test_cd_absolute_final_slash(self):
        root = Directory("/", None, [])
        expected = Directory("a", root, [])
        root.contents.append(expected)
        filesystem = FileSystem(0, root)
        filesystem.cd("/a/")
        self.assertEqual(filesystem.current, expected)

    def test_cd_relative(self):
        root = Directory("/", None, [])
        expected = Directory("a", root, [])
        root.contents.append(expected)
        filesystem = FileSystem(0, root)
        filesystem.cd("a")
        self.assertEqual(filesystem.current, expected)

    def test_cd_relative_final_slash(self):
        root = Directory("/", None, [])
        expected = Directory("a", root, [])
        root.contents.append(expected)
        filesystem = FileSystem(0, root)
        filesystem.cd("a/")
        self.assertEqual(filesystem.current, expected)

    def test_cd_up(self):
        root = Directory("/", None, [])
        a = Directory("a", root, [])
        root.contents.append(a)
        filesystem = FileSystem(0, root)
        filesystem.current = a
        filesystem.cd("..")
        self.assertEqual(filesystem.current, root)

    def test_cd_root(self):
        root = Directory("/", None, [])
        a = Directory("a", root, [])
        root.contents.append(a)
        filesystem = FileSystem(0, root)
        filesystem.current = a
        filesystem.cd("/")
        self.assertEqual(filesystem.current, root)


class TestCreateFileSystem(unittest.TestCase):
    def test_create_root_with_one_file(self):
        """
        $ cd /
        $ ls
        14848514 b.txt
        """
        inputs_outputs = [
            InputOutput(
                input=Input(command_type=CommandType.CD, arguments=["/"]),
                output=[],
            ),
            InputOutput(
                input=Input(command_type=CommandType.LS, arguments=[]),
                output=["14848514 b.txt"],
            )
        ]
        result = create_filesystem(inputs_outputs)
        expected = FileSystem(
            0,
            root=Directory(
                name="/",
                parent=None,
                contents=[
                    File(name="b.txt", size=14848514),
                ],
            )
        )
        self.assertEqual(result, expected)

    def test_create_root_with_one_dir(self):
        """
        $ cd /
        $ ls
        dir a
        $ cd a
        $ ls
        8504156 c.dat
        """
        inputs_outputs = [
            InputOutput(
                input=Input(command_type=CommandType.CD, arguments=["/"]),
                output=[],
            ),
            InputOutput(
                input=Input(command_type=CommandType.LS, arguments=[]),
                output=["dir a"],
            ),
            InputOutput(
                input=Input(command_type=CommandType.CD, arguments=["a"]),
                output=[],
            ),
            InputOutput(
                input=Input(command_type=CommandType.LS, arguments=[]),
                output=["8504156 c.dat"],
            ),
        ]
        result = create_filesystem(inputs_outputs)
        root = Directory(
            name="/",
            parent=None,
            contents=[],
        )
        a = Directory(
            name="a",
            parent=root,
            contents=[
                File(name="c.dat", size=8504156),
            ]
        )
        root.contents.append(a)
        expected = FileSystem(0, root=root)
        self.assertEqual(result, expected)


class TestDirectoriesMaxSize(unittest.TestCase):
    def test_max_size_1(self):
        """
        $ cd /
        $ ls
        3 b.txt
        dir a
        $ cd a
        $ ls
        2 c.dat
        dir d
        $ cd d
        $ ls
        1 e.dat
        """
        root = Directory(
            name="/",
            parent=None,
            contents=[
                File(name="b.txt", size=3),
            ]
        )
        a = Directory(
            name="a",
            parent=root,
            contents=[
                File(name="c.dat", size=2),
            ]
        )
        d = Directory(
            name="d",
            parent=a,
            contents=[
                File(name="e.dat", size=1),
            ]
        )
        a.contents.append(d)
        root.contents.append(a)
        filesystem = FileSystem(0, root=root)
        result = find_directories_with_max_total_size(filesystem.root, 1)
        self.assertEqual(result, [d])

    def test_max_size_3(self):
        """
        $ cd /
        $ ls
        4 b.txt
        dir a
        $ cd a
        $ ls
        2 c.dat
        dir d
        $ cd d
        $ ls
        1 e.dat
        """
        root = Directory(
            name="/",
            parent=None,
            contents=[
                File(name="b.txt", size=4),
            ]
        )
        a = Directory(
            name="a",
            parent=root,
            contents=[
                File(name="c.dat", size=2),
            ]
        )
        d = Directory(
            name="d",
            parent=a,
            contents=[
                File(name="e.dat", size=1),
            ]
        )
        a.contents.append(d)
        root.contents.append(a)
        filesystem = FileSystem(0 ,root=root)
        result = find_directories_with_max_total_size(filesystem.root, 3)
        self.assertEqual(result, [a, d])


class TestIntegration(unittest.TestCase):
    def test_used_space(self):
        with open("example.txt", "r") as f:
            inputs_outputs = read_inputs_and_outputs(f)
            filesystem = create_filesystem(inputs_outputs)
        assert filesystem is not None
        self.assertEqual(filesystem.used_space, 48381165)

    def test_free_space(self):
        with open("example.txt", "r") as f:
            inputs_outputs = read_inputs_and_outputs(f)
            filesystem = create_filesystem(inputs_outputs)
        assert filesystem is not None
        self.assertEqual(filesystem.free_space, 21618835)


if __name__ == "__main__":
    unittest.main()
