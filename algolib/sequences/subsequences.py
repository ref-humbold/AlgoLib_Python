# -*- coding: utf-8 -*-
"""Algorithms for subsequences"""
from typing import Iterable, Iterator, List, Sequence, TypeVar

_T = TypeVar("_T")


def longest_increasing(sequence: Sequence[_T], key=lambda x: x) -> Iterator[_T]:
    """Constructs the longest increasing subsequence.

    :param sequence: a sequence of elements
    :param key: key function for elements in sequence
    :return: the longest increasing subsequence (least lexicographically)"""
    previous_elem = [None]
    subsequence = [0]

    for (i, elem) in enumerate(sequence[1:], start=1):
        if key(elem) > key(sequence[subsequence[-1]]):
            previous_elem.append(subsequence[-1])
            subsequence.append(i)
        else:
            index = _search_index(sequence, key, subsequence, 0, len(subsequence), i)
            subsequence[index] = i
            previous_elem.append(subsequence[index - 1] if index > 0 else None)

    longest_subsequence = []
    subsequence_index = subsequence[-1]

    while subsequence_index is not None:
        longest_subsequence.append(sequence[subsequence_index])
        subsequence_index = previous_elem[subsequence_index]

    return reversed(longest_subsequence)


def _search_index(sequence, key, subsequence, index_begin, index_end, index_elem):
    # Searches for place of element in list of subsequences.
    # (index_begin inclusive, index_end exclusive)
    if index_end - index_begin <= 1:
        return index_begin

    index_middle = (index_begin + index_end - 1) // 2

    if key(sequence[index_elem]) > key(sequence[subsequence[index_middle]]):
        return _search_index(sequence, key, subsequence, index_middle + 1, index_end, index_elem)

    return _search_index(sequence, key, subsequence, index_begin, index_middle + 1, index_elem)


def maximum_subarray(iterable: Iterable[float]) -> List[float]:
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

    return maximal[1]


def maximal_subsum(sequence: Sequence[float]) -> float:
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
