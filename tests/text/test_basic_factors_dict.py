# -*- coding: utf-8 -*-
"""Tests: Structure of basic factors dictionary using Karp-Miller-Rosenberg algorithm."""
import unittest

from assertpy import assert_that

from algolib.text import BasicFactorsDict


class BasicFactorsDictTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None
        self.params_slice_valid = [
                [slice(1), (2, 0)], [slice(-13, 3), (7, 6)], [slice(None), (20, 21)],
                [slice(1, 2), (1, 0)], [slice(3, 4), (4, 0)], [slice(3, 7), (16, 0)],
                [slice(4, 6), (6, 0)], [slice(5, 15), (17, 12)], [slice(-4, None), (12, 0)],
                [slice(8, 9), (3, 0)], [slice(8, -1), (9, 0)]
        ]
        self.params_slice_invalid = [
                slice(4, 4), slice(-5, -5), slice(0, 0), slice(11, 11), slice(6, 2), slice(3, 0),
                slice(11, 8), slice(22, None), slice(None, -22), slice(18, 28), slice(-23, -13)
        ]
        self.params_step = [-2, 3]

    def setUp(self):
        self.test_object = BasicFactorsDict("mississippi")

    def test__op_getitem__when_slice__then_code(self):
        for slice_, expected in self.params_slice_valid:
            with self.subTest(param=slice_):
                # when
                result = self.test_object[slice_]

                # then
                assert_that(result).is_equal_to(expected)

    def test__op_getitem__when_slice_step_not_none__then_value_error(self):
        # when
        def function(i):
            return self.test_object[::i]

        for step in self.params_step:
            with self.subTest(param=step):
                # then
                assert_that(function).raises(ValueError).when_called_with(step)

    def test__op_getitem__when_invalid_slice__then_value_error(self):
        # when
        def function(s):
            return self.test_object[s]

        for slice_ in self.params_slice_invalid:
            with self.subTest(param=slice_):
                # then
                assert_that(function).raises(ValueError).when_called_with(slice_)
