# -*- coding: utf-8 -*-
"""Tests: Knuth-Morris-Pratt algorithm"""
import unittest

from assertpy import assert_that

from algolib.text import kmp


class KMPTest(unittest.TestCase):
    @staticmethod
    def test__kmp__when_pattern_found_once__then_single_occurrence():
        # when
        result = kmp("abcde", "a")
        # then
        assert_that(list(result)).is_equal_to([0])

    @staticmethod
    def test__kmp__when_pattern_found_twice__then_two_occurrences():
        # when
        result = kmp("abcdae", "a")
        # then
        assert_that(list(result)).is_equal_to([0, 4])

    @staticmethod
    def test__kmp__when_pattern_found_twice_and_intersects__then_two_occurrences():
        # when
        result = kmp("aaabcde", "aa")
        # then
        assert_that(list(result)).is_equal_to([0, 1])

    @staticmethod
    def test__kmp__when_pattern_not_found__then_empty_occurrences():
        # when
        result = kmp("abcde", "x")
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__kmp__when_pattern_is_empty_string__then_empty_occurrences():
        # when
        result = kmp("abcde", "")
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__kmp__when_text_is_empty_string__then_empty_occurrences():
        # when
        result = kmp("", "a")
        # then
        assert_that(list(result)).is_empty()
