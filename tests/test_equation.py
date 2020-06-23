# -*- coding: utf-8 -*-
"""Tests: Structure of linear equations system """
import unittest

from algolib.mathmat import Equation


class EquationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = Equation([2, 3, 0, -2], 15)

    def tearDown(self):
        self._test_object = None

    def test__str(self):
        # when
        result = str(self._test_object)
        # then
        self.assertEqual("2 x_0 + 3 x_1 + -2 x_3 = 15", result)

    def test__imul__when_constant_is_non_zero__then_multiplied(self):
        # when
        self._test_object *= 2
        # then
        self.assertListEqual([4, 6, 0, -4], self._test_object.coefficients)
        self.assertEqual(30, self._test_object.free)

    def test__imul__when_constant_is_zero__then_value_error(self):
        # when - then
        with self.assertRaises(ValueError):
            self._test_object *= 0

    def test__combine__when_constant_is_non_zero__then_combined(self):
        # when
        self._test_object.combine(Equation([1, -1, 4, 10], 5), -2)
        # then
        self.assertListEqual([0, 5, -8, -22], self._test_object.coefficients)
        self.assertEqual(5, self._test_object.free)

    def test__combine__when_constant_is_zero__then_value_error(self):
        # when - then
        with self.assertRaises(ValueError):
            self._test_object.combine(Equation([1, -1, 10, 7], 5), 0)
