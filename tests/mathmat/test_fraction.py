# -*- coding: utf-8 -*-
"""Tests: Structure of fraction"""
from unittest import TestCase

from algolib.mathmat import Fraction


class FractionTest(TestCase):
    def test__op_str__then_negated(self):
        # when
        result = str(Fraction(23, -18))
        # then
        self.assertEqual("-23/18", result)

    def test__op_pos__then_copied(self):
        # given
        fraction = Fraction(23, 18)
        # when
        result = +fraction
        # then
        self.assertIsNot(fraction, result)
        self.assertEqual(Fraction(23, 18), result)

    def test__op_neg__then_negated(self):
        # when
        result = -Fraction(23, 18)
        # then
        self.assertEqual(Fraction(-23, 18), result)

    def test__op_abs__then_absolute_value(self):
        # when
        result = abs(Fraction(-23, 18))
        # then
        self.assertEqual(Fraction(23, 18), result)

    def test__op_invert__then_inverted(self):
        # when
        result = ~Fraction(23, 18)
        # then
        self.assertEqual(Fraction(18, 23), result)

    def test__op_invert__when_zero__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            _ = ~Fraction()

    def test__op_add__then_added_normalized(self):
        # when
        result = Fraction(1, 2) + Fraction(5, 7)
        # then
        self.assertEqual(Fraction(17, 14), result)

    def test__op_iadd__then_added_normalized(self):
        # given
        fraction = Fraction(1, 2)
        # when
        fraction += Fraction(5, 7)
        # then
        self.assertEqual(Fraction(17, 14), fraction)

    def test__op_sub__then_subtracted_normalized(self):
        # when
        result = Fraction(1, 2) - Fraction(3, 10)
        # then
        self.assertEqual(Fraction(1, 5), result)

    def test__op_isub__then_subtracted_normalized(self):
        # given
        fraction = Fraction(1, 2)
        # when
        fraction -= Fraction(3, 10)
        # then
        self.assertEqual(Fraction(1, 5), fraction)

    def test__op_mul__then_multiplied_normalized(self):
        # when
        result = Fraction(3, 7) * Fraction(5, 12)
        # then
        self.assertEqual(Fraction(5, 28), result)

    def test__op_imul__then_multiplied_normalized(self):
        # given
        fraction = Fraction(3, 7)
        # when
        fraction *= Fraction(5, 12)
        # then
        self.assertEqual(Fraction(5, 28), fraction)

    def test__op_truediv__then_divided_normalized(self):
        # when
        result = Fraction(9, 14) / Fraction(2, 5)
        # then
        self.assertEqual(Fraction(45, 28), result)

    def test__op_itruediv__then_divided_normalized(self):
        # given
        fraction = Fraction(9, 14)
        # when
        fraction /= Fraction(2, 5)
        # then
        self.assertEqual(Fraction(45, 28), fraction)

    def test__op_truediv__when_zero__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            _ = Fraction(9, 14) / Fraction()
