# -*- coding: utf-8 -*-
"""Tests: Algorithm for longest increasing subsequence"""
import unittest

from assertpy import assert_that

from algolib.sequences import find_lis


class LongestIncreasingSubsequenceTest(unittest.TestCase):
    @staticmethod
    def test__find_lis__when_increasing__then_all_elements():
        # given
        sequence = [1, 3, 5, 7, 9, 11, 13, 15]
        # when
        result = find_lis(sequence)
        # then
        assert_that(list(result)).is_equal_to(sequence)

    @staticmethod
    def test__find_lis__when_decreasing__then_last_element_only():
        # when
        result = find_lis([12, 10, 8, 6, 4, 2])
        # then
        assert_that(list(result)).is_equal_to([2])

    @staticmethod
    def test__find_lis__when_multiple_subsequences__then_least_lexicographically():
        # when
        result = find_lis([2, 1, 4, 3, 6, 5, 8, 7, 10])
        # then
        assert_that(list(result)).is_equal_to([1, 3, 5, 7, 10])

    @staticmethod
    def test__find_lis__when_search_in_middle__then_least_lexicographically():
        # when
        result = find_lis([0, 2, 4, 6, 8, 3, 5, 7, 8])
        # then
        assert_that(list(result)).is_equal_to([0, 2, 3, 5, 7, 8])

    @staticmethod
    def test__find_lis__when_increasing_and_reversed_comparator__then_last_element_only():
        # when
        result = find_lis([1, 3, 5, 7, 9, 11, 13, 15], key=lambda x: -x)
        # then
        assert_that(list(result)).is_equal_to([15])

    @staticmethod
    def test__find_lis__when_decreasing_and_reversed_comparator__then_all_elements():
        # given
        sequence = [12, 10, 8, 6, 4, 2]
        # when
        result = find_lis(sequence, key=lambda x: -x)
        # then
        assert_that(list(result)).is_equal_to(sequence)
