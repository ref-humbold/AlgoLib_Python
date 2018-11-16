# -*- coding: utf-8 -*-
"""TESTS FOR BASIC MATHEMATICS ALGORITHMS"""
import unittest
from math import isnan
from algolib.math import gcd, lcm, power_mod, mult_mod


class MathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gcd_when_numbers_are_composite(self):
        number1 = 161
        number2 = 46

        result = gcd(number1, number2)

        self.assertEqual(23, result)

    def test_gcd_when_numbers_are_prime(self):
        number1 = 127
        number2 = 41

        result = gcd(number1, number2)

        self.assertEqual(1, result)

    def test_gcd_when_numbers_are_mutually_prime(self):
        number1 = 119
        number2 = 57

        result = gcd(number1, number2)

        self.assertEqual(1, result)

    def test_gcd_when_one_of_numbers_is_multiple_of_another(self):
        number1 = 272
        number2 = 34

        result = gcd(number1, number2)

        self.assertEqual(number2, result)

    def test_gcd_when_one_of_numbers_is_zero(self):
        number1 = 96
        number2 = 0

        result = gcd(number1, number2)

        self.assertEqual(number1, result)

    def test_lcm_when_numbers_are_composite(self):
        number1 = 161
        number2 = 46

        result = lcm(number1, number2)

        self.assertEqual(322, result)

    def test_lcm_when_numbers_are_prime(self):
        number1 = 127
        number2 = 41

        result = lcm(number1, number2)

        self.assertEqual(5207, result)

    def test_lcm_when_numbers_are_mutually_prime(self):
        number1 = 119
        number2 = 57

        result = lcm(number1, number2)

        self.assertEqual(6783, result)

    def test_lcm_when_one_of_numbers_is_multiple_of_another(self):
        number1 = 272
        number2 = 34

        result = lcm(number1, number2)

        self.assertEqual(number1, result)

    def test_lcm_when_one_of_numbers_is_zero(self):
        number1 = 96
        number2 = 0

        result = lcm(number1, number2)

        self.assertEqual(number2, result)

    def test_power_mod_when_base_is_zero(self):
        number1 = 0
        number2 = 14
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertEqual(number1, result)

    def test_power_mod_when_exponent_is_zero(self):
        number1 = 14
        number2 = 0
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertEqual(1, result)

    def test_power_mod_when_base_and_exponent_are_zero(self):
        number1 = 0
        number2 = 0
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertTrue(isnan(result))

    def test_power_mod_when_base_and_exponent_are_positive(self):
        number1 = 3
        number2 = 10
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertEqual(59049, result)

    def test_power_mod_when_base_is_negative_and_exponent_is_even(self):
        number1 = -3
        number2 = 10
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertEqual(59049, result)

    def test_power_mod_when_base_is_negative_and_exponent_is_odd(self):
        number1 = -3
        number2 = 9
        number3 = 0

        result = power_mod(number1, number2, number3)

        self.assertEqual(-19683, result)

    def test_power_mod_when_exponent_is_negative(self):
        number1 = 3
        number2 = -10
        number3 = 0

        with self.assertRaises(ArithmeticError):
            power_mod(number1, number2, number3)

    def test_power_mod_when_modulo_and_base_are_positive(self):
        number1 = 5
        number2 = 11
        number3 = 10000

        result = power_mod(number1, number2, number3)

        self.assertEqual(8125, result)

    def test_power_mod_when_modulo_is_positive_and_base_is_negative(self):
        number1 = -5
        number2 = 11
        number3 = 10000

        result = power_mod(number1, number2, number3)

        self.assertEqual(1875, result)

    def test_power_mod_when_modulo_is_negative(self):
        number1 = 5
        number2 = 11
        number3 = -10000

        with self.assertRaises(ArithmeticError):
            power_mod(number1, number2, number3)

    def test_mult_mod_when_factor1_is_zero(self):
        number1 = 0
        number2 = 14
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(number1, result)

    def test_power_mod_when_factor2_is_zero(self):
        number1 = 14
        number2 = 0
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(number2, result)

    def test_mult_mod_when_factors_are_zero(self):
        number1 = 0
        number2 = 0
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(number1, result)

    def test_mult_mod_when_factor1_is_negative_and_factor2_is_positive(self):
        number1 = -3
        number2 = 10
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(-30, result)

    def test_mult_mod_when_factor1_is_positive_and_factor2_is_negative(self):
        number1 = 3
        number2 = -10
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(-30, result)

    def test_mult_mod_when_factors_are_negative(self):
        number1 = -3
        number2 = -10
        number3 = 0

        result = mult_mod(number1, number2, number3)

        self.assertEqual(30, result)

    def test_mult_mod_when_modulo_and_factors_are_positive(self):
        number1 = 547
        number2 = 312
        number3 = 10000

        result = mult_mod(number1, number2, number3)

        self.assertEqual(664, result)

    def test_mult_mod_when_modulo_is_positive_and_factor1_is_negative(self):
        number1 = -547
        number2 = 312
        number3 = 10000

        result = mult_mod(number1, number2, number3)

        self.assertEqual(9336, result)

    def test_mult_mod_when_modulo_is_positive_and_factor2_is_negative(self):
        number1 = 547
        number2 = -312
        number3 = 10000

        result = mult_mod(number1, number2, number3)

        self.assertEqual(9336, result)

    def test_mult_mod_when_modulo_is_positive_and_factors_are_negative(self):
        number1 = -547
        number2 = -312
        number3 = 10000

        result = mult_mod(number1, number2, number3)

        self.assertEqual(664, result)

    def test_mult_mod_when_modulo_is_negative(self):
        number1 = 547
        number2 = 312
        number3 = -10000

        with self.assertRaises(ArithmeticError):
            mult_mod(number1, number2, number3)
