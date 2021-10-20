# -*- coding: utf-8 -*-
"""Tests: Algorithms for subsequences"""
import unittest

from assertpy import assert_that

from algolib.sequences import maximal_subsum, maximum_subarray


class SubseqsTest(unittest.TestCase):
    # region maximum_subarray

    @staticmethod
    def test__maximum_subarray__1():
        # given
        sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]
        # when
        result = maximum_subarray(sequence)
        # then
        assert_that(result).is_equal_to([3.5, 4.8, -1.6, 7.7, 2.1])

    @staticmethod
    def test__maximum_subarray__2():
        # given
        sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]
        # when
        result = maximum_subarray(sequence)
        # then
        assert_that(result).is_equal_to([7.7, 2.1, 0.8, 4.0])

    @staticmethod
    def test__maximum_subarray__when_all_elements_are_negative():
        # given
        sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]
        # when
        result = maximum_subarray(sequence)
        # then
        assert_that(result).is_empty()

    # endregion
    # region maximum_subsum

    @staticmethod
    def test__maximal_subsum__1():
        # given
        sequence = [3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8]
        # when
        result = maximal_subsum(sequence)
        # then
        assert_that(result).is_close_to(16.5, 0.000001)

    @staticmethod
    def test__maximal_subsum__2():
        # given
        sequence = [-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0]
        # when
        result = maximal_subsum(sequence)
        # then
        assert_that(result).is_close_to(14.6, 0.000001)

    @staticmethod
    def test__maximal_subsum__when_all_elements_are_negative():
        # given
        sequence = [-9.0, -2.4, -3.07, -1.93, -12.67]
        # when
        result = maximal_subsum(sequence)
        # then
        assert_that(result).is_equal_to(0.0)

    # endregion
