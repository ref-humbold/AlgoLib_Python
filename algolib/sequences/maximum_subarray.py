# -*- coding: utf-8 -*-
"""Algorithms for maximum subarray."""
from typing import Iterable, Sequence


def find_maximum_subarray(sequence: Iterable[float]) -> Iterable[float]:
    """Dynamically computes coherent subarray with maximal sum.

    :param sequence: the sequence of numbers
    :return: the maximum subarray"""
    actual_sum = 0
    actual_subarray = []
    maximal_sum = 0
    maximal_subarray = []

    for elem in sequence:
        if actual_sum < 0.0:
            actual_sum = 0
            actual_subarray = []

        actual_sum += elem
        actual_subarray.append(elem)

        if actual_sum > maximal_sum:
            maximal_sum = actual_sum
            maximal_subarray = actual_subarray[:]

    return iter(maximal_subarray)


def count_maximal_subsum(sequence: Sequence[float]) -> float:
    """Computes maximal sum from all coherent subarrays using interval tree.

    :param sequence: the sequence of numbers
    :return: the sum of maximum subarray"""
    size = 1

    while size < 2 * len(sequence):
        size *= 2

    interval_sums = [0.0] * size
    prefix_sums = [0.0] * size
    suffix_sums = [0.0] * size
    all_sums = [0.0] * size

    for i, elem in enumerate(sequence):
        index = size // 2 + i
        all_sums[index] += elem
        interval_sums[index] = max(all_sums[index], 0.0)
        prefix_sums[index] = max(all_sums[index], 0.0)
        suffix_sums[index] = max(all_sums[index], 0.0)
        index //= 2

        while index > 0:
            index_left = index + index
            index_right = index + index + 1
            interval_sums[index] = max(interval_sums[index_left], interval_sums[index_right],
                                       suffix_sums[index_left] + prefix_sums[index_right])
            prefix_sums[index] = max(prefix_sums[index_left],
                                     all_sums[index_left] + prefix_sums[index_right])
            suffix_sums[index] = max(suffix_sums[index_right],
                                     suffix_sums[index_left] + all_sums[index_right])
            all_sums[index] = all_sums[index_left] + all_sums[index_right]
            index //= 2

    return interval_sums[1]
