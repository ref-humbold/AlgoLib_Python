# -*- coding: utf-8 -*-
"""Tests: Structure of fraction"""
from unittest import TestCase

from algolib.mathmat import Fraction


class FractionTest(TestCase):
    def test__op_add__then_added_normalized(self):
        # when
        result = Fraction(1, 2) + Fraction(5, 7)
        # then
        self.assertEqual(Fraction(17, 14), result)

    def test__op_sub__then_subtracted_normalized(self):
        # when
        result = Fraction(1, 2) - Fraction(3, 10)
        # then
        self.assertEqual(Fraction(1, 5), result)

    def test__op_mul__then_multiplied_normalized(self):
        # when
        result = Fraction(3, 7) * Fraction(5, 12)
        # then
        self.assertEqual(Fraction(5, 28), result)

    def test__op_truediv__then_divided_normalized(self):
        # when
        result = Fraction(9, 14) / Fraction(2, 5)
        # then
        self.assertEqual(Fraction(45, 28), result)

    def test__op_truediv__when_zero__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            _ = Fraction(9, 14) / Fraction()

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
