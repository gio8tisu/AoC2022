import unittest

from main import create_crates_configuration, CranePart1, CranePart2


class TestCrateCreation(unittest.TestCase):
    def test_example(self):
        crate_drawing = ("\n" +
        "    [D]    \n" +
        "[N] [C]    \n" +
        "[Z] [M] [P]\n" +
        " 1   2   3 \n")
        crate_configuration = create_crates_configuration(crate_drawing)
        expected = [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"],
        ]
        self.assertEqual(crate_configuration, expected)

    def test_example_alt1(self):
        crate_drawing = ("\n" +
        "[D]        \n" +
        "[N] [C]    \n" +
        "[Z] [M] [P]\n" +
        " 1   2   3 \n")
        crate_configuration = create_crates_configuration(crate_drawing)
        expected = [
            ["Z", "N", "D"],
            ["M", "C"],
            ["P"],
        ]
        self.assertEqual(crate_configuration, expected)

    def test_example_alt2(self):
        crate_drawing = ("\n" +
        "        [D]\n" +
        "[N] [C] [A]\n" +
        "[Z] [M] [P]\n" +
        " 1   2   3 \n")
        crate_configuration = create_crates_configuration(crate_drawing)
        expected = [
            ["Z", "N"],
            ["M", "C"],
            ["P", "A", "D"],
        ]
        self.assertEqual(crate_configuration, expected)


class TetsCranePart1(unittest.TestCase):
    def test_example_move_1(self):
        crane = CranePart1()
        crate_configuration = [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"],
        ]
        crane.move_crate(crate_configuration, 1, 2, 1)
        expected = [
            ["Z", "N", "D"],
            ["M", "C"],
            ["P"],
        ]
        self.assertEqual(crate_configuration, expected)

    def test_example_move_2(self):
        crane = CranePart1()
        crate_configuration = [
            ["Z", "N", "C"],
            ["M"],
            ["P", "A", "D"],
        ]
        crane.move_crate(crate_configuration, 3, 1, 3)
        expected = [
            [],
            ["M"],
            ["P", "A", "D", "C", "N", "Z"],
        ]
        self.assertEqual(crate_configuration, expected)


class TetsCranePart2(unittest.TestCase):
    def test_example_move_1(self):
        crane = CranePart2()
        crate_configuration = [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"],
        ]
        crane.move_crate(crate_configuration, 1, 2, 1)
        expected = [
            ["Z", "N", "D"],
            ["M", "C"],
            ["P"],
        ]
        self.assertEqual(crate_configuration, expected)

    def test_example_move_3(self):
        crane = CranePart2()
        crate_configuration = [
            ["Z", "N", "D"],
            ["M", "C"],
            ["P"],
        ]
        crane.move_crate(crate_configuration, 3, 1, 3)
        expected = [
            [],
            ["M", "C"],
            ["P", "Z", "N", "D"],
        ]
        self.assertEqual(crate_configuration, expected)


if __name__ == "__main__":
    unittest.main()
