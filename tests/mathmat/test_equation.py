# -*- coding: utf-8 -*-
"""Tests: Structure of linear equation"""
import unittest

from algolib.mathmat import Equation


class EquationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = Equation([2, 3, 0, -2], 15)

    def test__op_str(self):
        # when
        result = str(self.test_object)
        # then
        self.assertEqual("2 x_0 + 3 x_1 + -2 x_3 = 15", result)

    def test__op_mul__then_multiplying_each_coefficient(self):
        # when
        result = self.test_object * 2
        # then
        self.assertListEqual([4, 6, 0, -4], result.coefficients)
        self.assertEqual(30, result.free)

    def test__op_mul__when_zero__then_value_error(self):
        # then
        with self.assertRaises(ValueError):
            # when
            _ = self.test_object * 0

    def test__op_rmul__then_multiplying_each_coefficient(self):
        # when
        result = 2 * self.test_object
        # then
        self.assertListEqual([4, 6, 0, -4], result.coefficients)
        self.assertEqual(30, result.free)

    def test__op_imul__then_multiplying_each_coefficient(self):
        # when
        self.test_object *= 2
        # then
        self.assertListEqual([4, 6, 0, -4], self.test_object.coefficients)
        self.assertEqual(30, self.test_object.free)

    def test__op_truediv__then_dividing_each_coefficient(self):
        # when
        result = self.test_object / -2
        # then
        self.assertListEqual([-1, -1.5, 0, 1], result.coefficients)
        self.assertEqual(-7.5, result.free)

    def test__op_truediv__when_zero__then_value_error(self):
        # then
        with self.assertRaises(ValueError):
            # when
            _ = self.test_object / 0

    def test__op_itruediv__then_dividing_each_coefficient(self):
        # when
        self.test_object /= -2
        # then
        self.assertListEqual([-1, -1.5, 0, 1], self.test_object.coefficients)
        self.assertEqual(-7.5, self.test_object.free)

    def test__combine__when_constant_is_non_zero__then_combined(self):
        # when
        self.test_object.combine(Equation([1, -1, 4, 10], 5), -2)
        # then
        self.assertListEqual([0, 5, -8, -22], self.test_object.coefficients)
        self.assertEqual(5, self.test_object.free)

    def test__combine__when_constant_is_zero__then_value_error(self):
        # then
        with self.assertRaises(ValueError):
            # when
            self.test_object.combine(Equation([1, -1, 10, 7], 5), 0)
