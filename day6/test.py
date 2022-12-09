import unittest

from main import get_start_marker_position, CircularQueue


class TestGetStartMarkerPositionPart1(unittest.TestCase):
    def test_example_1(self):
        queue = CircularQueue(4)
        stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(get_start_marker_position(stream, queue), 7)

    def test_example_2(self):
        queue = CircularQueue(4)
        stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(get_start_marker_position(stream, queue), 5)

    def test_example_3(self):
        queue = CircularQueue(4)
        stream = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(get_start_marker_position(stream, queue), 6)

    def test_example_4(self):
        queue = CircularQueue(4)
        stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(get_start_marker_position(stream, queue), 10)

    def test_example_5(self):
        queue = CircularQueue(4)
        stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(get_start_marker_position(stream, queue), 11)


class TestGetStartMarkerPositionPart2(unittest.TestCase):
    def test_example_1(self):
        queue = CircularQueue(14)
        stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(get_start_marker_position(stream, queue), 19)

    def test_example_2(self):
        queue = CircularQueue(14)
        stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(get_start_marker_position(stream, queue), 23)

    def test_example_3(self):
        queue = CircularQueue(14)
        stream = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(get_start_marker_position(stream, queue), 23)

    def test_example_4(self):
        queue = CircularQueue(14)
        stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(get_start_marker_position(stream, queue), 29)

    def test_example_5(self):
        queue = CircularQueue(14)
        stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(get_start_marker_position(stream, queue), 26)


if __name__ == "__main__":
    unittest.main()
