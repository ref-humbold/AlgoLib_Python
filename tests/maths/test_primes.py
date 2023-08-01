# -*- coding: utf-8 -*-
"""Tests: Algorithms for prime numbers"""
import unittest

from assertpy import assert_that

from algolib.maths import find_primes, test_fermat, test_miller


class PrimesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region test_find_primes

    @staticmethod
    def test__find_primes__when_zero_args__then_type_error():
        # when
        def function():
            find_primes()

        # then
        assert_that(function).raises(TypeError)

    @staticmethod
    def test__find_primes__when_three_args__then_type_error():
        # when
        def function():
            find_primes(20, 200, 10)

        # then
        assert_that(function).raises(TypeError)

    @staticmethod
    def test__find_primes__when_min_greater_than_max__then_empty():
        # when
        result = find_primes(100, 30)
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__find_primes__when_single_argument__then_min_is_zero():
        # when
        result1 = find_primes(100)
        result2 = find_primes(0, 100)
        # then
        assert_that(list(result1)).is_equal_to(list(result2))

    @staticmethod
    def test__find_primes__when_max_is_composite__then_all_primes():
        # when
        result = find_primes(100)
        # then
        assert_that(list(result)).is_equal_to(
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
             89, 97])

    @staticmethod
    def test__find_primes__when_max_is_prime__then_max_exclusive():
        # when
        result = find_primes(67)
        # then
        assert_that(list(
            result
        )).is_equal_to([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61])

    @staticmethod
    def test__find_primes__when_max_is_two__then_empty():
        # when
        result = find_primes(2)
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__find_primes__when_max_is_three__then_single_element():
        # when
        result = find_primes(3)
        # then
        assert_that(list(result)).is_equal_to([2])

    @staticmethod
    def test__find_primes__when_max_is_four__then_all_primes():
        # when
        result = find_primes(4)
        # then
        assert_that(list(result)).is_equal_to([2, 3])

    @staticmethod
    def test__find_primes__when_range__then_primes_between():
        # when
        result = find_primes(30, 200)
        # then
        assert_that(list(result)).is_equal_to(
            [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
             127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

    @staticmethod
    def test__find_primes__when_min_is_two__then_two_included():
        # when
        result = find_primes(2, 30)
        # then
        assert_that(list(result)).is_equal_to([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    @staticmethod
    def test__find_primes__when_min_is_three__then_two_not_included():
        # when
        result = find_primes(3, 30)
        # then
        assert_that(list(result)).is_equal_to([3, 5, 7, 11, 13, 17, 19, 23, 29])

    @staticmethod
    def test__find_primes__when_max_is_fourth_power_of_prime__then_all_primes_between():
        # when
        result = find_primes(9, 81)
        # then
        assert_that(list(
            result
        )).is_equal_to([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79])

    @staticmethod
    def test__find_primes__when_min_is_less_than_square_root_of_max__then_primes_between():
        # when
        result = find_primes(5, 150)
        # then
        assert_that(list(result)).is_equal_to(
            [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
             97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149])

    @staticmethod
    def test__find_primes__when_min_and_max_are_primes__then_min_inclusive_and_max_exclusive():
        # when
        result = find_primes(137, 317)
        # then
        assert_that(list(result)).is_equal_to(
            [137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
             229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313])

    @staticmethod
    def test__find_primes__when_min_equals_max_and_prime__then_empty():
        # when
        result = find_primes(41, 41)
        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__find_primes__when_min_equals_max_and_composite__then_empty():
        # when
        result = find_primes(91, 91)
        # then
        assert_that(list(result)).is_empty()

    # endregion
    # region test_test_fermat

    @staticmethod
    def test__test_fermat__when_zero__then_false():
        # when
        result = test_fermat(0)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_fermat__when_one__then_false():
        # when
        result = test_fermat(1)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_fermat__when_two__then_true():
        # when
        result = test_fermat(2)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_fermat__when_prime__then_true():
        # when
        result = test_fermat(1013)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_fermat__when_composite__then_false():
        # when
        result = test_fermat(1001)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_fermat__when_carmichael_number__then_false():
        # when
        result = test_fermat(1105)  # 1105 = 5 * 13 * 17 is a Carmichael number
        # then
        assert_that(result).is_false()

    # endregion
    # region test_test_miller

    @staticmethod
    def test__test_miller__when_zero__then_false():
        # when
        result = test_miller(0)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_miller__when_one__then_false():
        # when
        result = test_miller(1)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_miller__when_two__then_true():
        # when
        result = test_miller(2)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_miller__when_prime__then_true():
        # when
        result = test_miller(1013)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_miller__when_composite__then_false():
        # when
        result = test_miller(1001)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_miller__when_carmichael_number__then_false():
        # when
        result = test_miller(1105)
        # then
        assert_that(result).is_false()

    # endregion
