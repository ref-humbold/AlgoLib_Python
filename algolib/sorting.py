# -*- coding: utf-8 -*-
"""Sorting algorithms."""
from random import randint

from math import atan2, pi


def angle_sorted(points):
    """Immutable soting of 2D points by angle
    :param points: sequence of points
    :returns: list of points sorted by angle"""
    points_list = list(points)

    points_list.sort(
        key=lambda xy: ((atan2(xy[1], xy[0]) * 180.0 / pi) % 360.0, xy[0] ** 2 + xy[1] ** 2))

    return points_list


def heap_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne sortowanie ciągu przez kopcowanie.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    if index_end is None:
        index_end = len(sequence_list)

    if abs(index_begin) > len(sequence_list):
        raise IndexError("List beginning index out of range.")

    if abs(index_end) > len(sequence_list):
        raise IndexError("List ending index out of range.")

    if index_end < len(sequence_list):
        index_end %= len(sequence_list)

    index_begin %= len(sequence_list)
    heap_size = index_end - index_begin

    for i in range(index_begin + heap_size // 2, index_begin - 1, -1):
        _move_down(sequence_list, i, index_begin, index_end)

    while heap_size > 1:
        index_heap = index_begin + heap_size - 1
        sequence_list[index_heap], sequence_list[index_begin] = sequence_list[index_begin], \
                                                                sequence_list[index_heap]
        _move_down(sequence_list, index_begin, index_begin, index_heap)
        heap_size -= 1

    return sequence_list


def _move_down(heap, vertex, index_begin, index_end):
    """Przywracanie własności kopca.
    :param heap: kopiec
    :param vertex: wierzchołek kopca
    :param index_begin: początkowy indeks kopca
    :param index_end: końcowy indeks kopca"""
    next_vertex = None
    left_vertex = vertex + vertex - index_begin + 1
    right_vertex = vertex + vertex - index_begin + 2

    if right_vertex < index_end:
        next_vertex = left_vertex if heap[right_vertex] < heap[left_vertex] else right_vertex

    if left_vertex == index_end - 1:
        next_vertex = left_vertex

    if next_vertex is None:
        return

    if heap[next_vertex] > heap[vertex]:
        heap[next_vertex], heap[vertex] = heap[vertex], heap[next_vertex]

    _move_down(heap, next_vertex, index_begin, index_end)


def mergedown_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne sortowanie ciągu przez scalanie top-down.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    if index_end is None:
        index_end = len(sequence_list)

    if abs(index_begin) > len(sequence_list):
        raise IndexError("Sequence beginning index out of range.")

    if abs(index_end) > len(sequence_list):
        raise IndexError("Sequence ending index out of range.")

    if index_end < len(sequence_list):
        index_end %= len(sequence_list)

    index_begin %= len(sequence_list)

    _merge_sort(sequence_list, index_begin, index_end)

    return sequence_list


def _merge_sort(sequence, index_begin, index_end):
    """Mutowalne sortowanie listy przez scalanie top-down.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy"""
    if index_end - index_begin <= 1:
        return

    index_middle = (index_begin + index_end) // 2
    _merge_sort(sequence, index_begin, index_middle)
    _merge_sort(sequence, index_middle, index_end)
    _merge(sequence, index_begin, index_middle, index_end)


def mergeup_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne sortowanie listy przez scalanie bottom-up.
    :param seq: ciąg
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    if index_end is None:
        index_end = len(sequence_list)

    if abs(index_begin) > len(sequence_list):
        raise IndexError("Sequence beginning index out of range.")

    if abs(index_end) > len(sequence_list):
        raise IndexError("Sequence ending index out of range.")

    if index_end < len(sequence_list):
        index_end %= len(sequence_list)

    index_begin %= len(sequence_list)

    i = 2

    while i < 2 * (index_end - index_begin):
        for j in range(index_begin, index_end, i):
            _merge(sequence_list, j, min(j + i // 2, index_end), min(j + i, index_end))

        i *= 2

    return sequence_list


def _merge(sequence, index_begin, index_middle, index_end):
    """Scalanie dwóch uporządkowanych fragmentów listy.
    :param sequence: lista
    :param index_begin: początek fragmentu
    :param index_middle: środek fragmentu
    :param index_end: koniec fragmentu"""
    ordered = []
    iter1 = index_begin
    iter2 = index_middle

    while iter1 < index_middle and iter2 < index_end:
        if sequence[iter1] < sequence[iter2]:
            ordered.append(sequence[iter1])
            iter1 += 1
        else:
            ordered.append(sequence[iter2])
            iter2 += 1

    ordered += sequence[iter1:index_middle]
    ordered += sequence[iter2:index_end]
    sequence[index_begin:index_begin + len(ordered)] = ordered


def quick_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne szybkie sortowanie ciągu.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    if index_end is None:
        index_end = len(sequence_list)

    if abs(index_begin) > len(sequence_list):
        raise IndexError("List beginning index out of range.")

    if abs(index_end) > len(sequence_list):
        raise IndexError("List ending index out of range.")

    if index_end < len(sequence_list):
        index_end %= len(sequence_list)

    index_begin %= len(sequence_list)

    _quick_sort(sequence_list, index_begin, index_end)

    return sequence_list


def _quick_sort(sequence, index_begin, index_end):
    """Mutowalne szybkie sortowanie listy.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy"""
    if index_end - index_begin <= 1:
        return

    index_pivot = index_begin
    index_front = index_begin + 1
    index_back = index_end - 1
    rdpv = sorted([randint(index_begin, index_end - 1), randint(index_begin, index_end - 1),
                   randint(index_begin, index_end - 1)])[1]
    sequence[index_pivot], sequence[rdpv] = sequence[rdpv], sequence[index_pivot]

    while index_pivot < index_back:
        if sequence[index_front] < sequence[index_pivot]:
            sequence[index_pivot], sequence[index_front] = sequence[index_front], sequence[
                index_pivot]
            index_pivot = index_front
            index_front += 1
        else:
            sequence[index_front], sequence[index_back] = sequence[index_back], sequence[
                index_front]
            index_back -= 1

    _quick_sort(sequence, index_begin, index_pivot)
    _quick_sort(sequence, index_pivot + 1, index_end)
