# -*- coding: utf-8 -*-
"""Sequence sorting algorithms"""
from random import randint


def heap_sorted(sequence):
    """Immutably sorts specified sequence using a heap.

    :param sequence: a sequence of elements
    :return: list of sorted elements"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    index_begin = 0
    index_end = len(sequence_list)
    heap_size = index_end - index_begin

    for i in range(index_begin + heap_size // 2, index_begin - 1, -1):
        _move_down(sequence_list, i, index_begin, index_end)

    while heap_size > 1:
        index_heap = index_begin + heap_size - 1
        sequence_list[index_heap], sequence_list[index_begin] = \
            sequence_list[index_begin], sequence_list[index_heap]
        _move_down(sequence_list, index_begin, index_begin, index_heap)
        heap_size -= 1

    return sequence_list


def _move_down(heap, vertex, index_begin, index_end):
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


def mergedown_sorted(sequence):
    """Immutably sorts specified sequence using a top-down merge-sort algorithm.

    :param sequence: a sequence of elements
    :return: list of sorted elements"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    _merge_sort(sequence_list, 0, len(sequence_list))
    return sequence_list


def _merge_sort(sequence, index_begin, index_end):
    # Mutably sorts specified sequence using a recursive merge-sort algorithm.
    if index_end - index_begin <= 1:
        return

    index_middle = (index_begin + index_end) // 2
    _merge_sort(sequence, index_begin, index_middle)
    _merge_sort(sequence, index_middle, index_end)
    _merge(sequence, index_begin, index_middle, index_end)


def mergeup_sorted(sequence):
    """Immutably sorts specified sequence using a bottom-up merge-sort algorithm.

    :param sequence: a sequence of elements
    :return: list of sorted elements"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    half_step = 1

    while half_step < len(sequence_list):
        for i in range(0, len(sequence_list), half_step + half_step):
            index_middle = min(i + half_step, len(sequence_list))
            index_end = min(i + half_step + half_step, len(sequence_list))
            _merge(sequence_list, i, index_middle, index_end)

        half_step *= 2

    return sequence_list


def _merge(sequence, index_begin, index_middle, index_end):
    # Merges two sorted fragments of a sequence.
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


def quick_sorted(sequence):
    """Immutably sorts specified sequence using a quick-sort algorithm.

    :param sequence: a sequence of elements
    :return: list of sorted elements"""
    sequence_list = list(sequence)

    if sequence_list == []:
        return []

    _quick_sort(sequence_list, 0, len(sequence_list))
    return sequence_list


def _quick_sort(sequence, index_begin, index_end):
    # Mutably sorts specified sequence using a quick-sort algorithm.
    if index_end - index_begin <= 1:
        return

    index_pivot = sorted([
            randint(index_begin, index_end - 1),
            randint(index_begin, index_end - 1),
            randint(index_begin, index_end - 1)
    ])[1]
    sequence[index_pivot], sequence[index_begin] = sequence[index_begin], sequence[index_pivot]
    index_pivot = index_begin
    index_front = index_begin + 1
    index_back = index_end - 1

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

    _quick_sort(sequence, index_begin, index_pivot)
    _quick_sort(sequence, index_pivot + 1, index_end)
