# -*- coding: utf-8 -*-
"""Tests: Structure of fraction"""
from unittest import TestCase

from algolib.mathmat import Fraction


class FractionTest(TestCase):
    def test__invert__when_zero__then_arithmetic_error(self):
        # given
        frac = Fraction()
        # then
        with self.assertRaises(ArithmeticError):
            # when
            _ = ~frac
