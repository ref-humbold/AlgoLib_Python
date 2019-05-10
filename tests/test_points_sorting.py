# -*- coding: utf-8 -*-
"""Test: Sequence sorting algorithms."""
import unittest
from algolib.geometry import p2d, angle_sorted


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_angle_sorted(self):
        sequence = [p2d(0, 0), p2d(-2, -3), p2d(-3, -2), p2d(3, -2), p2d(-2, 3),
                    p2d(3, 2), p2d(2, -3), p2d(2, 3), p2d(-3, 2)]
        sequence_copy = sequence[:]

        result = angle_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([p2d(0, 0), p2d(3, 2), p2d(2, 3), p2d(-2, 3), p2d(-3, 2),
                              p2d(-3, -2), p2d(-2, -3), p2d(2, -3), p2d(3, -2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test_angle_sorted_when_argument_is_not_list(self):
        sequence = {p2d(0, 0), p2d(-2, -3), p2d(-3, -2), p2d(3, -2), p2d(-2, 3),
                    p2d(3, 2), p2d(2, -3), p2d(2, 3), p2d(-3, 2)}

        result = angle_sorted(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([p2d(0, 0), p2d(3, 2), p2d(2, 3), p2d(-2, 3), p2d(-3, 2),
                              p2d(-3, -2), p2d(-2, -3), p2d(2, -3), p2d(3, -2)], result)

    def test_angle_sorted_when_all_equal(self):
        sequence = [p2d(1, 2), p2d(1, 2), p2d(1, 2), p2d(1, 2), p2d(1, 2), p2d(1, 2), p2d(1, 2)]

        result = angle_sorted(sequence)

        self.assertListEqual([p2d(1, 2), p2d(1, 2), p2d(1, 2), p2d(1, 2),
                              p2d(1, 2), p2d(1, 2), p2d(1, 2)], result)

    def test_angle_sorted_when_empty_list(self):
        sequence = []

        result = angle_sorted(sequence)

        self.assertListEqual([], result)
