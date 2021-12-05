# -*- coding: utf-8 -*-
"""Tests: Algorithms for maximum subarray"""
import unittest

from assertpy import assert_that

from algolib.sequences import count_maximal_subsum, find_maximum_subarray


class MaximumSubarrayTest(unittest.TestCase):
    # region find_maximum_subarray

    @staticmethod
    def test__find_maximum_subarray__when_all_elements_are_positive__then_whole_sequence():
        # given
        sequence = [9.0, 2.4, 3.07, 1.93, 12.67]
        # when
        result = find_maximum_subarray(sequence)
        # then
        assert_that(list(result)).is_equal_to(sequence)

    @staticmethod
    def test__find_maximum_subarray__when_negative_less_than_subsum__then_include_negative():
        # when
        result = find_maximum_subarray([3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8])
        # then
        assert_that(list(result)).is_equal_to([3.5, 4.8, -1.6, 7.7, 2.1])

    @staticmethod
    def test__find_maximum_subarray__when_negative_greater_than_subsum__then_exclude_negative():
        # when
        result = find_maximum_subarray([-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0])
        # then
        assert_that(list(result)).is_equal_to([7.7, 2.1, 0.8, 4.0])

    @staticmethod
    def test__find_maximum_subarray__when_all_elements_are_negative__then_empty():
        # when
        result = find_maximum_subarray([-9.0, -2.4, -3.07, -1.93, -12.67])
        # then
        assert_that(list(result)).is_empty()

    # endregion
    # region count_maximum_subsum

    @staticmethod
    def test__count_maximal_subsum__when_all_elements_are_positive__then_sum_of_all():
        # when
        result = count_maximal_subsum([9.0, 2.4, 3.07, 1.93, 12.67])
        # then
        assert_that(result).is_close_to(29.07, 0.000001)

    @staticmethod
    def test__count_maximal_subsum__when_negative_less_than_subsum__then_include_negative():
        # when
        result = count_maximal_subsum([3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8])
        # then
        assert_that(result).is_close_to(16.5, 0.000001)

    @staticmethod
    def test__count_maximal_subsum__when_negative_greater_than_subsum__then_exclude_negative():
        # when
        result = count_maximal_subsum([-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0])
        # then
        assert_that(result).is_close_to(14.6, 0.000001)

    @staticmethod
    def test__count_maximal_subsum__when_all_elements_are_negative__then_zero():
        # when
        result = count_maximal_subsum([-9.0, -2.4, -3.07, -1.93, -12.67])
        # then
        assert_that(result).is_equal_to(0.0)

    # endregion
