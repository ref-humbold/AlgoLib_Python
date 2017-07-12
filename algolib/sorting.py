# -*- coding: utf-8 -*-
"""ALGORYTMY SORTOWANIA"""
from math import atan2, pi
from random import randint


def angle_sort(points):
    """Mutowalne sortowanie kątowe punktów na płaszczyźnie.
    :param points: lista punktów"""
    if not isinstance(points, list):
        raise TypeError("Argument should be of type list, not {0}.".format(type(points).__name__))

    points.sort(key=lambda xy: (
        (atan2(xy[1], xy[0]) * 180.0 / pi) % 360.0, xy[0] ** 2 + xy[1] ** 2))


def angle_sorted(points):
    """Niemutowalne sortowanie kątowe punktów na płaszczyźnie.
    :param points: ciąg punktów
    :returns: lista punktów posortowana względem kąta"""
    points_copy = list(points)
    angle_sort(points_copy)

    return points_copy


def heap_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne sortowanie listy przez kopcowanie.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)
    heap_sort(sequence_list, index_begin, index_end)

    return sequence_list


def heap_sort(sequence, index_begin=0, index_end=None):
    """Mutowalne sortowanie listy przez kopcowanie.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy"""
    if not isinstance(sequence, list):
        raise TypeError("Sequence should be of type list, not {0}.".format(
            type(sequence).__name__))

    if sequence == []:
        return

    if index_end is None:
        index_end = len(sequence)

    if abs(index_begin) > len(sequence):
        raise IndexError("List beginning index out of range.")

    if abs(index_end) > len(sequence):
        raise IndexError("List ending index out of range.")

    if index_end < len(sequence):
        index_end %= len(sequence)

    index_begin %= len(sequence)
    heap_size = index_end - index_begin

    if heap_size <= 1:
        return

    for i in range(index_begin + heap_size // 2, index_begin - 1, -1):
        _move_down(sequence, i, index_begin, index_end)

    while heap_size > 1:
        index_heap = index_begin + heap_size - 1
        sequence[index_heap], sequence[index_begin] = sequence[index_begin], sequence[index_heap]
        _move_down(sequence, index_begin, index_begin, index_heap)
        heap_size -= 1


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


def merge_sorted(sequence, index_begin=0, index_end=None):
    """Niemutowalne sortowanie listy przez scalanie.
    :param seq: ciąg
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)
    merge_sort(sequence_list, index_begin, index_end)

    return sequence_list


def merge_sort(sequence, index_begin=0, index_end=None):
    """Mutowalne sortowanie listy przez scalanie.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy"""
    if not isinstance(sequence, list):
        raise TypeError("Sequence should be of type list, not {0}.".format(
            type(sequence).__name__))

    if sequence == []:
        return

    if index_end is None:
        index_end = len(sequence)

    if abs(index_begin) > len(sequence):
        raise IndexError("List beginning index out of range.")

    if abs(index_end) > len(sequence):
        raise IndexError("List ending index out of range.")

    if index_end < len(sequence):
        index_end %= len(sequence)

    index_begin %= len(sequence)

    if index_end - index_begin <= 1:
        return

    index_middle = (index_begin + index_end) // 2
    merge_sort(sequence, index_begin, index_middle)
    merge_sort(sequence, index_middle, index_end)
    _merge(sequence, index_begin, index_middle, index_end)


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
    """Niemutowalne szybkie sortowanie listy.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy
    :returns: lista posortowanych elementów"""
    sequence_list = list(sequence)
    quick_sort(sequence_list, index_begin, index_end)

    return sequence_list


def quick_sort(sequence, index_begin=0, index_end=None):
    """Mutowalne szybkie sortowanie listy.
    :param sequence: lista
    :param index_begin: początkowy indeks listy
    :param index_end: końcowy indeks listy"""
    if not isinstance(sequence, list):
        raise TypeError("Sequence should be of type list, not {0}.".format(
            type(sequence).__name__))

    if sequence == []:
        return

    if index_end is None:
        index_end = len(sequence)

    if abs(index_begin) > len(sequence):
        raise IndexError("List beginning index out of range.")

    if abs(index_end) > len(sequence):
        raise IndexError("List ending index out of range.")

    if index_end < len(sequence):
        index_end %= len(sequence)

    index_begin %= len(sequence)

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
            sequence[index_pivot], sequence[index_front] = \
                sequence[index_front], sequence[index_pivot]
            index_pivot = index_front
            index_front += 1
        else:
            sequence[index_front], sequence[index_back] = \
                sequence[index_back], sequence[index_front]
            index_back -= 1

    quick_sort(sequence, index_begin, index_pivot)
    quick_sort(sequence, index_pivot + 1, index_end)