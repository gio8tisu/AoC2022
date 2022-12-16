import unittest

from main import Cave, FlowIntoAbyss


class TestCave(unittest.TestCase):
    def test_add_rock_strucure(self):
        cave = Cave()
        path = [(0, 0), (2, 0), (2, 2)]
        cave.add_rock_structure(path)
        self.assertEqual(cave.rocks, {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)})

    def test_pour_sand_straight_down_rock(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (500, 9), (501, 9), (502, 9)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(500, 8)})

    def test_pour_sand_left_rock(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (500, 9), (500, 8), (501, 9), (502, 9)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(499, 8)})

    def test_pour_sand_right_rock(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (499, 9), (499, 8), (500, 9), (500, 8), (501, 9), (502, 9)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(501, 8)})

    def test_pour_sand_straight_down_sand(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (499, 10), (500, 10), (501, 10), (501, 9), (502, 9)}
        cave.sand = {(500, 9)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(500, 9), (500, 8)})

    def test_pour_sand_left_sand(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (500, 9), (501, 9), (502, 9)}
        cave.sand = {(500, 8)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(500, 8), (499, 8)})

    def test_pour_sand_right_sand(self):
        cave = Cave()
        cave.rocks = {(498, 9), (499, 9), (500, 9), (501, 9), (502, 9)}
        cave.sand = {(499, 8), (500, 8)}
        cave.pour_sand()
        self.assertEqual(cave.sand, {(499, 8), (500, 8), (501, 8)})

    def test_pour_sand_flow_into_abyss(self):
        cave = Cave()
        with self.assertRaises(FlowIntoAbyss):
            cave.pour_sand()


if __name__ == "__main__":
    unittest.main()
