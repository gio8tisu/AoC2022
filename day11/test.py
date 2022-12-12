import unittest

from main import Monkey, parse_monkey_notes, parse_operation, parse_starting_items, parse_test, parse_throw, play_game, read_notes


class TestParseMonkeyNotes(unittest.TestCase):
    def test_parse_starting_items(self):
        line = "  Starting items: 79, 98"
        expected = [79, 98]
        actual = parse_starting_items(line)
        self.assertEqual(expected, actual)

    def test_parse_operation_1(self):
        line = "  Operation: new = old * 19"
        operation = parse_operation(line)
        self.assertEqual(19, operation(1))
        self.assertEqual(38, operation(2))

    def test_parse_operation_2(self):
        line = "  Operation: new = old * old"
        operation = parse_operation(line)
        self.assertEqual(1, operation(1))
        self.assertEqual(4, operation(2))

    def test_parse_test_1(self):
        line = "  Test: divisible by 23"
        test = parse_test(line)
        self.assertTrue(test(23))
        self.assertFalse(test(24))
        self.assertTrue(test(46))

    def test_parse_test_2(self):
        line = "  Test: divisible by 13"
        test = parse_test(line)
        self.assertTrue(test(13))
        self.assertFalse(test(14))
        self.assertTrue(test(26))

    def test_parse_throw(self):
        line1 = "    If true: throw to monkey 2"
        line2 = "    If false: throw to monkey 3"
        throw = parse_throw(line1, line2)
        self.assertEqual(2, throw(True))
        self.assertEqual(3, throw(False))

    def test_parse_monkey_1(self):
        monkey_notes = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""
        monkey = parse_monkey_notes(monkey_notes)
        expected = Monkey(
            items=[79, 98],
            operation=lambda old: old * 19,
            test=lambda new: new % 23 == 0,
            throw=lambda test: 2 if test else 3,
        )
        self.assertEqual(monkey.items, expected.items)
        self.assertEqual(monkey.operation(79), expected.operation(79))
        self.assertEqual(monkey.operation(98), expected.operation(98))
        self.assertEqual(monkey.test(79 * 19), expected.test(79 * 19))
        self.assertEqual(monkey.test(98 * 19), expected.test(98 * 19))
        self.assertEqual(monkey.throw(True), expected.throw(True))
        self.assertEqual(monkey.throw(False), expected.throw(False))


class TestIntegration(unittest.TestCase):
    def test_example_inspected_items(self):
        with open("example.txt", "r") as file:
            monkeys = read_notes(file)
            play_game(monkeys)
            self.assertEqual(monkeys[0].inspected_items, 101)
            self.assertEqual(monkeys[1].inspected_items, 95)
            self.assertEqual(monkeys[2].inspected_items, 7)
            self.assertEqual(monkeys[3].inspected_items, 105)


if __name__ == "__main__":
    unittest.main()
