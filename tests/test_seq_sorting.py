# -*- coding: utf-8 -*-
"""TEST : Sequence sorting algorithms."""
import unittest

from algolib.sequences import heap_sorted, mergedown_sorted, mergeup_sorted, quick_sorted


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_heap_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_heap_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_heap_sorted_when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = heap_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test_heap_sorted_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        result = heap_sorted(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, result)

    def test_heap_sorted_when_left_index_out_of_range(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            heap_sorted(sequence, index1, index2)

    def test_heap_sorted_when_right_index_out_of_range(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            heap_sorted(sequence, index1, index2)

    def test_heap_sorted_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = heap_sorted(sequence, index1, index2)

        self.assertListEqual(sequence, result)

    def test_heap_sorted_when_empty_list(self):
        sequence = []

        result = heap_sorted(sequence)

        self.assertListEqual([], result)

    def test_mergedown_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = mergedown_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_mergedown_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = mergedown_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_mergedown_sorted_when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = mergedown_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test_mergedown_sorted_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        result = mergedown_sorted(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, result)

    def test_mergedown_sorted_when_left_index_out_of_range(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            mergedown_sorted(sequence, index1, index2)

    def test_mergedown_sorted_when_right_index_out_of_range(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            mergedown_sorted(sequence, index1, index2)

    def test_mergedown_sorted_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = mergedown_sorted(sequence, index1, index2)

        self.assertListEqual(sequence, result)

    def test_mergedown_sorted_when_empty_list(self):
        sequence = []

        result = mergedown_sorted(sequence)

        self.assertListEqual([], result)

    def test_mergeup_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = mergeup_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_mergeup_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = mergeup_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_mergeup_sorted_when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = mergeup_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test_mergeup_sorted_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        result = mergeup_sorted(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, result)

    def test_mergeup_sorted_when_left_index_out_of_range(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            mergeup_sorted(sequence, index1, index2)

    def test_mergeup_sorted_when_right_index_out_of_range(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            mergeup_sorted(sequence, index1, index2)

    def test_mergeup_sorted_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = mergeup_sorted(sequence, index1, index2)

        self.assertListEqual(sequence, result)

    def test_mergeup_sorted_when_empty_list(self):
        sequence = []

        result = mergeup_sorted(sequence)

        self.assertListEqual([], result)

    def test_quick_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = quick_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test_quick_sorted_when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = quick_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test_quick_sorted_when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = quick_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test_quick_sorted_when_indices(self):
        index1 = 3
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_sorted = sequence[:index1] + sorted(sequence[index1:index2]) + sequence[index2:]

        result = quick_sorted(sequence, index1, index2)

        self.assertListEqual(sequence_sorted, result)

    def test_quick_sorted_when_left_index_out_of_range(self):
        index1 = -13
        index2 = -2
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            quick_sorted(sequence, index1, index2)

    def test_quick_sorted_when_right_index_out_of_range(self):
        index1 = 3
        index2 = 17
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        with self.assertRaises(IndexError):
            quick_sorted(sequence, index1, index2)

    def test_quick_sorted_when_indices_reversed(self):
        index1 = 7
        index2 = 3
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = quick_sorted(sequence, index1, index2)

        self.assertListEqual(sequence_copy, result)

    def test_quick_sorted_when_empty_list(self):
        sequence = []

        result = quick_sorted(sequence)

        self.assertListEqual([], result)
