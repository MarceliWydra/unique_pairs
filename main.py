from collections import defaultdict
from typing import DefaultDict, List, Tuple


def calculate_sum_of_pairs(array: List[int]) -> List[Tuple[List[Tuple[int, int]], int]]:
    """
    Calculate the sum of pairs in a list of integers
    :param array: List of integers
    :return: List of pairs and their sum
    """
    sum_to_pairs = defaultdict(list)
    if len(array) < 2:
        return sum_to_pairs

    for i, num1 in enumerate(array):
        for num2 in array[i + 1 :]:
            pair = (num1, num2)
            reversed_pair = (num2, num1)
            sum = num1 + num2
            if pair not in sum_to_pairs[sum] and reversed_pair not in sum_to_pairs[sum]:
                sum_to_pairs[num1 + num2].append((num1, num2))

    return sum_to_pairs


def find_pairs_with_equal_sum(
    pairs: DefaultDict[int, List]
) -> List[Tuple[List[Tuple[int, int]], int]]:
    """
    Find pairs with equal sum
    :param pairs: Dictionary where key is the sum of pairs and value is the list of pairs
    :return: List of pairs and their sum
    """
    return [(pairs[key], key) for key in pairs if len(pairs[key]) > 1]


if __name__ == "__main__":
    input_array = [4, 23, 65, 67, 24, 12, 86]
    pairs = calculate_sum_of_pairs(input_array)
    pairs_with_equal_sums = find_pairs_with_equal_sum(pairs)
    for pairs_with_sum in pairs_with_equal_sums:
        formatted_pairs = ", ".join(
            [f"({pair[0]}, {pair[1]})" for pair in pairs_with_sum[0]]
        )
        print(f"Pairs: {formatted_pairs} have sum : {pairs_with_sum[1]}")
