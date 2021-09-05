# -*- coding: utf-8 -*-
"""Algorithms for subsequences"""
from typing import Iterable, Iterator, List, Sequence, TypeVar

_T = TypeVar("_T")


def longest_increasing(sequence: Sequence[_T], key=lambda x: x) -> Iterator[_T]:
    """Constructs longest ordered subsequence.

    :param sequence: a sequence of elements
    :param key: key function for elements in subsequence
    :return: least lexicographically longest ordered subsequence"""
    previous_elem = [None]
    subseq_last = [0]

    for (i, elem) in enumerate(sequence[1:], start=1):
        if key(elem) < key(sequence[subseq_last[-1]]):
            previous_elem.append(subseq_last[-1])
            subseq_last.append(i)
        else:
            index = _search_index(sequence, key, subseq_last, i, 0, len(subseq_last) - 1)
            subseq_last[index] = i
            previous_elem.append(subseq_last[index - 1] if index > 0 else None)

    longest_subseq = []
    j = subseq_last[-1]

    while j is not None:
        longest_subseq.append(sequence[j])
        j = previous_elem[j]

    return reversed(longest_subseq)


def _search_index(sequence, key, subseq_last, index_elem, index_begin, index_end):
    if index_begin == index_end:
        return index_begin

    index_middle = (index_begin + index_end) // 2

    if key(sequence[index_elem]) < key(sequence[subseq_last[index_middle]]):
        return _search_index(sequence, key, subseq_last, index_elem, index_middle + 1, index_end)

    return _search_index(sequence, key, subseq_last, index_elem, index_begin, index_middle)


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
