# -*- coding: utf-8 -*-
"""Tests: Structure of fraction."""
from unittest import TestCase

from assertpy import assert_that

from algolib.maths import Fraction


class FractionTest(TestCase):
    @staticmethod
    def test__op_str__then_negated():
        # when
        result = str(Fraction(23, -18))
        # then
        assert_that(result).is_equal_to("-23/18")

    @staticmethod
    def test__op_pos__then_copied():
        # given
        fraction = Fraction(23, 18)
        # when
        result = +fraction
        # then
        assert_that(result).is_not_same_as(fraction)
        assert_that(result).is_equal_to(Fraction(23, 18))

    @staticmethod
    def test__op_neg__then_negated():
        # when
        result = -Fraction(23, 18)
        # then
        assert_that(result).is_equal_to(Fraction(-23, 18))

    @staticmethod
    def test__op_abs__then_absolute_value():
        # when
        result = abs(Fraction(-23, 18))
        # then
        assert_that(result).is_equal_to(Fraction(23, 18))

    @staticmethod
    def test__op_invert__then_inverted():
        # when
        result = ~Fraction(23, 18)
        # then
        assert_that(result).is_equal_to(Fraction(18, 23))

    @staticmethod
    def test__op_invert__when_zero__then_arithmetic_error():
        # when
        def function(fraction):
            return ~fraction

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(Fraction())

    @staticmethod
    def test__op_add__then_added_normalized():
        # when
        result = Fraction(1, 2) + Fraction(5, 7)
        # then
        assert_that(result).is_equal_to(Fraction(17, 14))

    @staticmethod
    def test__op_iadd__then_added_normalized():
        # given
        fraction = Fraction(1, 2)
        # when
        fraction += Fraction(5, 7)
        # then
        assert_that(fraction).is_equal_to(Fraction(17, 14))

    @staticmethod
    def test__op_sub__then_subtracted_normalized():
        # when
        result = Fraction(1, 2) - Fraction(3, 10)
        # then
        assert_that(result).is_equal_to(Fraction(1, 5))

    @staticmethod
    def test__op_isub__then_subtracted_normalized():
        # given
        fraction = Fraction(1, 2)
        # when
        fraction -= Fraction(3, 10)
        # then
        assert_that(fraction).is_equal_to(Fraction(1, 5))

    @staticmethod
    def test__op_mul__then_multiplied_normalized():
        # when
        result = Fraction(3, 7) * Fraction(5, 12)
        # then
        assert_that(result).is_equal_to(Fraction(5, 28))

    @staticmethod
    def test__op_imul__then_multiplied_normalized():
        # given
        fraction = Fraction(3, 7)
        # when
        fraction *= Fraction(5, 12)
        # then
        assert_that(fraction).is_equal_to(Fraction(5, 28))

    @staticmethod
    def test__op_truediv__then_divided_normalized():
        # when
        result = Fraction(9, 14) / Fraction(2, 5)
        # then
        assert_that(result).is_equal_to(Fraction(45, 28))

    @staticmethod
    def test__op_itruediv__then_divided_normalized():
        # given
        fraction = Fraction(9, 14)
        # when
        fraction /= Fraction(2, 5)
        # then
        assert_that(fraction).is_equal_to(Fraction(45, 28))

    @staticmethod
    def test__op_truediv__when_zero__then_zero_division_error():
        # when
        def function(divisor):
            return Fraction(9, 14) / divisor

        # then
        assert_that(function).raises(ZeroDivisionError).when_called_with(Fraction())
