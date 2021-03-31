# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic mathematics"""
from math import isnan
import unittest

from algolib.mathmat import gcd, lcm, mult_mod, power_mod


class MathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__gcd__when_numbers_are_composite(self):
        # when
        result = gcd(161, 46)
        # then
        self.assertEqual(23, result)

    def test__gcd__when_numbers_are_prime(self):
        # when
        result = gcd(127, 41)
        # then
        self.assertEqual(1, result)

    def test__gcd__when_numbers_are_mutually_prime(self):
        # when
        result = gcd(119, 57)
        # then
        self.assertEqual(1, result)

    def test__gcd__when_one_number_is_multiple_of_another(self):
        # given
        number = 34
        # when
        result = gcd(272, number)
        # then
        self.assertEqual(number, result)

    def test__gcd__when_one_number_is_zero(self):
        # given
        number = 96
        # when
        result = gcd(number, 0)
        # then
        self.assertEqual(number, result)

    def test__lcm__when_numbers_are_composite(self):
        # when
        result = lcm(161, 46)
        # then
        self.assertEqual(322, result)

    def test__lcm__when_numbers_are_prime(self):
        # when
        result = lcm(127, 41)
        # then
        self.assertEqual(5207, result)

    def test__lcm__when_numbers_are_mutually_prime(self):
        # when
        result = lcm(119, 57)
        # then
        self.assertEqual(6783, result)

    def test__lcm__when_one_of_numbers_is_multiple_of_another(self):
        # given
        number = 272
        # when
        result = lcm(number, 34)
        # then
        self.assertEqual(number, result)

    def test__lcm__when_one_of_numbers_is_zero(self):
        # when
        result = lcm(96, 0)
        # then
        self.assertEqual(0, result)

    def test__power_mod__when_base_is_zero(self):
        # when
        result = power_mod(0, 14, 0)
        # then
        self.assertEqual(0, result)

    def test__power_mod__when_exponent_is_zero(self):
        # when
        result = power_mod(14, 0, 0)
        # then
        self.assertEqual(1, result)

    def test__power_mod__when_base_and_exponent_are_zero(self):
        # when
        result = power_mod(0, 0, 0)
        # then
        self.assertTrue(isnan(result))

    def test__power_mod__when_base_and_exponent_are_positive(self):
        # when
        result = power_mod(3, 10, 0)
        # then
        self.assertEqual(59049, result)

    def test__power_mod__when_base_is_negative_and_exponent_is_even(self):
        # when
        result = power_mod(-3, 10, 0)
        # then
        self.assertEqual(59049, result)

    def test__power_mod__when_base_is_negative_and_exponent_is_odd(self):
        # when
        result = power_mod(-3, 9, 0)
        # then
        self.assertEqual(-19683, result)

    def test__power_mod__when_exponent_is_negative(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            power_mod(3, -10, 0)

    def test__power_mod__when_modulo_and_base_are_positive(self):
        # when
        result = power_mod(5, 11, 10000)
        # then
        self.assertEqual(8125, result)

    def test__power_mod__when_modulo_is_positive_and_base_is_negative(self):
        # when
        result = power_mod(-5, 11, 10000)
        # then
        self.assertEqual(1875, result)

    def test__power_mod__when_modulo_is_negative(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            power_mod(5, 11, -10000)

    def test__mult_mod__when_first_factor_is_zero(self):
        # when
        result = mult_mod(0, 14, 0)
        # then
        self.assertEqual(0, result)

    def test__power_mod__when_second_factor_is_zero(self):
        # when
        result = mult_mod(14, 0, 0)
        # then
        self.assertEqual(0, result)

    def test__mult_mod__when_factors_are_zero(self):
        # when
        result = mult_mod(0, 0, 0)
        # then
        self.assertEqual(0, result)

    def test__mult_mod__when_one_factor_is_negative_and_another_is_positive(self):
        # when
        result = mult_mod(-3, 10, 0)
        # then
        self.assertEqual(-30, result)

    def test__mult_mod__when_one_factor_is_positive_and_another_is_negative(self):
        # when
        result = mult_mod(3, -10, 0)
        # then
        self.assertEqual(-30, result)

    def test__mult_mod__when_factors_are_negative(self):
        # when
        result = mult_mod(-3, -10, 0)
        # then
        self.assertEqual(30, result)

    def test__mult_mod__when_modulo_and_factors_are_positive(self):
        # when
        result = mult_mod(547, 312, 10000)
        # then
        self.assertEqual(664, result)

    def test__mult_mod__when_modulo_is_positive_and_first_factor_is_negative(self):
        # when
        result = mult_mod(-547, 312, 10000)
        # then
        self.assertEqual(9336, result)

    def test__mult_mod__when_modulo_is_positive_and_second_factor_is_negative(self):
        # when
        result = mult_mod(547, -312, 10000)
        # then
        self.assertEqual(9336, result)

    def test__mult_mod__when_modulo_is_positive_and_factors_are_negative(self):
        # when
        result = mult_mod(-547, -312, 10000)
        # then
        self.assertEqual(664, result)

    def test__mult_mod__when_modulo_is_negative(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            mult_mod(547, 312, -10000)
