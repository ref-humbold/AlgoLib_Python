# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZANIA LICZB PIERWSZYCH PRZEZ SITO ERASTOTENESA"""
from math import sqrt


def primes(*numbers):
    """Wyznaczanie liczb pierwszych.
    :param numbers: granice przedziału
    :returns: lista liczb pierwszych"""
    if len(numbers) == 1:
        return _find_primes(0, numbers[0])
    elif len(numbers) == 2:
        return _find_primes(numbers[0], numbers[1])
    else:
        raise TypeError("Expected 1 or 2 arguments, got " + str(len(numbers)) + ".")


def _find_primes(min_number, max_number):
    """Wyznaczanie liczb pierwszych na przedziale domknietym.
    :param min_number: dolna granica przedziału
    :param max_number: górna granica przedziału
    :returns: lista liczb pierwszych"""
    if max_number < 2:
        return []

    is_prime = [i == 2 or (i > 2 and i % 2 == 1) for i in range(min_number, max_number + 1)]
    base_primes = [True] * int(sqrt(max_number) // 2)

    for i, prime in enumerate(base_primes):
        if prime:
            num = 2 * i + 3
            begin = max(num * num - min_number, num - min_number % num)

            for j in range(num * num, len(base_primes), 2 * num):
                base_primes[(j - 3) // 2] = False

            for j in range(begin, len(is_prime), num):
                is_prime[j] = False

    return [min_number + i for i, prime in enumerate(is_prime) if prime]
