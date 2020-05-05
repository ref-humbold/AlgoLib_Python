# -*- coding: utf-8 -*-
"""Tests: Knuth-Morris-Pratt algorithm"""
import unittest

from algolib.text import kmp


class KMPTest(unittest.TestCase):
    def test__kmp__when_pattern_found_once__then_single_occurrence(self):
        text = "abcde"
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([0], list(result))

    def test__kmp__when_pattern_found_twice__then_two_occurrences(self):
        text = "abcdae"
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([0, 4], list(result))

    def test__kmp__when_pattern_found_twice_and_intersects__then_two_occurrences(self):
        text = "aaabcde"
        pattern = "aa"

        result = kmp(text, pattern)

        self.assertListEqual([0, 1], list(result))

    def test__kmp__when_pattern_not_found__then_empty_occurrences(self):
        text = "abcde"
        pattern = "x"

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))

    def test__kmp__when_pattern_is_empty_string__then_empty_occurrences(self):
        text = "abcde"
        pattern = ""

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))

    def test__kmp__when_text_is_empty_string__then_empty_occurrences(self):
        text = ""
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))
