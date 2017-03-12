# -*- coding: utf-8 -*-
"""ALGORYTMY WYZNACZANIA PODCIĄGU SPÓJNEGO O MAKSYMALNEJ SUMIE"""
def find_maxsum_subseq1(sequence):
    """Wyznaczanie spójnego podciągu o maksymalnej sumie w sposób dynamiczny.
    :param sequence: ciąg
    :returns: elementy spójnego podciągu o maksymalnej sumie"""
    actual_subseq = []
    max_subseq = []

    for elem in sequence:
        if sum(actual_subseq) < 0.0:
            actual_subseq = []

        actual_subseq.append(elem)

        if sum(actual_subseq) > sum(max_subseq):
            max_subseq = actual_subseq[:]

    return max_subseq


def find_maxsum_subseq2(sequence):
    """Wyznaczanie spójnego podciągu o maksymalnej sumie za pomocą drzewa parzedziałowego.
    :param sequence: ciąg
    :returns: elementy spójnego podciągu o maksymalnej sumie"""
    size = 1

    while size < 2*len(sequence):
        size <<= 1

    interval_sums = [0.0]*size
    prefix_sums = [0.0]*size
    suffix_sums = [0.0]*size
    all_sums = [0.0]*size

    for i, elem in enumerate(sequence):
        index = size//2+i
        all_sums[index] += elem
        interval_sums[index] = max(all_sums[index], 0.0)
        prefix_sums[index] = max(all_sums[index], 0.0)
        suffix_sums[index] = max(all_sums[index], 0.0)
        index >>= 1

        while index > 0:
            index_left = index+index
            index_right = index+index+1
            interval_sums[index] = max(interval_sums[index_left], interval_sums[index_right],
                                       suffix_sums[index_left]+prefix_sums[index_right])
            prefix_sums[index] = max(prefix_sums[index_left],
                                     all_sums[index_left]+prefix_sums[index_right])
            suffix_sums[index] = max(suffix_sums[index_right],
                                     suffix_sums[index_left]+all_sums[index_right])
            all_sums[index] = all_sums[index_left]+all_sums[index_right]
            index >>= 1

    return interval_sums[1]
