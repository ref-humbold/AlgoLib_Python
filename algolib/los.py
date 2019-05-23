# -*- coding: utf-8 -*-
"""Longest ordered subsequence (least lexicographically)."""


def find_los(sequence, order):
    """Constructs longest ordered subsequence.
    :param sequence: sequence of elements
    :param order: order function of elements in subsequence
    :returns: least lexicographically longest ordered subsequence"""
    previous_elem = [None]
    subseq_last = [0]

    for (i, elem) in enumerate(sequence[1:], start=1):
        if order(elem, sequence[subseq_last[-1]]):
            previous_elem.append(subseq_last[-1])
            subseq_last.append(i)
        else:
            index = _search(order, sequence, subseq_last, 0, len(subseq_last) - 1, i)
            subseq_last[index] = i
            previous_elem.append(subseq_last[index - 1] if index > 0 else None)

    longest_subseq = []
    j = subseq_last[-1]

    while j is not None:
        longest_subseq.append(sequence[j])
        j = previous_elem[j]

    longest_subseq.reverse()

    return longest_subseq


def _search(order, sequence, subseq_last, index_begin, index_end, index_elem):
    """Searches for place of element in list of subsequences.
    :param order: order function of elements in subsequence
    :param sequence: input sequence
    :param subseq_last: last elements of subsequences
    :param index_begin: index of beginning
    :param index_end: index of end
    :param index_elem: index of current element
    :returns: index in list of subsequences"""
    if index_begin == index_end:
        return index_begin

    index_middle = (index_begin + index_end) // 2

    if order(sequence[index_elem], sequence[subseq_last[index_middle]]):
        return _search(order, sequence, subseq_last, index_middle + 1, index_end, index_elem)

    return _search(order, sequence, subseq_last, index_begin, index_middle, index_elem)
