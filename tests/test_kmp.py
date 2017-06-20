# -*- coding: utf-8 -*-
"""TESTY DLA ALGORYTMU KNUTHA-MORRISA-PRATTA"""
import unittest
from algolib import kmp


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

        self.assertListEqual([0], result)

    def test_kmp_when_pattern_found_twice(self):
        text = "abcdae"
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([0, 4], result)

    def test_kmp_when_pattern_found_twice_and_intersects(self):
        text = "aaabcde"
        pattern = "aa"

        result = kmp(text, pattern)

        self.assertListEqual([0, 1], result)

    def test_kmp_when_pattern_not_found(self):
        text = "abcde"
        pattern = "x"

        result = kmp(text, pattern)

        self.assertListEqual([], result)

    def test_kmp_when_pattern_is_empty_string(self):
        text = "abcde"
        pattern = ""

        result = kmp(text, pattern)

        self.assertListEqual([], result)

    def test_kmp_when_pattern_is_none(self):
        text = "abcde"
        pattern = None

        with self.assertRaises(TypeError):
            kmp(text, pattern)

    def test_kmp_when_pattern_is_not_a_string(self):
        text = "abcde"
        pattern = 10

        with self.assertRaises(TypeError):
            kmp(text, pattern)

    def test_kmp_when_text_is_empty_string(self):
        text = ""
        pattern = "a"

        result = kmp(text, pattern)

        self.assertListEqual([], result)

    def test_kmp_when_text_is_none(self):
        text = None
        pattern = "a"

        with self.assertRaises(TypeError):
            kmp(text, pattern)

    def test_kmp_when_text_is_not_a_string(self):
        text = 10
        pattern = "a"

        with self.assertRaises(TypeError):
            kmp(text, pattern)
