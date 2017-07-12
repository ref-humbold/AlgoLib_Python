# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZAJĄCY NAJMNIEJSZY LEKSYKOGRAFICZNIE NAJDŁUŻSZY PODCIĄG ROSNĄCY"""


def find_lis(sequence):
    """Wyznaczanie najdłuższego podciągu rosnącego.
    :param sequence: ciąg wejściowy
    :returns: najdłuższy podciąg rosnący"""
    previous_elem = [None] * len(sequence)
    subseq_last = [0]

    for i, elem in enumerate(sequence[1:], start=1):
        if elem > sequence[subseq_last[-1]]:
            previous_elem[i] = subseq_last[-1]
            subseq_last.append(i)
        else:
            index = _search(sequence, subseq_last, 0, len(subseq_last) - 1, i)
            subseq_last[index] = i
            previous_elem[i] = subseq_last[index - 1] if index > 0 else None

    longest_subseq = []
    j = subseq_last[-1]

    while j is not None:
        longest_subseq.append(sequence[j])
        j = previous_elem[j]

    longest_subseq.reverse()

    return longest_subseq


def _search(sequence, subseq_last, index_begin, index_end, index_elem):
    """Wyszukiwanie miejsca dla elementu.
    :param sequence: ciąg wejściowy
    :param subseq_last: końcowe elementy podciągów
    :param index_begin: indeks początku
    :param index_end: indeks końca
    :param index_elem: indeks elementu
    :returns: indeks miejsca elementu w tablicy długości"""
    if index_begin == index_end:
        return index_begin

    index_middle = (index_begin + index_end) // 2

    if sequence[index_elem] > sequence[subseq_last[index_middle]]:
        return _search(sequence, subseq_last, index_middle + 1, index_end, index_elem)
    else:
        return _search(sequence, subseq_last, index_begin, index_middle, index_elem)