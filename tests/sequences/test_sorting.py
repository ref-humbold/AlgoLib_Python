# -*- coding: utf-8 -*-
"""Tests: Algorithms for sequence sorting."""
import unittest

from assertpy import assert_that

from algolib.sequences import bottom_up_merge_sorted, heap_sorted, quick_sorted, \
    top_down_merge_sorted


class SortingTest(unittest.TestCase):
    @staticmethod
    def test__heap_sorted():
        # given
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        # when
        result = heap_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_not_same_as(sequence)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__heap_sorted__when_argument_is_not_list():
        # given
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}
        # when
        result = heap_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__top_down_merge_sorted():
        # given
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        # when
        result = top_down_merge_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_not_same_as(sequence)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__top_down_merge_sorted__when_argument_is_not_list():
        # given
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}
        # when
        result = top_down_merge_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__bottom_up_merge_sorted():
        # given
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        # when
        result = bottom_up_merge_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_not_same_as(sequence)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__bottom_up_merge_sorted__when_argument_is_not_list():
        # given
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}
        # when
        result = bottom_up_merge_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__quick_sorted():
        # given
        sequence = [3, 17, -6, 0, 9, -12, 7, 4, 2]
        # when
        result = quick_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_not_same_as(sequence)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))

    @staticmethod
    def test__quick_sorted__when_argument_is_not_list():
        # given
        sequence = {3, 17, -6, 0, 9, -12, 7, 4, 2}
        # when
        result = quick_sorted(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(sequence))
