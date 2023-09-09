# -*- coding: utf-8 -*-
"""Tests: Structure of linear equation"""
import unittest

from assertpy import assert_that

from algolib.maths import Equation


class EquationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = Equation([2, 3, 0, -2.5], 15)

    @staticmethod
    def coefficients(eq):
        return [eq[i] for i in range(len(eq))]

    def test__op_repr__then_string_representation(self):
        # when
        result = repr(self.test_object)
        # then
        assert_that(result).is_equal_to("Equation([2, 3, 0, -2.5], 15)")

    def test__op_str__then_string_representation(self):
        # when
        result = str(self.test_object)
        # then
        assert_that(result).is_equal_to("2 x_0 + 3 x_1 + -2.5 x_3 = 15")

    def test__op_pos__then_copied(self):
        # when
        result = +self.test_object
        # then
        assert_that(result).is_not_same_as(self.test_object)
        assert_that(self.coefficients(result)).is_equal_to(self.coefficients(self.test_object))
        assert_that(result.free).is_equal_to(self.test_object.free)

    def test__op_neg__then_negated(self):
        # when
        result = -self.test_object
        # then
        assert_that(self.coefficients(result)).is_equal_to([-2, -3, 0, 2.5])
        assert_that(result.free).is_equal_to(-15)

    def test__op_add__then_adding_equations(self):
        # when
        result = self.test_object + Equation([1, -1, 4, 10], 5)
        # then
        assert_that(self.coefficients(result)).is_equal_to([3, 2, 4, 7.5])
        assert_that(result.free).is_equal_to(20)

    def test__op_iadd__then_adding_equations(self):
        # when
        self.test_object += Equation([1, -1, 4, 10], 5)
        # then
        assert_that(self.coefficients(self.test_object)).is_equal_to([3, 2, 4, 7.5])
        assert_that(self.test_object.free).is_equal_to(20)

    def test__op_sub__then_subtracting_equation(self):
        # when
        result = self.test_object - Equation([1, -1, 4, 10], 5)
        # then
        assert_that(self.coefficients(result)).is_equal_to([1, 4, -4, -12.5])
        assert_that(result.free).is_equal_to(10)

    def test__op_isub__then_subtracting_equation(self):
        # when
        self.test_object -= Equation([1, -1, 4, 10], 5)
        # then
        assert_that(self.coefficients(self.test_object)).is_equal_to([1, 4, -4, -12.5])
        assert_that(self.test_object.free).is_equal_to(10)

    def test__op_mul__then_multiplying_each_coefficient(self):
        # when
        result = self.test_object * 2
        # then
        assert_that(self.coefficients(result)).is_equal_to([4, 6, 0, -5])
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
        assert_that(self.coefficients(result)).is_equal_to([4, 6, 0, -5])
        assert_that(result.free).is_equal_to(30)

    def test__op_imul__then_multiplying_each_coefficient(self):
        # when
        self.test_object *= 2
        # then
        assert_that(self.coefficients(self.test_object)).is_equal_to([4, 6, 0, -5])
        assert_that(self.test_object.free).is_equal_to(30)

    def test__op_truediv__then_dividing_each_coefficient(self):
        # when
        result = self.test_object / -2
        # then
        assert_that(self.coefficients(result)).is_equal_to([-1, -1.5, 0, 1.25])
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
        assert_that(self.coefficients(self.test_object)).is_equal_to([-1, -1.5, 0, 1.25])
        assert_that(self.test_object.free).is_equal_to(-7.5)

    def test__has_solution__when_solution__then_true(self):
        # when
        result = self.test_object.has_solution([10, 10, -29, 14])
        # then
        assert_that(result).is_true()

    def test__has_solution__when_not_solution__then_false(self):
        # when
        result = self.test_object.has_solution([10, 6, -17, 14])
        # then
        assert_that(result).is_false()
