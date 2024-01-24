# -*- coding: utf-8 -*-
"""Tests: Structure of suffix array."""
import unittest

from assertpy import assert_that

from algolib.text import SuffixArray


class SuffixArrayTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = SuffixArray("mississippi")

    def test__op_len(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(11)

    def test__op_getitem(self):
        # when
        result0 = self.test_object[0]
        result1 = self.test_object[3]
        result2 = self.test_object[6]
        result3 = self.test_object[9]
        # then
        assert_that(result0).is_equal_to("i")
        assert_that(result1).is_equal_to("ississippi")
        assert_that(result2).is_equal_to("ppi")
        assert_that(result3).is_equal_to("ssippi")

    def test__op_getitem__when_out_of_range(self):
        # when
        def function(i):
            return self.test_object[i]

        # then
        assert_that(function).raises(IndexError).when_called_with(20)

    def test__index_at(self):
        # when
        result0 = self.test_object.index_at(0)
        result1 = self.test_object.index_at(3)
        result2 = self.test_object.index_at(6)
        result3 = self.test_object.index_at(9)
        # then
        assert_that(result0).is_equal_to(10)
        assert_that(result1).is_equal_to(1)
        assert_that(result2).is_equal_to(8)
        assert_that(result3).is_equal_to(5)

    def test__index_at__when_out_of_range(self):
        # when
        function = self.test_object.index_at
        # then
        assert_that(function).raises(IndexError).when_called_with(20)

    def test__index_of(self):
        # when
        result0 = self.test_object.index_of(0)
        result1 = self.test_object.index_of(3)
        result2 = self.test_object.index_of(6)
        result3 = self.test_object.index_of(9)
        # then
        assert_that(result0).is_equal_to(4)
        assert_that(result1).is_equal_to(8)
        assert_that(result2).is_equal_to(7)
        assert_that(result3).is_equal_to(5)

    def test__index_of__when_out_of_range(self):
        # when
        function = self.test_object.index_of
        # then
        assert_that(function).raises(IndexError).when_called_with(20)

    def test__lcp__when_same_suffix(self):
        # when
        result = self.test_object.lcp(4, 4)
        # then
        assert_that(result).is_equal_to(7)

    def test__lcp__when_different_suffix1(self):
        # when
        result = self.test_object.lcp(1, 10)
        # then
        assert_that(result).is_equal_to(1)

    def test__lcp__when_different_suffix2(self):
        # when
        result = self.test_object.lcp(9, 6)
        # then
        assert_that(result).is_equal_to(0)

    def test__lcp__when_swap_suffix(self):
        # when
        result0 = self.test_object.lcp(2, 5)
        result1 = self.test_object.lcp(5, 2)
        # then
        assert_that(result0).is_equal_to(3)
        assert_that(result1).is_equal_to(result0)
