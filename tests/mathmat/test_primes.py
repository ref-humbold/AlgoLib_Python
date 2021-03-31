# -*- coding: utf-8 -*-
"""Tests: Algorithms for prime numbers"""
import unittest

from algolib.mathmat import find_primes, test_fermat, test_miller


class PrimesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region test_find_primes

    def test__find_primes__when_zero_args__then_type_error(self):
        # then
        with self.assertRaises(TypeError):
            # when
            find_primes()

    def test__find_primes__when_three_args__then_type_error(self):
        # when
        with self.assertRaises(TypeError):
            # then
            find_primes(20, 200, 10)

    def test__find_primes__when_two_args_descending__then_empty_generator(self):
        # when
        result = find_primes(100, 30)
        # then
        self.assertListEqual([], list(result))

    def test__find_primes__when_one_arg__then_same_as_two_args_with_zero_as_min(self):
        # when
        result1 = find_primes(100)
        result2 = find_primes(0, 100)
        # then
        self.assertListEqual(list(result1), list(result2))

    def test__find_primes__when_one_arg__then_primes_less_than_arg(self):
        # when
        result = find_primes(100)
        # then
        self.assertListEqual([
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
            83, 89, 97], list(result))

    def test__find_primes__when_max_is_prime__then_primes_less_than_arg(self):
        # when
        result = find_primes(67)
        # then
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61],
                             list(result))

    def test__find_primes__when_at_most_two(self):
        # when
        result = find_primes(2)
        # then
        self.assertListEqual([], list(result))

    def test__find_primes__when_two_args__then_primes_between(self):
        # when
        result = find_primes(30, 200)
        # then
        self.assertListEqual([
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199],
            list(result))

    def test__find_primes__when_min_less_than_sqrt_of_max__then_primes_between(self):
        # when
        result = find_primes(5, 150)
        # then
        self.assertListEqual([
            5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149], list(result))

    def test__find_primes__when_min_and_max_are_primes__then_primes_between_with_min_inclusive(
            self):
        # when
        result = find_primes(137, 317)
        # then
        self.assertListEqual([
            137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
            229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313],
            list(result))

    def test__find_primes__when_min_equals_max_and_prime__then_empty_list(self):
        # when
        result = find_primes(41, 41)
        # then
        self.assertListEqual([], list(result))

    def test__find_primes__when_min_equals_max_and_composite__then_empty(self):
        # when
        result = find_primes(91, 91)
        # then
        self.assertListEqual([], list(result))

    # endregion
    # region test_test_fermat

    def test__test_fermat__when_zero__then_false(self):
        # when
        result = test_fermat(0)
        # then
        self.assertFalse(result)

    def test__test_fermat__when_one__then_false(self):
        # when
        result = test_fermat(1)
        # then
        self.assertFalse(result)

    def test__test_fermat__when_two__then_true(self):
        # when
        result = test_fermat(2)
        # then
        self.assertTrue(result)

    def test__test_fermat__when_prime__then_true(self):
        # when
        result = test_fermat(1013)
        # then
        self.assertTrue(result)

    def test__test_fermat__when_composite__then_false(self):
        # when
        result = test_fermat(1001)
        # then
        self.assertFalse(result)

    def test__test_fermat__when_carmichael_number__then_false(self):
        # when
        result = test_fermat(1105)  # 1105 = 5 * 13 * 17 is a Carmichael number
        # then
        self.assertFalse(result)

    # endregion
    # region test_test_miller

    def test__test_miller__when_zero__then_false(self):
        # when
        result = test_miller(0)
        # then
        self.assertFalse(result)

    def test__test_miller__when_one__then_false(self):
        # when
        result = test_miller(1)
        # then
        self.assertFalse(result)

    def test__test_miller__when_two__then_true(self):
        # when
        result = test_miller(2)
        # then
        self.assertTrue(result)

    def test__test_miller__when_prime__then_true(self):
        # when
        result = test_miller(1013)
        # then
        self.assertTrue(result)

    def test__test_miller__when_composite__then_false(self):
        # when
        result = test_miller(1001)
        # then
        self.assertFalse(result)

    def test__test_miller__when_carmichael_number__then_false(self):
        # when
        result = test_miller(1105)
        # then
        self.assertFalse(result)

    # endregion
