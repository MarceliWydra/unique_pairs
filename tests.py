from collections import defaultdict
from unittest import TestCase

from main import calculate_sum_of_pairs, find_pairs_with_equal_sum


class TestCalculateSumOfPairs(TestCase):
    def test_calculate_sum_of_pairs(self):
        self.maxDiff = None
        input_array = [4, 23, 65, 67, 24, 12, 86]
        # list of pairs and their sum from elements in input_array
        expected_output = defaultdict(
            list,
            {
                27: [(4, 23)],
                69: [(4, 65)],
                71: [(4, 67)],
                28: [(4, 24)],
                16: [(4, 12)],
                90: [(4, 86), (23, 67)],
                88: [(23, 65)],
                47: [(23, 24)],
                35: [(23, 12)],
                109: [(23, 86)],
                132: [(65, 67)],
                89: [(65, 24)],
                77: [(65, 12)],
                151: [(65, 86)],
                91: [(67, 24)],
                79: [(67, 12)],
                153: [(67, 86)],
                36: [(24, 12)],
                110: [(24, 86)],
                98: [(12, 86)],
            },
        )
        self.assertEqual(calculate_sum_of_pairs(input_array), expected_output)

    def test_calculate_sum_of_pairs_empty_array(self):
        input_array = []
        self.assertEqual(calculate_sum_of_pairs(input_array), defaultdict(list, {}))

    def test_calculate_sum_of_pairs_single_element_array(self):
        input_array = [4]
        self.assertEqual(calculate_sum_of_pairs(input_array), defaultdict(list, {}))

    def test_calculate_sum_of_pairs_two_element_array(self):
        input_array = [4, 23]
        expcted_output = defaultdict(list, {27: [(4, 23)]})
        self.assertEqual(calculate_sum_of_pairs(input_array), expcted_output)

    def test_calculate_sum_of_pairs_when_negative_numbers(self):
        input_array = [-4, 23, 65, 67, 24, 12, 86]
        expected_output = defaultdict(
            list,
            {
                19: [(-4, 23)],
                61: [(-4, 65)],
                63: [(-4, 67)],
                20: [(-4, 24)],
                8: [(-4, 12)],
                82: [(-4, 86)],
                88: [(23, 65)],
                90: [(23, 67)],
                47: [(23, 24)],
                35: [(23, 12)],
                109: [(23, 86)],
                132: [(65, 67)],
                89: [(65, 24)],
                77: [(65, 12)],
                151: [(65, 86)],
                91: [(67, 24)],
                79: [(67, 12)],
                153: [(67, 86)],
                36: [(24, 12)],
                110: [(24, 86)],
                98: [(12, 86)],
            },
        )
        self.assertEqual(calculate_sum_of_pairs(input_array), expected_output)

    def test_calculate_sum_of_pairs_when_all_numbers_identical(self):
        input_array = [4, 4, 4, 4, 4, 4, 4]
        expected_output = defaultdict(list, {8: [(4, 4)]})
        print(calculate_sum_of_pairs(input_array))
        self.assertEqual(calculate_sum_of_pairs(input_array), expected_output)

    def test_calculate_sum_of_pairs_when_no_repeated_sum(self):
        input_array = [1, 2, 3, 10]
        expected_output = defaultdict(
            list,
            {
                3: [(1, 2)],
                4: [(1, 3)],
                11: [(1, 10)],
                5: [(2, 3)],
                12: [(2, 10)],
                13: [(3, 10)],
            },
        )
        self.assertEqual(calculate_sum_of_pairs(input_array), expected_output)


class TestFindPairsWithEqualSum(TestCase):
    def test_single_pair(self):
        pairs = defaultdict(list, {27: [(4, 23)], 25: [(2, 23)]})
        self.assertEqual(find_pairs_with_equal_sum(pairs), [])

    def test_multiple_pairs(self):
        pairs = defaultdict(list, {27: [(4, 23), (2, 25)], 25: [(2, 23), (3, 22)]})
        self.assertEqual(
            find_pairs_with_equal_sum(pairs),
            [([(4, 23), (2, 25)], 27), ([(2, 23), (3, 22)], 25)],
        )

    def test_empty_dictionary(self):
        pairs = defaultdict(list, {})
        self.assertEqual(find_pairs_with_equal_sum(pairs), [])
