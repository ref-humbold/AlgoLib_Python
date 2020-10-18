# -*- coding: utf-8 -*-
"""Tests: Base words dictionary structure using Karp-Miller-Rosenberg algorithm"""
import unittest

from algolib.text import BaseWordsDict


class KMRTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = BaseWordsDict("mississippi")

    def test__getitem__when_empty_range(self):
        # when
        result = self.test_object[4, 4]
        # then
        self.assertEqual((0, 0), result)

    def test__getitem__when_single_character(self):
        # when
        result1 = self.test_object[1, 2]  # i
        result2 = self.test_object[0, 1]  # m
        result3 = self.test_object[8, 9]  # p
        result4 = self.test_object[3, 4]  # s
        # then
        self.assertEqual((1, 0), result1)
        self.assertEqual((2, 0), result2)
        self.assertEqual((3, 0), result3)
        self.assertEqual((4, 0), result4)

    def test__getitem__when_base_word(self):
        # when
        result1 = self.test_object[0, 1]  # m
        result2 = self.test_object[4, 6]  # is
        result3 = self.test_object[8, 10]  # pp
        result4 = self.test_object[7, 11]  # ippi
        result5 = self.test_object[3, 7]  # siss
        # then
        self.assertEqual((2, 0), result1)
        self.assertEqual((6, 0), result2)
        self.assertEqual((9, 0), result3)
        self.assertEqual((12, 0), result4)
        self.assertEqual((16, 0), result5)

    def test__getitem__when_composed_word(self):
        # when
        result1 = self.test_object[0, 3]  # mis
        # then
        self.assertEqual((7, 6), result1)
