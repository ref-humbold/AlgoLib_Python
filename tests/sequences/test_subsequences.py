# -*- coding: utf-8 -*-
"""Tests: Algorithms for subsequences"""
import unittest

from algolib.sequences import maximal_subsum, maximum_subarray


class SubseqsTest(unittest.TestCase):
    def test__maximum_subarray1(self):
        sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]

        result = maximum_subarray(sequence)

        self.assertListEqual([3.5, 4.8, -1.6, 7.7, 2.1], result)

    def test__maximum_subarray2(self):
        sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]

        result = maximum_subarray(sequence)

        self.assertListEqual([7.7, 2.1, 0.8, 4.0], result)

    def test__maximum_subarray__when_all_elements_are_negative(self):
        sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]

        result = maximum_subarray(sequence)

        self.assertListEqual([], result)

    def test__maximal_subsum1(self):
        sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]

        result = maximal_subsum(sequence)

        self.assertAlmostEqual(16.5, result, delta=0.000001)

    def test__maximal_subsum2(self):
        sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]

        result = maximal_subsum(sequence)

        self.assertAlmostEqual(14.6, result, delta=0.000001)

    def test__maximal_subsum__when_all_elements_are_negative(self):
        sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]

        result = maximal_subsum(sequence)

        self.assertAlmostEqual(0.0, result, delta=0.0)
