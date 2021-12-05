# -*- coding: utf-8 -*-
"""Algorithm for longest increasing subsequence"""
from typing import Iterable, Sequence, TypeVar

_T = TypeVar("_T")


def find_lis(sequence: Sequence[_T], key=lambda x: x) -> Iterable[_T]:
    """Constructs the longest increasing subsequence.

    :param sequence: sequence of elements
    :param key: key function for elements in sequence
    :return: the longest increasing subsequence (least lexicographically)"""
    previous_elem = [None]
    subsequence = [0]

    for (i, elem) in enumerate(sequence[1:], start=1):
        if key(elem) > key(sequence[subsequence[-1]]):
            previous_elem.append(subsequence[-1])
            subsequence.append(i)
        else:
            index = _search_index(sequence, key, subsequence, i, 0, len(subsequence))
            subsequence[index] = i
            previous_elem.append(subsequence[index - 1] if index > 0 else None)

    longest_subsequence = []
    subsequence_index = subsequence[-1]

    while subsequence_index is not None:
        longest_subsequence.append(sequence[subsequence_index])
        subsequence_index = previous_elem[subsequence_index]

    return reversed(longest_subsequence)


def _search_index(sequence, key, subsequence, index_elem, index_begin, index_end):
    # Searches for index of element in list of subsequences.
    # (index_begin inclusive, index_end exclusive)
    if index_end - index_begin <= 1:
        return index_begin

    index_middle = (index_begin + index_end - 1) // 2

    return _search_index(sequence, key, subsequence, index_elem, index_middle + 1, index_end) \
        if key(sequence[index_elem]) > key(sequence[subsequence[index_middle]]) else \
        _search_index(sequence, key, subsequence, index_elem, index_begin, index_middle + 1)
