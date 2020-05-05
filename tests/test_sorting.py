# -*- coding: utf-8 -*-
"""Tests: Algorithms for sequence sorting"""
import unittest

from algolib.sequences import heap_sorted, mergedown_sorted, mergeup_sorted, quick_sorted


class SortingTest(unittest.TestCase):
    def test__heap_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test__heap_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__heap_sorted__when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = heap_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test__heap_sorted__when_empty_list(self):
        sequence = []

        result = heap_sorted(sequence)

        self.assertListEqual([], result)

    def test__mergedown_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = mergedown_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)
        self.assertListEqual(sequence_copy, sequence)

    def test__mergedown_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = mergedown_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__mergedown_sorted__when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = mergedown_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test__mergedown_sorted__when_empty_list(self):
        sequence = []

        result = mergedown_sorted(sequence)

        self.assertListEqual([], result)

    def test__mergeup_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = mergeup_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test__mergeup_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = mergeup_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__mergeup_sorted__when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = mergeup_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test__mergeup_sorted__when_empty_list(self):
        sequence = []

        result = mergeup_sorted(sequence)

        self.assertListEqual([], result)

    def test__quick_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        sequence_copy = sequence[:]

        result = quick_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence_copy), result)
        self.assertListEqual(sequence_copy, sequence)

    def test__quick_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = quick_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__quick_sorted__when_all_equal(self):
        sequence = [10, 10, 10, 10, 10, 10, 10, 10, 10]

        result = quick_sorted(sequence)

        self.assertListEqual([10, 10, 10, 10, 10, 10, 10, 10, 10], result)

    def test__quick_sorted__when_empty_list(self):
        sequence = []

        result = quick_sorted(sequence)

        self.assertListEqual([], result)
