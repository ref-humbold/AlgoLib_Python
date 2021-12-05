# -*- coding: utf-8 -*-
"""Algorithms for maximum subarray"""
from typing import Iterable, Sequence


def find_maximum_subarray(iterable: Iterable[float]) -> Iterable[float]:
    """Dynamically constructs coherent subarray with maximal sum.

    :param iterable: sequence of numbers
    :return: maximum subarray"""
    actual = [0, []]
    maximal = (0, [])

    for elem in iterable:
        if actual[0] < 0.0:
            actual = [0, []]

        actual[0] += elem
        actual[1].append(elem)

        if actual[0] > maximal[0]:
            maximal = (actual[0], actual[1][:])

    return iter(maximal[1])


def count_maximal_subsum(sequence: Sequence[float]) -> float:
    """Counts maximal sum from all coherent subarrays using interval tree.

    :param sequence: sequence of numbers
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
