import unittest

from main import parse_packet, is_packet_in_right_order, is_divider_packet, sort_packets


class TestParsePacket(unittest.TestCase):
    def test_parse_packet_1(self):
        expected = [1, 1, 3, 1, 1]
        self.assertEqual(parse_packet("[1,1,3,1,1]"), expected)

    def test_parse_packet_2(self):
        expected = [[1], [2, 3, 4]]
        self.assertEqual(parse_packet("[[1],[2,3,4]]"), expected)

    def test_parse_packet_3(self):
        expected = [[8, 7, 6]]
        self.assertEqual(parse_packet("[[8,7,6]]"), expected)

    def test_parse_packet_4(self):
        expected = []
        self.assertEqual(parse_packet("[]"), expected)


class TestIsPacketInRightOrder(unittest.TestCase):
    def test_is_right_order_ordered_pair_integers(self):
        left = 1
        right = 2
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_unordered_pair_integers(self):
        left = 2
        right = 1
        self.assertFalse(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_one_list(self):
        left = 1
        right = [2]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_one_list_alt(self):
        left = [1]
        right = 2
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_lists_one_item(self):
        left = [1]
        right = [2]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_lists_short(self):
        left = [1, 1]
        right = [1, 2]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_lists_different_size(self):
        left = [1, 1]
        right = [1, 1, 5, 1, 1]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_lists_different_size_right(self):
        left = [1, 1, 5, 1, 1]
        right = [1, 1]
        self.assertFalse(is_packet_in_right_order(left, right))

    def test_is_right_order_ordered_pair_lists(self):
        left = [1, 1, 3, 1, 1]
        right = [1, 1, 5, 1, 1]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_pair_2(self):
        left = [[1], [2, 3, 4]]
        right = [[1], 4]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_pair_5(self):
        left = [7, 7, 7, 7]
        right = [7, 7, 7]
        self.assertFalse(is_packet_in_right_order(left, right))

    def test_pair_6(self):
        left = []
        right = [3]
        self.assertTrue(is_packet_in_right_order(left, right))

    def test_pair_6_alt(self):
        left = [3]
        right = []
        self.assertFalse(is_packet_in_right_order(left, right))

    def test_pair_7(self):
        left = [[]]
        right = []
        self.assertFalse(is_packet_in_right_order(left, right))


class TestIsDividerPacket(unittest.TestCase):
    def test_is_divider_2_true(self):
        packet = [[2]]
        self.assertTrue(is_divider_packet(packet))

    def test_is_divider_6_true(self):
        packet = [[6]]
        self.assertTrue(is_divider_packet(packet))

    def test_is_divider_other_false(self):
        packet = [6]
        self.assertFalse(is_divider_packet(packet))


class TestSortPackets(unittest.TestCase):
    def test_example(self):
        packets = [
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
            [[1], [2, 3, 4]],
            [[1], 4],
            [9],
            [[8, 7, 6]],
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
            [7, 7, 7, 7],
            [7, 7, 7],
            [],
            [3],
            [[[]]],
            [[]],
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            [[2]],
            [[6]]
        ]
        expected = [
            [],
            [[]],
            [[[]]],
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
            [[1], [2, 3, 4]],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [[1], 4],
            [[2]],
            [3],
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
            [[6]],
            [7, 7, 7],
            [7, 7, 7, 7],
            [[8, 7, 6]],
            [9]
        ]
        sort_packets(packets)
        self.assertEqual(packets, expected)


if __name__ == "__main__":
    unittest.main()
