# -*- coding: utf-8 -*-
"""TESTS FOR MAXIMUM SUBARRAY ALGORITHMS"""
import unittest
from algolib import find_maximum_subarray, find_maximal_sum


class MaximumSubarrayTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__sequence = None

    def setUp(self):
        pass

    def tearDown(self):
        self.__sequence = None

    def test_find_maximum_subarray1(self):
        self.__sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]

        result = find_maximum_subarray(self.__sequence)

        self.assertListEqual([3.5, 4.8, -1.6, 7.7, 2.1], result)

    def test_find_maximum_subarray2(self):
        self.__sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]

        result = find_maximum_subarray(self.__sequence)

        self.assertListEqual([7.7, 2.1, 0.8, 4.0], result)

    def test_find_maximum_subarray_when_all_elements_are_negative(self):
        self.__sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]

        result = find_maximum_subarray(self.__sequence)

        self.assertListEqual([], result)

    def test_find_maximumal_sum1(self):
        self.__sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]

        result = find_maximal_sum(self.__sequence)

        self.assertAlmostEqual(16.5, result, delta=0.000001)

    def test_find_maximumal_sum2(self):
        self.__sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]

        result = find_maximal_sum(self.__sequence)

        self.assertAlmostEqual(14.6, result, delta=0.000001)

    def test_find_maximumal_sum_when_all_elements_are_negative(self):
        self.__sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]

        result = find_maximal_sum(self.__sequence)

        self.assertAlmostEqual(0.0, result, delta=0.0)
