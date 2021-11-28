# -*- coding: utf-8 -*-
"""Tests: Algorithms for subsequences"""
import unittest

from assertpy import assert_that

from algolib.sequences import longest_increasing, maximal_subsum, maximum_subarray


class SubseqsTest(unittest.TestCase):
    # region longest_increasing

    @staticmethod
    def test__longest_increasing__when_increasing__then_all_elements():
        # given
        sequence = [1, 3, 5, 7, 9, 11, 13, 15]
        # when
        result = longest_increasing(sequence)
        # then
        assert_that(list(result)).is_equal_to(sequence)

    @staticmethod
    def test__longest_increasing__when_decreasing__then_last_element_only():
        # given
        sequence = [12, 10, 8, 6, 4, 2]
        # when
        result = longest_increasing(sequence)
        # then
        assert_that(list(result)).is_equal_to([2])

    @staticmethod
    def test__longest_increasing__when_multiple_subsequences__then_least_lexicographically():
        # given
        sequence = [2, 1, 4, 3, 6, 5, 8, 7, 10]
        # when
        result = longest_increasing(sequence)
        # then
        assert_that(list(result)).is_equal_to([1, 3, 5, 7, 10])

    @staticmethod
    def test__longest_increasing__when_increasing_and_reversed_comparator__then_last_element_only():
        # given
        sequence = [1, 3, 5, 7, 9, 11, 13, 15]
        # when
        result = longest_increasing(sequence, key=lambda x: -x)
        # then
        assert_that(list(result)).is_equal_to([15])

    @staticmethod
    def test__longest_increasing__when_decreasing_and_reversed_comparator__then_all_elements():
        # given
        sequence = [12, 10, 8, 6, 4, 2]
        # when
        result = longest_increasing(sequence, key=lambda x: -x)
        # then
        assert_that(list(result)).is_equal_to(sequence)

    # endregion
    # region maximum_subarray

    @staticmethod
    def test__maximum_subarray__when_all_elements_are_positive__then_whole_sequence():
        # given
        sequence = [9.0, 2.4, 3.07, 1.93, 12.67]
        # when
        result = maximum_subarray(sequence)
        # then
        assert_that(list(result)).is_equal_to(sequence)

    @staticmethod
    def test__maximum_subarray__when_negative_less_than_subsum__then_include_negative():
        # when
        result = maximum_subarray([3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8])
        # then
        assert_that(list(result)).is_equal_to([3.5, 4.8, -1.6, 7.7, 2.1])

    @staticmethod
    def test__maximum_subarray__when_negative_greater_than_subsum__then_exclude_negative():
        # when
        result = maximum_subarray([-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0])
        # then
        assert_that(list(result)).is_equal_to([7.7, 2.1, 0.8, 4.0])

    @staticmethod
    def test__maximum_subarray__when_all_elements_are_negative__then_empty():
        # when
        result = maximum_subarray([-9.0, -2.4, -3.07, -1.93, -12.67])
        # then
        assert_that(list(result)).is_empty()

    # endregion
    # region maximum_subsum

    @staticmethod
    def test__maximal_subsum__when_all_elements_are_positive__then_sum_of_all():
        # when
        result = maximal_subsum([9.0, 2.4, 3.07, 1.93, 12.67])
        # then
        assert_that(result).is_close_to(29.07, 0.000001)

    @staticmethod
    def test__maximal_subsum__when_negative_less_than_subsum__then_include_negative():
        # when
        result = maximal_subsum([3.5, 4.8, -1.6, 7.7, 2.1, -9.3, 0.8])
        # then
        assert_that(result).is_close_to(16.5, 0.000001)

    @staticmethod
    def test__maximal_subsum__when_negative_greater_than_subsum__then_exclude_negative():
        # when
        result = maximal_subsum([-9.3, -1.2, 3.5, 4.8, -10.6, 7.7, 2.1, 0.8, 4.0])
        # then
        assert_that(result).is_close_to(14.6, 0.000001)

    @staticmethod
    def test__maximal_subsum__when_all_elements_are_negative__then_zero():
        # when
        result = maximal_subsum([-9.0, -2.4, -3.07, -1.93, -12.67])
        # then
        assert_that(result).is_equal_to(0.0)

    # endregion
