# -*- coding: utf-8 -*-
"""Algorithms for sequence sorting."""
from random import randint
from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def heap_sorted(sequence: Iterable[_T]) -> List[_T]:
    """Immutably sorts given sequence using heap.

    :param sequence: the sequence of elements
    :return: the sorted sequence"""
    sequence_list = list(sequence)

    if not sequence_list:
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


def top_down_merge_sorted(sequence: Iterable[_T]) -> List[_T]:
    """Immutably sorts given sequence using top-down merge-sort algorithm.
    Sorting is guaranteed to be stable.

    :param sequence: the sequence of elements
    :return: the sorted sequence"""
    sequence_list = list(sequence)

    if not sequence_list:
        return []

    _do_merge_sort(sequence_list, 0, len(sequence_list))
    return sequence_list


def bottom_up_merge_sorted(sequence: Iterable[_T]) -> List[_T]:
    """Immutably sorts given sequence using bottom-up merge-sort algorithm.
    Sorting is guaranteed to be stable.

    :param sequence: the sequence of elements
    :return: the sorted sequence"""
    sequence_list = list(sequence)

    if not sequence_list:
        return []

    half_step = 1

    while half_step < len(sequence_list):
        for i in range(0, len(sequence_list), half_step + half_step):
            index_middle = min(i + half_step, len(sequence_list))
            index_end = min(i + half_step + half_step, len(sequence_list))
            _merge(sequence_list, i, index_middle, index_end)

        half_step *= 2

    return sequence_list


def quick_sorted(sequence: Iterable[_T]) -> List[_T]:
    """Immutably sorts given sequence using quick-sort algorithm.

    :param sequence: the sequence of elements
    :return: the sorted sequence"""
    sequence_list = list(sequence)

    if not sequence_list:
        return []

    _do_quick_sort(sequence_list, 0, len(sequence_list))
    return sequence_list


def _move_down(heap, vertex, index_begin, index_end):
    # Move element down inside given heap.
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


def _do_merge_sort(sequence, index_begin, index_end):
    # Mutably sorts given sequence using recursive merge-sort algorithm.
    if index_end - index_begin <= 1:
        return

    index_middle = (index_begin + index_end) // 2
    _do_merge_sort(sequence, index_begin, index_middle)
    _do_merge_sort(sequence, index_middle, index_end)
    _merge(sequence, index_begin, index_middle, index_end)


def _merge(sequence, index_begin, index_middle, index_end):
    # Merges two sorted fragments of given sequence. Guaranteed to be stable.
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


def _do_quick_sort(sequence, index_begin, index_end):
    # Mutably sorts given sequence using quick-sort algorithm.
    if index_end - index_begin <= 1:
        return

    index_pivot = _choose_pivot(index_begin, index_end)
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

    _do_quick_sort(sequence, index_begin, index_pivot)
    _do_quick_sort(sequence, index_pivot + 1, index_end)


def _choose_pivot(index_begin, index_end):
    # Randomly chooses pivot for quick-sort algorithm.
    return sorted([
        randint(index_begin, index_end - 1),
        randint(index_begin, index_end - 1),
        randint(index_begin, index_end - 1)
    ])[1]
