import unittest

from main import Direction, Position, move_head, move_tail


class TestMoveHead(unittest.TestCase):
    def test_move_up(self):
        initial_position = Position(0, 0)
        direction = Direction.UP
        expected_position = Position(0, 1)
        self.assertEqual(move_head(initial_position, direction), expected_position)

    def test_move_down(self):
        initial_position = Position(2, 2)
        direction = Direction.DOWN
        expected_position = Position(2, 1)
        self.assertEqual(move_head(initial_position, direction), expected_position)

    def test_move_right(self):
        initial_position = Position(2, 2)
        direction = Direction.RIGHT
        expected_position = Position(3, 2)
        self.assertEqual(move_head(initial_position, direction), expected_position)

    def test_move_left(self):
        initial_position = Position(2, 2)
        direction = Direction.LEFT
        expected_position = Position(1, 2)
        self.assertEqual(move_head(initial_position, direction), expected_position)


class TestMoveTail(unittest.TestCase):
    def test_example_0(self):
        head_position = Position(0, 0)
        tail_position = Position(0, 0)
        expected_position = Position(0, 0)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_1(self):
        head_position = Position(0, 1)
        tail_position = Position(0, 0)
        expected_position = Position(0, 0)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_1_neg(self):
        head_position = Position(0, 1)
        tail_position = Position(0, 3)
        expected_position = Position(0, 2)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_2(self):
        head_position = Position(0, 2)
        tail_position = Position(0, 0)
        expected_position = Position(0, 1)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_3(self):
        head_position = Position(4, 2)
        tail_position = Position(3, 0)
        expected_position = Position(4, 1)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_4(self):
        head_position = Position(4, 1)
        tail_position = Position(3, 0)
        expected_position = Position(3, 0)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_5(self):
        head_position = Position(2, 0)
        tail_position = Position(0, 0)
        expected_position = Position(1, 0)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_5_neg(self):
        head_position = Position(0, 0)
        tail_position = Position(2, 0)
        expected_position = Position(1, 0)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)

    def test_example_6(self):
        head_position = Position(2, 4)
        tail_position = Position(4, 3)
        expected_position = Position(3, 4)
        self.assertEqual(move_tail(tail_position, head_position), expected_position)


if __name__ == "__main__":
    unittest.main()
