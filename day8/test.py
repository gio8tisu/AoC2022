import unittest
from unittest.mock import patch

from main import count_visible_trees, is_visible, tree_scenic_score, count_trees_in_up_direction, count_trees_in_down_direction, count_trees_in_right_direction, count_trees_in_left_direction


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


class TestScenicScore(unittest.TestCase):
    def test_scenic_score_top_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        with patch("main.count_trees_in_up_direction", return_value=1), patch("main.count_trees_in_down_direction", return_value=2), patch("main.count_trees_in_left_direction", return_value=1), patch("main.count_trees_in_right_direction", return_value=2):
            result = tree_scenic_score(grid, 1, 2)
        self.assertEqual(result, 4)

    def test_scenic_score_bottom_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        with patch("main.count_trees_in_up_direction", return_value=2), patch("main.count_trees_in_down_direction", return_value=1), patch("main.count_trees_in_left_direction", return_value=2), patch("main.count_trees_in_right_direction", return_value=2):
            result = tree_scenic_score(grid, 3, 2)
        self.assertEqual(result, 8)

    def test_count_trees_up_top_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        result = count_trees_in_up_direction(grid, 1, 2)
        self.assertEqual(result, 1)

    def test_count_trees_left_top_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        result = count_trees_in_left_direction(grid, 1, 2)
        self.assertEqual(result, 1)

    def test_count_trees_right_top_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        result = count_trees_in_right_direction(grid, 1, 2)
        self.assertEqual(result, 2)

    def test_count_trees_down_top_middle_five(self):
        grid = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        result = count_trees_in_down_direction(grid, 1, 2)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
