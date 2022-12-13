import unittest

from main import parse_height, parse_height_map, Coordinate


class TestParseChar(unittest.TestCase):
    def test_parse_a(self):
        height = parse_height("a")
        self.assertEqual(height, 0)

    def test_parse_z(self):
        height = parse_height("z")
        self.assertEqual(height, 25)

    def test_parse_start(self):
        height = parse_height("S")
        self.assertEqual(height, 0)

    def test_parse_end(self):
        height = parse_height("E")
        self.assertEqual(height, 25)


class TestCoordinate(unittest.TestCase):
    def test_coordinate_equality(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(1, 2)
        self.assertEqual(coord1, coord2)

    def test_coordinate_inequality(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(2, 1)
        self.assertNotEqual(coord1, coord2)

    def test_coordinate_sum(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(2, 1)
        coord3 = coord1 + coord2
        self.assertEqual(coord3, Coordinate(3, 3))


class TestFunctional(unittest.TestCase):
    def test_parse_height_map(self):
        with open("example.txt", "r") as f:
            height_map, source_coordinates, target_coordinates = parse_height_map(f)
        self.assertEqual(source_coordinates, Coordinate(0, 0))
        self.assertEqual(target_coordinates, Coordinate(2, 5))
        self.assertEqual(len(height_map), 5)
        self.assertEqual(len(height_map[0]), 8)


if __name__ == "__main__":
    unittest.main()
