# -*- coding: utf-8 -*-
"""TESTY DLA ALGORYTMÓW SORTOWANIA"""
import unittest
from algolib import angle_sort, angle_sorted, heap_sort, heap_sorted, merge_sort, \
    merge_sorted, quick_sort, quick_sorted


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_angle_sorted(self):
        sequence = [(0, 0), (-2, -3), (-3, -2), (3, -2), (-2, 3), (3, 2), (2, -3), (2, 3), (-3, 2)]
        sequence_copy = sequence[:]

        result = angle_sorted(sequence)

        self.assertListEqual([(0, 0), (3, 2), (2, 3), (-2, 3), (-3, 2),
                              (-3, -2), (-2, -3), (2, -3), (3, -2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test_angle_sorted_when_argument_is_not_list(self):
        sequence = {(0, 0), (-2, -3), (-3, -2), (3, -2), (-2, 3), (3, 2), (2, -3), (2, 3), (-3, 2)}

        result = angle_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([(0, 0), (3, 2), (2, 3), (-2, 3), (-3, 2),
                              (-3, -2), (-2, -3), (2, -3), (3, -2)], result)

    def test_angle_sort(self):
        sequence = [(0, 0), (-2, -3), (-3, -2), (3, -2), (-2, 3), (3, 2), (2, -3), (2, 3), (-3, 2)]

        angle_sort(sequence)

        self.assertListEqual([(0, 0), (3, 2), (2, 3), (-2, 3), (-3, 2),
                              (-3, -2), (-2, -3), (2, -3), (3, -2)], sequence)

    def test_angle_sort_when_empty_list(self):
        sequence = []

        angle_sort(sequence)

        self.assertListEqual([], sequence)

    def test_angle_sort_when_argument_is_not_list(self):
        sequence = {(0, 0), (-2, -3), (-3, -2), (3, -2), (-2, 3), (3, 2), (2, -3), (2, 3), (-3, 2)}

        with self.assertRaises(TypeError):
            angle_sort(sequence)

    def test_heap_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = heap_sorted(sequence)

        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_heap_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_heap_sort(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        heap_sort(sequence)

        self.assertListEqual(sorted(sequence_copy), sequence)

    def test_heap_sort_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        heap_sort(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, sequence)

    def test_heap_sort_when_index_out_of_range_1(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            heap_sort(sequence, index1, index2)

    def test_heap_sort_when_index_out_of_range_2(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            heap_sort(sequence, index1, index2)

    def test_heap_sort_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        heap_sort(sequence, index1, index2)

        self.assertListEqual(sequence_copy, sequence)

    def test_heap_sort_when_empty_list(self):
        sequence = []

        heap_sort(sequence)

        self.assertListEqual([], sequence)

    def test_heap_sort_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        with self.assertRaises(TypeError):
            heap_sort(sequence)

    def test_merge_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = merge_sorted(sequence)

        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_merge_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = merge_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_merge_sort(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        merge_sort(sequence)

        self.assertListEqual(sorted(sequence_copy), sequence)

    def test_merge_sort_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        merge_sort(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, sequence)

    def test_merge_sort_when_index_out_of_range_1(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            merge_sort(sequence, index1, index2)

    def test_merge_sort_when_index_out_of_range_2(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            merge_sort(sequence, index1, index2)

    def test_merge_sort_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        merge_sort(sequence, index1, index2)

        self.assertListEqual(sequence_copy, sequence)

    def test_merge_sort_when_empty_list(self):
        sequence = []

        merge_sort(sequence)

        self.assertListEqual([], sequence)

    def test_merge_sort_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        with self.assertRaises(TypeError):
            merge_sort(sequence)

    def test_quick_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = quick_sorted(sequence)

        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_quick_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = quick_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_quick_sort(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        quick_sort(sequence)

        self.assertListEqual(sorted(sequence_copy), sequence)

    def test_quick_sort_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        quick_sort(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, sequence)

    def test_quick_sort_when_index_out_of_range_1(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            quick_sort(sequence, index1, index2)

    def test_quick_sort_when_index_out_of_range_2(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            quick_sort(sequence, index1, index2)

    def test_quick_sort_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        quick_sort(sequence, index1, index2)

        self.assertListEqual(sequence_copy, sequence)

    def test_quick_sort_when_empty_list(self):
        sequence = []

        quick_sort(sequence)

        self.assertListEqual([], sequence)

    def test_quick_sort_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        with self.assertRaises(TypeError):
            quick_sort(sequence)
