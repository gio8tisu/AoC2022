import unittest

from main import count_visible_trees, is_visible


class TestCountVisible(unittest.TestCase):
    def test_visible_trees_count(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        result = count_visible_trees(grid)
        self.assertEqual(result, 21)

    def test_is_visible_edges(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        # Top edge
        self.assertEqual(is_visible(grid, 0, 0), True)
        self.assertEqual(is_visible(grid, 0, 1), True)
        self.assertEqual(is_visible(grid, 0, 2), True)
        self.assertEqual(is_visible(grid, 0, 3), True)
        self.assertEqual(is_visible(grid, 0, 4), True)
        # Left edge
        self.assertEqual(is_visible(grid, 1, 0), True)
        self.assertEqual(is_visible(grid, 2, 0), True)
        self.assertEqual(is_visible(grid, 3, 0), True)
        self.assertEqual(is_visible(grid, 4, 0), True)
        # Right edge
        self.assertEqual(is_visible(grid, 1, 4), True)
        self.assertEqual(is_visible(grid, 2, 4), True)
        self.assertEqual(is_visible(grid, 3, 4), True)
        self.assertEqual(is_visible(grid, 4, 4), True)
        # Bottom edge
        self.assertEqual(is_visible(grid, 4, 1), True)
        self.assertEqual(is_visible(grid, 4, 2), True)
        self.assertEqual(is_visible(grid, 4, 3), True)

    def test_is_visible_top_left_5(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 1, 1), True)

    def test_is_visible_top_middle_5(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 1, 2), True)

    def test_is_visible_top_right_1(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 1, 3), False)

    def test_is_visible_left_middle_5(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 2, 1), True)

    def test_is_visible_center_3(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 2, 2), False)

    def test_is_visible_right_middle_3(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 2, 3), True)

    def test_is_visible_bottom_left_3(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 3, 1), False)

    def test_is_visible_bottom_middle_5(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 3, 2), True)

    def test_is_visible_bottom_right_4(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(is_visible(grid, 3, 3), False)


if __name__ == "__main__":
    unittest.main()
