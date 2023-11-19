# -*- coding: utf-8 -*-
"""Algorithms for testing prime numbers."""
from random import randint

from algolib.maths.maths import gcd, power


def test_prime_fermat(number: int) -> bool:
    """Checks whether given number is prime using Fermat prime test.

    :param number: the number
    :return: ``True`` if the number is probably prime, otherwise ``False``"""
    number = abs(number)

    if number in {2, 3}:
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    for _ in range(17):
        witness = randint(1, number - 1)

        if gcd(witness, number) > 1 or power(witness, number - 1, number) != 1:
            return False

    return True


def test_prime_miller(number: int) -> bool:
    """Checks whether given number is prime using Miller-Rabin prime test.

    :param number: the number
    :return: ``True`` if the number is probably prime, otherwise ``False``"""
    number = abs(number)

    if number in {2, 3}:
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    multiplicand = number - 1

    while multiplicand % 2 == 0:
        multiplicand //= 2

    for _ in range(17):
        witness = randint(1, number - 1)

        if power(witness, multiplicand, number) != 1:
            exponents = []
            exp = multiplicand

            while exp <= number // 2:
                exponents.append(exp)
                exp *= 2

            if all(power(witness, d, number) != number - 1 for d in exponents):
                return False

    return True
