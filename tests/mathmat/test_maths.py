# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic mathematics"""
import unittest

from assertpy import assert_that

from algolib.mathmat import gcd, lcm, multiply, power


class MathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region gcd

    @staticmethod
    def test__gcd__when_numbers_are_composite__then_gcd():
        # when
        result = gcd(161, 46)
        # then
        assert_that(result).is_equal_to(23)

    @staticmethod
    def test__gcd__when_numbers_are_prime__then_one():
        # when
        result = gcd(127, 41)
        # then
        assert_that(result).is_equal_to(1)

    @staticmethod
    def test__gcd__when_numbers_are_mutually_prime__then_one():
        # when
        result = gcd(119, 57)
        # then
        assert_that(result).is_equal_to(1)

    @staticmethod
    def test__gcd__when_one_of_numbers_is_multiple_of_another__then_less_number():
        # given
        number = 34
        # when
        result = gcd(number, number * 6)
        # then
        assert_that(result).is_equal_to(number)

    @staticmethod
    def test__gcd__when_one_of_numbers_is_zero__then_another_number():
        # given
        number = 96
        # when
        result = gcd(number, 0)
        # then
        assert_that(result).is_equal_to(number)

    # endregion
    # region lcm

    @staticmethod
    def test__lcm__when_numbers_are_composite__then_lcm():
        # when
        result = lcm(161, 46)
        # then
        assert_that(result).is_equal_to(322)

    @staticmethod
    def test__lcm__when_numbers_are_prime__then_product():
        # when
        result = lcm(127, 41)
        # then
        assert_that(result).is_equal_to(5207)

    @staticmethod
    def test__lcm__when_numbers_are_mutually_prime__then_product():
        # when
        result = lcm(119, 57)
        # then
        assert_that(result).is_equal_to(6783)

    @staticmethod
    def test__lcm__when_one_of_numbers_is_multiple_of_another__then_greater_number():
        # given
        number = 34
        # when
        result = lcm(number, number * 6)
        # then
        assert_that(result).is_equal_to(number * 6)

    @staticmethod
    def test__lcm__when_one_of_numbers_is_zero__then_zero():
        # when
        result = lcm(96, 0)
        # then
        assert_that(result).is_equal_to(0)

    # endregion
    # region multiply

    @staticmethod
    def test__multiply__when_first_factor_is_zero():
        # when
        result = multiply(0, 14)
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__multiply__when_second_factor_is_zero():
        # when
        result = multiply(14, 0)
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__multiply__when_factors_are_zero():
        # when
        result = multiply(0, 0)
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__multiply__when_factors_are_positive__then_result_is_positive():
        # when
        result = multiply(3, 10)
        # then
        assert_that(result).is_equal_to(30)

    @staticmethod
    def test__multiply__when_first_factor_is_negative_and_second_factor_is_positive__then_result_is_negative():
        # when
        result = multiply(-3, 10)
        # then
        assert_that(result).is_equal_to(-30)

    @staticmethod
    def test__multiply__when_first_factor_is_positive_and_second_factor_is_negative__then_result_is_negative():
        # when
        result = multiply(3, -10)
        # then
        assert_that(result).is_equal_to(-30)

    @staticmethod
    def test__multiply__when_factors_are_negative__then_result_is_positive():
        # when
        result = multiply(-3, -10)
        # then
        assert_that(result).is_equal_to(30)

    @staticmethod
    def test__multiply__when_modulo_and_factors_are_positive():
        # when
        result = multiply(547, 312, 10000)
        # then
        assert_that(result).is_equal_to(664)

    @staticmethod
    def test__multiply__when_modulo_is_positive_and_first_factor_is_negative():
        # when
        result = multiply(-547, 312, 10000)
        # then
        assert_that(result).is_equal_to(9336)

    @staticmethod
    def test__multiply__when_modulo_is_positive_and_second_factor_is_negative():
        # when
        result = multiply(547, -312, 10000)
        # then
        assert_that(result).is_equal_to(9336)

    @staticmethod
    def test__multiply__when_modulo_is_positive_and_factors_are_negative():
        # when
        result = multiply(-547, -312, 10000)
        # then
        assert_that(result).is_equal_to(664)

    @staticmethod
    def test__multiply__when_modulo_is_negative__then_arithmetic_error():
        # when
        def function(modulo):
            return multiply(547, 312, modulo)

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(-10000)

    # endregion
    # region power

    @staticmethod
    def test__power__when_base_is_zero__then_zero():
        # when
        result = power(0, 14)
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__power__when_exponent_is_zero__then_one():
        # when
        result = power(14, 0)
        # then
        assert_that(result).is_equal_to(1)

    @staticmethod
    def test__power__when_base_and_exponent_are_zero__then_nan():
        # when
        result = power(0, 0)
        # then
        assert_that(result).is_nan()

    @staticmethod
    def test__power__when_base_and_exponent_are_positive__then_result_is_positive():
        # when
        result = power(3, 10)
        # then
        assert_that(result).is_equal_to(59049)

    @staticmethod
    def test__power__when_base_is_negative_and_exponent_is_even__then_result_is_positive():
        # when
        result = power(-3, 10)
        # then
        assert_that(result).is_equal_to(59049)

    @staticmethod
    def test__power__when_base_is_negative_and_exponent_is_odd__then_result_is_negative():
        # when
        result = power(-3, 9)
        # then
        assert_that(result).is_equal_to(-19683)

    @staticmethod
    def test__power__when_exponent_is_negative__then_arithmetic_error():
        def function(exponent):
            return power(3, exponent)

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(-10)

    @staticmethod
    def test__power__when_modulo_and_base_are_positive():
        # when
        result = power(5, 11, 10000)
        # then
        assert_that(result).is_equal_to(8125)

    @staticmethod
    def test__power__when_modulo_is_positive_and_base_is_negative_and_exponent_is_odd():
        # when
        result = power(-5, 11, 10000)
        # then
        assert_that(result).is_equal_to(1875)

    @staticmethod
    def test__power__when_modulo_is_positive_and_base_is_negative_and_exponent_is_even():
        # when
        result = power(-5, 12, 10000)
        # then
        assert_that(result).is_equal_to(625)

    @staticmethod
    def test__power__when_modulo_is_negative__then_arithmetic_error():
        # when
        def function(modulo):
            return power(5, 11, modulo)

        # then
        assert_that(function).raises(ArithmeticError).when_called_with(-10000)

    # endregion
