# -*- coding: utf-8 -*-
"""Test: knuth-morris-pratt algorithm"""
import unittest
from algolib.text import kmp


class KMPTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kmp_when_pattern_found_once(self):
        text = "abcde"
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([0], list(result))

    def test_kmp_when_pattern_found_twice(self):
        text = "abcdae"
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([0, 4], list(result))

    def test_kmp_when_pattern_found_twice_and_intersects(self):
        text = "aaabcde"
        pattern = "aa"

        result = kmp(text, pattern)

        self.assertListEqual([0, 1], list(result))

    def test_kmp_when_pattern_not_found(self):
        text = "abcde"
        pattern = "x"

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))

    def test_kmp_when_pattern_is_empty_string(self):
        text = "abcde"
        pattern = ""

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))

    def test_kmp_when_text_is_empty_string(self):
        text = ""
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([], list(result))
