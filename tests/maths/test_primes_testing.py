# -*- coding: utf-8 -*-
"""Tests: Algorithms for testing prime numbers."""
import unittest

from assertpy import assert_that

from algolib.maths import test_prime_fermat, test_prime_miller


class PrimesTestingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 1001 = 7 * 11 * 13 ; 3481 = 59 ^ 2 ; 41041 = 7 * 11 * 13 * 41 ; 73627 = 17 * 61 * 71
        self.params_not_primes = [0, 1, 77, 1001, 3481, 41041, 73627]
        self.params_primes = [2, 107, 1013, 2131, 6199]

    # region test_test_prime_fermat

    def test__test_prime_fermat__when_not_prime__then_false(self):
        for number in self.params_not_primes:
            with self.subTest(param=number):
                # when
                result = test_prime_fermat(number)

                # then
                assert_that(result).is_false()

    def test__test_prime_fermat__when_prime__then_true(self):
        for number in self.params_primes:
            with self.subTest(param=number):
                # when
                result = test_prime_fermat(number)

                # then
                assert_that(result).is_true()

    # endregion
    # region test_test_prime_miller

    def test__test_prime_miller__when_not_prime__then_false(self):
        for number in self.params_not_primes:
            with self.subTest(param=number):
                # when
                result = test_prime_miller(number)

                # then
                assert_that(result).is_false()

    def test__test_prime_miller__when_prime__then_true(self):
        for number in self.params_primes:
            with self.subTest(param=number):
                # when
                result = test_prime_miller(number)

                # then
                assert_that(result).is_true()

    # endregion
