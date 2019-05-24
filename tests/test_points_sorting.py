# -*- coding: utf-8 -*-
"""TEST : Points sorting algorithms."""
import unittest

from algolib.geometry import angle_sorted, p2d, sorted_by_x, sorted_by_y


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

    def test_sorted_by_x(self):
        sequence = [p2d(0, 0), p2d(-2, -3), p2d(-3, -2), p2d(3, -2), p2d(-2, 3),
                    p2d(3, 2), p2d(2, -3), p2d(2, 3), p2d(-3, 2)]
        sequence_copy = sequence[:]

        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([p2d(-3, -2), p2d(-3, 2), p2d(-2, -3), p2d(-2, 3), p2d(0, 0),
                              p2d(2, -3), p2d(2, 3), p2d(3, -2), p2d(3, 2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test_sorted_by_y(self):
        sequence = [p2d(0, 0), p2d(-2, -3), p2d(-3, -2), p2d(3, -2), p2d(-2, 3),
                    p2d(3, 2), p2d(2, -3), p2d(2, 3), p2d(-3, 2)]
        sequence_copy = sequence[:]

        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual(
            [p2d(-2, -3), p2d(2, -3), p2d(-3, -2), p2d(3, -2), p2d(0, 0), p2d(-3, 2),
             p2d(3, 2), p2d(-2, 3), p2d(2, 3)], result)
        self.assertListEqual(sequence_copy, sequence)
