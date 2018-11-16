# -*- coding: utf-8 -*-
"""TESTS FOR ALGORITMS FOR PRIME NUMBERS"""
import unittest
from algolib.math import find_primes


class PrimesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_primes_when_zero_args(self):
        with self.assertRaises(TypeError):
            find_primes()

    def test_find_primes_when_three_args(self):
        with self.assertRaises(TypeError):
            find_primes(20, 200, 10)

    def test_find_primes_when_two_args_descending(self):
        with self.assertRaises(ValueError):
            find_primes(100, 30)

    def test_find_primes_one_arg_is_two_args_with_zero_as_min(self):
        result1 = find_primes(100)
        result2 = find_primes(0, 100)

        self.assertListEqual(list(result1), list(result2))

    def test_find_primes_one_arg(self):
        result = find_primes(100)

        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], list(result))

    def test_find_primes_one_arg_when_max_is_prime(self):
        result = find_primes(67)

        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                              43, 47, 53, 59, 61, 67], list(result))

    def test_find_primes_one_arg_when_less_than_two(self):
        result = find_primes(1)

        self.assertListEqual([], list(result))

    def test_find_primes_two_args(self):
        result = find_primes(30, 200)

        self.assertListEqual([31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                              103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                              173, 179, 181, 191, 193, 197, 199], list(result))

    def test_find_primes_two_args_when_min_less_than_sqrt_of_max(self):
        result = find_primes(5, 150)

        self.assertListEqual([5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                              71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                              139, 149], list(result))

    def test_find_primes_two_args_when_min_and_max_are_find_primes(self):
        result = find_primes(137, 317)

        self.assertListEqual([137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                              199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
                              277, 281, 283, 293, 307, 311, 313, 317], list(result))

    def test_find_primes_two_args_when_min_equals_max_and_prime(self):
        result = find_primes(41, 41)

        self.assertListEqual([41], list(result))

    def test_find_primes_two_args_when_min_equals_max_and_composite(self):
        result = find_primes(91, 91)

        self.assertListEqual([], list(result))
