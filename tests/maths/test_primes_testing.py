# -*- coding: utf-8 -*-
"""Tests: Algorithms for testing prime numbers"""
import unittest

from assertpy import assert_that

from algolib.maths import test_prime_fermat, test_prime_miller


class PrimesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region test_test_prime_fermat

    @staticmethod
    def test__test_prime_fermat__when_zero__then_false():
        # when
        result = test_prime_fermat(0)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_fermat__when_one__then_false():
        # when
        result = test_prime_fermat(1)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_fermat__when_two__then_true():
        # when
        result = test_prime_fermat(2)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_fermat__when_prime_1__then_true():
        # when
        result = test_prime_fermat(1013)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_fermat__when_prime_2__then_true():
        # when
        result = test_prime_fermat(2131)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_fermat__when_prime_3__then_true():
        # when
        result = test_prime_fermat(6199)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_fermat__when_composite_1__then_false():
        # when
        result = test_prime_fermat(1001)  # 1001 = 7 * 11 * 13
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_fermat__when_composite_2__then_false():
        # when
        result = test_prime_fermat(41041)  # 41041 = 7 * 11 * 13 * 41
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_fermat__when_composite_3__then_false():
        # when
        result = test_prime_fermat(73627)  # 73627 = 17 * 61 * 71
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_fermat__when_composite_square_of_prime__then_false():
        # when
        result = test_prime_fermat(3481)  # 3481 = 59 ^ 2
        # then
        assert_that(result).is_false()

    # endregion
    # region test_test_prime_miller

    @staticmethod
    def test__test_prime_miller__when_zero__then_false():
        # when
        result = test_prime_miller(0)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_miller__when_one__then_false():
        # when
        result = test_prime_miller(1)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_miller__when_two__then_true():
        # when
        result = test_prime_miller(2)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_miller__when_prime_1__then_true():
        # when
        result = test_prime_miller(1013)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_miller__when_prime_2__then_true():
        # when
        result = test_prime_miller(2131)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_miller__when_prime_3__then_true():
        # when
        result = test_prime_miller(6199)
        # then
        assert_that(result).is_true()

    @staticmethod
    def test__test_prime_miller__when_composite_1__then_false():
        # when
        result = test_prime_miller(1001)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_miller__when_composite_2__then_false():
        # when
        result = test_prime_miller(41041)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_miller__when_composite_3__then_false():
        # when
        result = test_prime_miller(73627)
        # then
        assert_that(result).is_false()

    @staticmethod
    def test__test_prime_miller__when_composite_square_of_prime__then_false():
        # when
        result = test_prime_miller(3481)
        # then
        assert_that(result).is_false()

    # endregion
