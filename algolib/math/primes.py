# -*- coding: utf-8 -*-
"""Algoritms for prime numbers"""
from random import randint
from math import sqrt
from .maths import gcd, power_mod


def find_primes(*numbers):
    """Wyznaczanie liczb pierwszych
    :param numbers: granice przedziału
    :returns: lista liczb pierwszych"""
    if len(numbers) == 1:
        return _find_primes_range(0, numbers[0])

    if len(numbers) == 2:
        return _find_primes_range(numbers[0], numbers[1])

    raise TypeError("Expected 1 or 2 arguments, got {0}".format(len(numbers)))


def test_fermat(number):
    """Test pierwszości Fermata
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number in (2, 3):
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    return all(map(lambda rdv: gcd(rdv, number) == 1
                   and power_mod(rdv, number - 1, number) == 1,
                   [randint(1, number - 1) for _ in range(12)]))


def test_miller(number):
    """Test pierwszości Millera-Rabina
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number in (2, 3):
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    expon, multip = _distribute(number - 1)

    return all(map(lambda rdv: power_mod(rdv, multip, number) == 1
                   or any(power_mod(rdv, (1 << i) * multip, number) == number - 1
                          for i in range(expon)),
                   [randint(1, number - 1) for _ in range(12)]))


def _find_primes_range(min_number, max_number):
    """Wyznaczanie liczb pierwszych na przedziale domknietym
    :param min_number: dolna granica przedziału
    :param max_number: górna granica przedziału
    :returns: lista liczb pierwszych"""
    if max_number < min_number:
        raise ValueError(
            "Second argument must be grater or equal to the first argument.")

    if max_number < 2:
        return []

    is_prime = [i == 2 or (i > 2 and i % 2 == 1)
                for i in range(min_number, max_number + 1)]
    base_primes = [True] * int(sqrt(max_number) / 2)

    for i, prime in enumerate(base_primes):
        if prime:
            num = 2 * i + 3
            begin = num * num - min_number if min_number < num * num else -min_number % num

            for j in range((num * num - 3) // 2, len(base_primes), num):
                base_primes[j] = False

            for j in range(begin, len(is_prime), num):
                is_prime[j] = False

    return (min_number + i for i, prime in enumerate(is_prime) if prime)


def _distribute(number):
    """Rozkładanie liczby do testu Millera-Rabina
    :param number: rozkładana liczba
    :returns: rozkład liczby"""
    power = 2
    expon = 1

    while number % power == 0:
        expon += 1
        power <<= 1

    expon -= 1

    return expon, number // (1 << expon)
