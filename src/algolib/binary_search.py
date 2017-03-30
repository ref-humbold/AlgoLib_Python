# -*- coding:utf-8 -*-
"""ALGORYTM BINARY SEARCH: ZNAJDOWANIE ELEMENTU W UPORZĄDKOWANYM CIĄGU"""
def binary_search(sequence, element, index_begin=0, index_end=-1):
    """Wyszukiwanie elementu w ciągu.
    :param sequence: posortowany ciąg
    :param element: poszukiwany element
    :param index_begin: indeks początku ciągu
    :param index_end: indeks końca ciągu
    :returns: czy element znajduje się w ciągu"""
    index_begin = index_begin % len(sequence)
    index_end = index_end % len(sequence)

    if index_begin > index_end:
        return False

    index_middle = (index_begin + index_end) // 2

    if sequence[index_middle] == element:
        return True
    elif sequence[index_middle] < element:
        return binary_search(sequence, element, index_middle + 1, index_end)
    else:
        return binary_search(sequence, element, index_begin, index_middle - 1)
