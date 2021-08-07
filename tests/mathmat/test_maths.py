# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic mathematics"""
from math import isnan
import unittest

from algolib.mathmat import gcd, lcm, multiply, power


class MathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region gcd

    def test__gcd__when_numbers_are_composite__then_gcd(self):
        # when
        result = gcd(161, 46)
        # then
        self.assertEqual(23, result)

    def test__gcd__when_numbers_are_prime__then_one(self):
        # when
        result = gcd(127, 41)
        # then
        self.assertEqual(1, result)

    def test__gcd__when_numbers_are_mutually_prime__then_one(self):
        # when
        result = gcd(119, 57)
        # then
        self.assertEqual(1, result)

    def test__gcd__when_one_of_numbers_is_multiple_of_another__then_less_number(self):
        # given
        number = 34
        # when
        result = gcd(number, number * 6)
        # then
        self.assertEqual(number, result)

    def test__gcd__when_one_of_numbers_is_zero__then_another_number(self):
        # given
        number = 96
        # when
        result = gcd(number, 0)
        # then
        self.assertEqual(number, result)

    # endregion
    # region lcm

    def test__lcm__when_numbers_are_composite__then_lcm(self):
        # when
        result = lcm(161, 46)
        # then
        self.assertEqual(322, result)

    def test__lcm__when_numbers_are_prime__then_product(self):
        # when
        result = lcm(127, 41)
        # then
        self.assertEqual(5207, result)

    def test__lcm__when_numbers_are_mutually_prime__then_product(self):
        # when
        result = lcm(119, 57)
        # then
        self.assertEqual(6783, result)

    def test__lcm__when_one_of_numbers_is_multiple_of_another__then_greater_number(self):
        # given
        number = 34
        # when
        result = lcm(number, number * 6)
        # then
        self.assertEqual(number * 6, result)

    def test__lcm__when_one_of_numbers_is_zero__then_zero(self):
        # when
        result = lcm(96, 0)
        # then
        self.assertEqual(0, result)

    # endregion
    # region multiply

    def test__multiply__when_first_factor_is_zero(self):
        # when
        result = multiply(0, 14)
        # then
        self.assertEqual(0, result)

    def test__multiply__when_second_factor_is_zero(self):
        # when
        result = multiply(14, 0)
        # then
        self.assertEqual(0, result)

    def test__multiply__when_factors_are_zero(self):
        # when
        result = multiply(0, 0)
        # then
        self.assertEqual(0, result)

    def test__multiply__when_factors_are_positive__then_result_is_positive(self):
        # when
        result = multiply(3, 10)
        # then
        self.assertEqual(30, result)

    def test__multiply__when_first_factor_is_negative_and_second_factor_is_positive__then_result_is_negative(
            self):
        # when
        result = multiply(-3, 10)
        # then
        self.assertEqual(-30, result)

    def test__multiply__when_first_factor_is_positive_and_second_factor_is_negative__then_result_is_negative(
            self):
        # when
        result = multiply(3, -10)
        # then
        self.assertEqual(-30, result)

    def test__multiply__when_factors_are_negative__then_result_is_positive(self):
        # when
        result = multiply(-3, -10)
        # then
        self.assertEqual(30, result)

    def test__multiply__when_modulo_and_factors_are_positive(self):
        # when
        result = multiply(547, 312, 10000)
        # then
        self.assertEqual(664, result)

    def test__multiply__when_modulo_is_positive_and_first_factor_is_negative(self):
        # when
        result = multiply(-547, 312, 10000)
        # then
        self.assertEqual(9336, result)

    def test__multiply__when_modulo_is_positive_and_second_factor_is_negative(self):
        # when
        result = multiply(547, -312, 10000)
        # then
        self.assertEqual(9336, result)

    def test__multiply__when_modulo_is_positive_and_factors_are_negative(self):
        # when
        result = multiply(-547, -312, 10000)
        # then
        self.assertEqual(664, result)

    def test__multiply__when_modulo_is_negative__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            multiply(547, 312, -10000)

    # endregion
    # region power

    def test__power__when_base_is_zero__then_zero(self):
        # when
        result = power(0, 14)
        # then
        self.assertEqual(0, result)

    def test__power__when_exponent_is_zero__then_one(self):
        # when
        result = power(14, 0)
        # then
        self.assertEqual(1, result)

    def test__power__when_base_and_exponent_are_zero__then_nan(self):
        # when
        result = power(0, 0)
        # then
        self.assertTrue(isnan(result))

    def test__power__when_base_and_exponent_are_positive__then_result_is_positive(self):
        # when
        result = power(3, 10)
        # then
        self.assertEqual(59049, result)

    def test__power__when_base_is_negative_and_exponent_is_even__then_result_is_positive(self):
        # when
        result = power(-3, 10)
        # then
        self.assertEqual(59049, result)

    def test__power__when_base_is_negative_and_exponent_is_odd__then_result_is_negative(self):
        # when
        result = power(-3, 9)
        # then
        self.assertEqual(-19683, result)

    def test__power__when_exponent_is_negative__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            power(3, -10)

    def test__power__when_modulo_and_base_are_positive(self):
        # when
        result = power(5, 11, 10000)
        # then
        self.assertEqual(8125, result)

    def test__power__when_modulo_is_positive_and_base_is_negative_and_exponent_is_odd(self):
        # when
        result = power(-5, 11, 10000)
        # then
        self.assertEqual(1875, result)

    def test__power__when_modulo_is_positive_and_base_is_negative_and_exponent_is_even(self):
        # when
        result = power(-5, 12, 10000)
        # then
        self.assertEqual(625, result)

    def test__power__when_modulo_is_negative__then_arithmetic_error(self):
        # then
        with self.assertRaises(ArithmeticError):
            # when
            power(5, 11, -10000)

    # endregion
