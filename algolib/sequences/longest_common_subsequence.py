# -*- coding: utf-8 -*-
"""Algorithm for longest common subsequence"""
from typing import Sequence, TypeVar

_T = TypeVar("_T")


def count_lcs_length(sequence1: Sequence[_T], sequence2: Sequence[_T]):
    short_seq, long_seq = \
        (sequence1, sequence2) if len(sequence1) <= len(sequence2) else (sequence2, sequence1)
    lcs = [0] * (len(short_seq) + 1)

    for element1 in long_seq:
        previous_above = lcs[0]

        for i, element2 in enumerate(short_seq):
            previous_diagonal = previous_above
            previous_above = lcs[i + 1]
            lcs[i + 1] = \
                previous_diagonal + 1 if element1 == element2 else max(previous_above, lcs[i])

    return lcs[-1]
