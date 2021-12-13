# -*- coding: utf-8 -*-
"""Tests: Knuth-Morris-Pratt algorithm for pattern searching"""
import unittest

from assertpy import assert_that

from algolib.text import kmp_search


class KnuthMorrisPrattTest(unittest.TestCase):
    @staticmethod
    def test__kmp_search__when_pattern_found_once__then_single_occurrence():
        # when
        result = kmp_search("abcde", "a")
        # then
        assert_that(list(result)).is_equal_to([0])

    @staticmethod
    def test__kmp_search__when_pattern_found_twice__then_two_occurrences():
        # when
        result = kmp_search("abcdae", "a")
        # then
        assert_that(list(result)).is_equal_to([0, 4])

    @staticmethod
    def test__kmp_search__when_pattern_found_twice_and_intersects__then_two_occurrences():
        # when
        result = kmp_search("aaabcde", "aa")
        # then
        assert_that(list(result)).is_equal_to([0, 1])

    @staticmethod
    def test__kmp_search__when_pattern_not_found__then_empty_occurrences():
        # when
        result = kmp_search("abcde", "x")
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__kmp_search__when_pattern_is_empty_string__then_empty_occurrences():
        # when
        result = kmp_search("abcde", "")
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__kmp_search__when_text_is_empty_string__then_empty_occurrences():
        # when
        result = kmp_search("", "a")
        # then
        assert_that(list(result)).is_empty()
