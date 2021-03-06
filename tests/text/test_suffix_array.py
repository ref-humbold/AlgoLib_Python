# -*- coding: utf-8 -*-
"""Tests: Structure of suffix array """
import unittest

from algolib.text import SuffixArray


class SuffixArrayTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = SuffixArray("mississippi")

    def tearDown(self):
        self.test_object = None

    def test__len(self):
        result = len(self.test_object)

        self.assertEqual(11, result)

    def test__getitem(self):
        result0 = self.test_object[0]
        result1 = self.test_object[3]
        result2 = self.test_object[6]
        result3 = self.test_object[9]

        self.assertEqual("i", result0)
        self.assertEqual("ississippi", result1)
        self.assertEqual("ppi", result2)
        self.assertEqual("ssippi", result3)

    def test__getitem__when_out_of_range(self):
        with self.assertRaises(IndexError):
            _ = self.test_object[20]

    def test__index_at(self):
        result0 = self.test_object.index_at(0)
        result1 = self.test_object.index_at(3)
        result2 = self.test_object.index_at(6)
        result3 = self.test_object.index_at(9)

        self.assertEqual(10, result0)
        self.assertEqual(1, result1)
        self.assertEqual(8, result2)
        self.assertEqual(5, result3)

    def test__index_at__when_out_of_range(self):
        with self.assertRaises(IndexError):
            self.test_object.index_at(20)

    def test__index_of(self):
        result0 = self.test_object.index_of(0)
        result1 = self.test_object.index_of(3)
        result2 = self.test_object.index_of(6)
        result3 = self.test_object.index_of(9)

        self.assertEqual(4, result0)
        self.assertEqual(8, result1)
        self.assertEqual(7, result2)
        self.assertEqual(5, result3)

    def test__index_of__when_out_of_range(self):
        with self.assertRaises(IndexError):
            self.test_object.index_of(20)

    def test__lcp__when_same_suffix(self):
        result = self.test_object.lcp(4, 4)

        self.assertEqual(7, result)

    def test__lcp__when_different_suffix1(self):
        result = self.test_object.lcp(1, 10)

        self.assertEqual(1, result)

    def test__lcp__when_different_suffix2(self):
        result = self.test_object.lcp(9, 6)

        self.assertEqual(0, result)

    def test__lcp__when_swap_suffix(self):
        result0 = self.test_object.lcp(2, 5)
        result1 = self.test_object.lcp(5, 2)

        self.assertEqual(3, result0)
        self.assertEqual(result0, result1)
