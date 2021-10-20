# -*- coding: utf-8 -*-
"""Tests: Structure of linear equation"""
import unittest

from assertpy import assert_that

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
        assert_that(result).is_equal_to("2 x_0 + 3 x_1 + -2 x_3 = 15")

    def test__op_mul__then_multiplying_each_coefficient(self):
        # when
        result = self.test_object * 2
        # then
        assert_that(result.coefficients).is_equal_to([4, 6, 0, -4])
        assert_that(result.free).is_equal_to(30)

    def test__op_mul__when_zero__then_arithmetic_error(self):
        # when
        def function(constant):
            return self.test_object * constant

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(0)

    def test__op_rmul__then_multiplying_each_coefficient(self):
        # when
        result = 2 * self.test_object
        # then
        assert_that(result.coefficients).is_equal_to([4, 6, 0, -4])
        assert_that(result.free).is_equal_to(30)

    def test__op_imul__then_multiplying_each_coefficient(self):
        # when
        self.test_object *= 2
        # then
        assert_that(self.test_object.coefficients).is_equal_to([4, 6, 0, -4])
        assert_that(self.test_object.free).is_equal_to(30)

    def test__op_truediv__then_dividing_each_coefficient(self):
        # when
        result = self.test_object / -2
        # then
        assert_that(result.coefficients).is_equal_to([-1, -1.5, 0, 1])
        assert_that(result.free).is_equal_to(-7.5)

    def test__op_truediv__when_zero__then_zero_division_error(self):
        # when
        def function(constant):
            return self.test_object / constant

        # then
        assert_that(function).raises(ZeroDivisionError).when_called_with(0)

    def test__op_itruediv__then_dividing_each_coefficient(self):
        # when
        self.test_object /= -2
        # then
        assert_that(self.test_object.coefficients).is_equal_to([-1, -1.5, 0, 1])
        assert_that(self.test_object.free).is_equal_to(-7.5)

    def test__combine__when_constant_is_non_zero__then_combined(self):
        # when
        self.test_object.combine(Equation([1, -1, 4, 10], 5), -2)
        # then
        assert_that(self.test_object.coefficients).is_equal_to([0, 5, -8, -22])
        assert_that(self.test_object.free).is_equal_to(5)

    def test__combine__when_constant_is_zero__then_arithmetic_error(self):
        # when
        def function(constant):
            return self.test_object.combine(Equation([1, -1, 10, 7], 5), constant)

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(0)
