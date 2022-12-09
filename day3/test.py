import unittest

from main import create_rucksack, find_duplicate, content_to_int, Rucksack, find_badge, group_rucksacks


class TestCreateRucksack(unittest.TestCase):
    def test_create_rucksack(self):
        line = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected = Rucksack(
                ["v", "J", "r", "w", "p", "W", "t", "w", "J", "g", "W", "r"],
                ["h", "c", "s", "F", "M", "M", "f", "F", "F", "h", "F", "p"]
        )

        self.assertEqual(create_rucksack(line), expected)


class TestDuplicates(unittest.TestCase):
    def test_find_duplicate(self):
        rucksack = Rucksack(
                ["v", "J", "r", "w", "p", "W", "t", "w", "J", "g", "W", "r"],
                ["h", "c", "s", "F", "M", "M", "f", "F", "F", "h", "F", "p"]
        )
        expected = "p"

        self.assertEqual(find_duplicate(rucksack), expected)


class TestContentValue(unittest.TestCase):
    def test_p(self):
        self.assertEqual(content_to_int("p"), 16)

    def test_L(self):
        self.assertEqual(content_to_int("L"), 38)

    def test_P(self):
        self.assertEqual(content_to_int("P"), 42)

    def test_v(self):
        self.assertEqual(content_to_int("v"), 22)

    def test_t(self):
        self.assertEqual(content_to_int("t"), 20)

    def test_s(self):
        self.assertEqual(content_to_int("s"), 19)


class TestGrouping(unittest.TestCase):
    def test_group_rucksack(self):
        rucksacks = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        grouped_rucksacks = group_rucksacks(rucksacks)

        expected = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
            ["J", "K", "L"]
        ]
        self.assertEqual(grouped_rucksacks, expected)


class TestFindBadges(unittest.TestCase):
    def test_group1(self):
        # vJrwpWtwJgWrhcsFMMfFFhFp
        # jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        # PmmdzqPrVvPwwTWBwg
        rucksack1 = Rucksack(
                ["v", "J", "r", "w", "p", "W", "t", "w", "J", "g", "W", "r"],
                ["h", "c", "s", "F", "M", "M", "f", "F", "F", "h", "F", "p"]
        )
        rucksack2 = Rucksack(
                ["j", "q", "H", "R", "N", "q", "R", "j", "q", "z", "j", "G", "D", "L", "G", "L"],
                ["r", "s", "F", "M", "f", "F", "Z", "S", "r", "L", "r", "F", "Z", "s", "S", "L"]
        )
        rucksack3 = Rucksack(
                ["P", "m", "m", "d", "z", "q", "P", "r", "V"],
                ["v", "P", "w", "w", "T", "W", "B", "w", "g"]
        )
        badge = find_badge([rucksack1, rucksack2, rucksack3])

        self.assertEqual(badge, "r")


    def test_group2(self):
        # wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        # ttgJtRGJQctTZtZT
        # CrZsJsPPZsGzwwsLwLmpwMDw
        rucksack1 = Rucksack(
                ["w", "M", "q", "v", "L", "M", "Z", "H", "h", "H", "M", "v", "w", "L", "H"],
                ["j", "b", "v", "c", "j", "n", "n", "S", "B", "n", "v", "T", "Q", "F", "n"]
        )
        rucksack2 = Rucksack(
                ["t", "t", "g", "J", "t", "R", "G", "J"],
                ["Q", "c", "t", "T", "Z", "t", "Z", "T"]
        )
        rucksack3 = Rucksack(
                ["C", "r", "Z", "s", "J", "s", "P", "P", "Z", "s", "G", "z"],
                ["w", "w", "s", "L", "w", "L", "m", "p", "w", "M", "D", "w"]
        )
        badge = find_badge([rucksack1, rucksack2, rucksack3])

        self.assertEqual(badge, "Z")
