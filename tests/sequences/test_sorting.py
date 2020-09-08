# -*- coding: utf-8 -*-
"""Tests: Algorithms for sequence sorting"""
import unittest

from algolib.sequences import bottom_up_merge_sorted, heap_sorted, quick_sorted, \
    top_down_merge_sorted


class SortingTest(unittest.TestCase):
    def test__heap_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual(sorted(sequence), result)

    def test__heap_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = heap_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__top_down_merge_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = top_down_merge_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual(sorted(sequence), result)

    def test__top_down_merge_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = top_down_merge_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

    def test__bottom_up_merge_sorted(self):
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]

        result = bottom_up_merge_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual(sorted(sequence), result)

    def test__bottom_up_merge_sorted__when_argument_is_not_list(self):
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}

        result = bottom_up_merge_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(sorted(sequence), result)

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
