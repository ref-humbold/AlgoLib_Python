# -*- coding: utf-8 -*-
"""Tests: Structure of base words dictionary using Karp-Miller-Rosenberg algorithm."""
import unittest

from assertpy import assert_that

from algolib.text import BaseWordsDict


class BaseWordsDictTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = BaseWordsDict("mississippi")

    def test__op_getitem__when_empty_range__then_zero_and_zero(self):
        # when
        result = self.test_object[4:4]
        # then
        assert_that(result).is_equal_to((0, 0))

    def test__op_getitem__when_start_greater_than_end__then_zero_and_zero(self):
        # when
        result = self.test_object[6:2]
        # then
        assert_that(result).is_equal_to((0, 0))

    def test__op_getitem__when_single_character__then_code_and_zero(self):
        # when
        result1 = self.test_object[1:2]  # i
        result2 = self.test_object[-11:-10]  # m
        result3 = self.test_object[8:9]  # p
        result4 = self.test_object[3:4]  # s
        # then
        assert_that(result1).is_equal_to((1, 0))
        assert_that(result2).is_equal_to((2, 0))
        assert_that(result3).is_equal_to((3, 0))
        assert_that(result4).is_equal_to((4, 0))

    def test__op_getitem__when_base_word__then_code_and_zero(self):
        # when
        result1 = self.test_object[:1]  # m
        result2 = self.test_object[4:6]  # is
        result3 = self.test_object[8:-1]  # pp
        result4 = self.test_object[7:]  # ippi
        result5 = self.test_object[3:7]  # siss
        # then
        assert_that(result1).is_equal_to((2, 0))
        assert_that(result2).is_equal_to((6, 0))
        assert_that(result3).is_equal_to((9, 0))
        assert_that(result4).is_equal_to((12, 0))
        assert_that(result5).is_equal_to((16, 0))

    def test__op_getitem__when_composed_word__then_code_and_code(self):
        # when
        result1 = self.test_object[0:3]  # mis
        result2 = self.test_object[:]  # mississippi
        # then
        assert_that(result1).is_equal_to((7, 6))
        assert_that(result2).is_equal_to((20, 21))

    def test__op_getitem__when_slice_has_step__then_index_error(self):
        # when
        def function(i):
            return self.test_object[::i]

        # then
        assert_that(function).raises(IndexError).when_called_with(-2)
