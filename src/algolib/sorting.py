# -*- coding: utf-8 -*-
"""ALGORYTMY SORTOWANIA"""
from math import atan2, pi
from random import randint

def angle_sort(points):
    """Mutowalne sortowanie kątowe punktów na płaszczyźnie.
    :param points: lista punktów"""
    polar = lambda xy: ((atan2(xy[1], xy[0])*180/pi)%360, xy[0]**2+xy[1]**2)
    points.sort(key=polar)


def angle_sorted(points):
    """Niemutowalne sortowanie kątowe punktów na płaszczyźnie.
    :param points: lista punktów
    :returns: lista punktów posortowana względem kąta"""
    polar = lambda xy: ((atan2(xy[1], xy[0])*180/pi)%360, xy[0]**2+xy[1]**2)

    return sorted(points, key=polar)


def heap_sorted(sequence, index_begin=0, index_end=-1):
    """Niemutowalne sortowanie ciągu przez kopcowanie.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu"""
    sequence_copy = sequence[:]
    heap_sort(sequence_copy, index_begin, index_end)

    return sequence_copy


def heap_sort(sequence, index_begin=0, index_end=-1):
    """Mutowalne sortowanie ciągu przez kopcowanie.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu"""
    index_begin %= len(sequence)
    index_end %= len(sequence)
    heap_size = index_end-index_begin

    for i in range(index_begin+heap_size//2, index_begin-1, -1):
        move_down(sequence, i, index_begin, index_end)

    while heap_size > 1:
        index_heap = index_begin+heap_size
        sequence[index_heap], sequence[index_begin] = sequence[index_begin], sequence[index_heap]
        move_down(sequence, index_begin, index_begin, index_heap-1)


def move_down(heap, vertex, index_begin, index_end):
    """Przywracanie własności kopca.
    :param heap: kopiec
    :param vertex: wierzchołek kopca
    :param index_begin: początkowy indeks kopca
    :param index_end: końcowy indeks kopca"""
    next_vertex = None
    left_vertex = vertex+vertex-index_begin+1
    right_vertex = vertex+vertex-index_begin+2

    if right_vertex <= index_end:
        next_vertex = left_vertex if heap[right_vertex] < heap[left_vertex] else right_vertex

    if left_vertex == index_end:
        next_vertex = left_vertex

    if next_vertex is not None:
        if heap[next_vertex] > heap[vertex]:
            heap[next_vertex], heap[vertex] = heap[vertex], heap[next_vertex]

        move_down(heap, next_vertex, index_begin, index_end)


def merge_sorted(sequence, index_begin=0, index_end=-1):
    """Niemutowalne sortowanie ciągu przez scalanie.
    :param seq: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu"""
    sequence_copy = sequence[:]
    merge_sort(sequence_copy, index_begin, index_end)

    return sequence_copy


def merge_sort(sequence, index_begin=0, index_end=-1):
    """Mutowalne sortowanie ciągu przez scalanie.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu"""
    index_begin %= len(sequence)
    index_end %= len(sequence)

    if index_begin < index_end:
        index_middle = (index_begin+index_end)//2
        merge_sort(sequence, index_begin, index_middle)
        merge_sort(sequence, index_middle+1, index_end)
        merge(sequence, index_begin, index_middle, index_end)


def merge(sequence, index_begin, index_middle, index_end):
    """Scalanie dwóch uporządkowanych fragmentów ciągu.
    :param sequence: ciąg
    :param index_begin: początek fragmentu
    :param index_middle: środek fragmentu
    :param index_end: koniec fragmentu"""
    ordered = []
    iter1 = index_begin
    iter2 = index_middle+1

    while iter1 <= index_middle and iter2 <= index_end:
        if sequence[iter1] < sequence[iter2]:
            ordered.append(sequence[iter1])
            iter1 += 1
        else:
            ordered.append(sequence[iter2])
            iter2 += 1

    if iter1 <= index_middle:
        ordered += sequence[iter1:index_middle+1]

    if iter2 <= index_end:
        ordered += sequence[iter2:index_end+1]

    sequence[index_begin:index_begin+len(ordered)] = ordered


def quick_sorted(sequence, index_begin=0, index_end=-1):
    """Niemutowalne szybkie sortowanie ciągu.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu
    :returns: posortowany ciąg"""
    sequence_copy = sequence[:]
    quick_sort(sequence_copy, index_begin, index_end)

    return sequence_copy


def quick_sort(sequence, index_begin=0, index_end=-1):
    """Mutowalne szybkie sortowanie ciągu.
    :param sequence: ciąg
    :param index_begin: początkowy indeks ciągu
    :param index_end: końcowy indeks ciągu"""
    index_begin %= len(sequence)
    index_end %= len(sequence)
    get_pivot = lambda i, j: sorted([randint(i, j), randint(i, j), randint(i, j)])[1]

    if index_begin < index_end:
        index_pivot = index_begin
        index_front = index_begin+1
        index_back = index_end
        rdpv = get_pivot(index_begin, index_end)
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

        quick_sort(sequence, index_begin, index_pivot-1)
        quick_sort(sequence, index_pivot+1, index_end)
