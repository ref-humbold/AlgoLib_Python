# -*- coding: utf-8 -*-
"""Tests: Knuth-Morris-Pratt algorithm"""
import unittest

from algolib.text import kmp


class KMPTest(unittest.TestCase):
    def test__kmp__when_pattern_found_once__then_single_occurrence(self):
        # when
        result = kmp("abcde", "a")
        # then
        self.assertListEqual([0], list(result))

    def test__kmp__when_pattern_found_twice__then_two_occurrences(self):
        # when
        result = kmp("abcdae", "a")
        # then
        self.assertListEqual([0, 4], list(result))

    def test__kmp__when_pattern_found_twice_and_intersects__then_two_occurrences(self):
        # when
        result = kmp("aaabcde", "aa")
        # then
        self.assertListEqual([0, 1], list(result))

    def test__kmp__when_pattern_not_found__then_empty(self):
        # when
        result = kmp("abcde", "x")
        # then
        self.assertListEqual([], list(result))

    def test__kmp__when_pattern_is_empty_string__then_empty(self):
        # when
        result = kmp("abcde", "")
        # then
        self.assertListEqual([], list(result))

    def test__kmp__when_text_is_empty_string__then_empty(self):
        # when
        result = kmp("", "a")
        # then
        self.assertListEqual([], list(result))
