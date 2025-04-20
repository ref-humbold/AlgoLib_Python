# -*- coding: utf-8 -*-
"""Tests: Algorithms for searching for prime numbers."""
from itertools import product
import unittest

from assertpy import assert_that

from algolib.maths import find_primes


class PrimesSearchingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                       73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                       157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
                       239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                       331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                       421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
                       509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
                       613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                       709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
                       821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                       919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        self.params_max = [2, 3, 4, 67, 100, 155, 400, 499, 701, 911]
        self.params_min_max = product([2, 3, 8, 25, 54, 71, 101, 243],
                                      [54, 150, 243, 481, 625, 827, 1000])

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
    def test__find_primes__when_single_argument__then_min_is_zero():
        # when
        result1 = find_primes(100)
        result2 = find_primes(0, 100)

        # then
        assert_that(list(result1)).is_equal_to(list(result2))

    def test__find_primes__when_maximal_number__then_max_exclusive(self):
        for number in self.params_max:
            with self.subTest(param=number):
                # when
                result = find_primes(number)

                # then
                assert_that(list(result)).is_equal_to([p for p in self.primes if p < number])

    def test__find_primes__when_range__then_min_inclusive_and_max_exclusive(self):
        for minimum, maximum in self.params_min_max:
            with self.subTest(param=(minimum, maximum)):
                # when
                result = find_primes(minimum, maximum)

                # then
                assert_that(list(result)).is_equal_to(
                    [p for p in self.primes if minimum <= p < maximum])
