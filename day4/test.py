import unittest

from main import create_assignment_pair, is_fully_contained, is_overlapped


class TestCreateAssignmentPair(unittest.TestCase):
    def test_first_pair(self):
        # 2-4,6-8
        assignment_pair = create_assignment_pair("2-4,6-8")

        expected_first_elf = [2, 3, 4]
        expected_second_elf = [6, 7, 8]
        self.assertEqual(assignment_pair.first_elf, expected_first_elf)
        self.assertEqual(assignment_pair.second_elf, expected_second_elf)

    def test_second_pair(self):
        # 2-3,4-5
        assignment_pair = create_assignment_pair("2-3,4-5")

        expected_first_elf = [2, 3]
        expected_second_elf = [4, 5]
        self.assertEqual(assignment_pair.first_elf, expected_first_elf)
        self.assertEqual(assignment_pair.second_elf, expected_second_elf)


class TestFullyContained(unittest.TestCase):
    def test_first_pair(self):
        # 2-4,6-8
        assignment_pair = create_assignment_pair("2-4,6-8")

        self.assertFalse(is_fully_contained(assignment_pair))

    def test_second_pair(self):
        # 2-3,4-5
        assignment_pair = create_assignment_pair("2-3,4-5")

        self.assertFalse(is_fully_contained(assignment_pair))

    def test_fourth_pair(self):
        # 2-8,3-7
        assignment_pair = create_assignment_pair("2-8,3-7")

        self.assertTrue(is_fully_contained(assignment_pair))

    def test_fifth_pair(self):
        # 6-6,4-6
        assignment_pair = create_assignment_pair("6-6,4-6")

        self.assertTrue(is_fully_contained(assignment_pair))


class TestOverlapAtAll(unittest.TestCase):
    def test_first_pair(self):
        # 2-4,6-8
        assignment_pair = create_assignment_pair("2-4,6-8")

        self.assertFalse(is_overlapped(assignment_pair))

    def test_second_pair(self):
        # 2-3,4-5
        assignment_pair = create_assignment_pair("2-3,4-5")

        self.assertFalse(is_overlapped(assignment_pair))

    def test_third_pair(self):
        # 5-7,7-9
        assignment_pair = create_assignment_pair("5-7,7-9")

        self.assertTrue(is_overlapped(assignment_pair))

    def test_fifth_pair(self):
        # 6-6,4-6
        assignment_pair = create_assignment_pair("6-6,4-6")

        self.assertTrue(is_overlapped(assignment_pair))


if __name__ == "__main__":
    unittest.main()
