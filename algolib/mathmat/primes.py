# -*- coding: utf-8 -*-
"""Algorithms for prime numbers"""
from math import sqrt
from random import randint
from typing import Iterable

from algolib.mathmat.maths import gcd, power_mod


def find_primes(*numbers: int) -> Iterable[int]:
    """Finds prime numbers inside a range of integers.

    :param numbers: range borders; beginning inclusive (defaults to 0), ending exclusive
    :return: generator of prime numbers"""
    if len(numbers) == 1:
        return _find_primes_range(0, numbers[0])

    if len(numbers) == 2:
        return _find_primes_range(numbers[0], numbers[1])

    raise TypeError(f"Expected 1 or 2 arguments, got {len(numbers)}")


def test_fermat(number: int) -> bool:
    """Checks whether specified number is prime running Fermat's prime test.

    :param number: number to check
    :return: ``true`` if the number is probably prime, otherwise ``false``"""
    number = abs(number)

    if number in {2, 3}:
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    for _ in range(17):
        witness = randint(1, number - 1)

        if gcd(witness, number) > 1 and power_mod(witness, number - 1, number) != 1:
            return False

    return True


def test_miller(number: int) -> bool:
    """Checks whether specified number is prime running Miller-Rabin's prime test.

    :param number: number to check
    :return: ``true`` if the number is probably prime, otherwise ``false``"""
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

        if power_mod(witness, multiplicand, number) != 1:
            exponents = []
            exp = multiplicand

            while exp <= number // 2:
                exponents.append(exp)
                exp *= 2

            if all(map(lambda d, wit=witness: power_mod(wit, d, number) != number - 1, exponents)):
                return False

    return True


def _find_primes_range(min_number, max_number):
    # Finds prime numbers inside a specified range (minimum inclusive, maximum exclusive)
    if max_number <= min_number or max_number <= 2:
        return

    is_prime = [i == 2 or (i > 2 and i % 2 == 1) for i in range(min_number, max_number)]
    base_primes = [True] * int(sqrt(max_number) / 2)

    for i, prime in enumerate(base_primes):
        if prime:
            num = 2 * i + 3
            begin = num * num - min_number if min_number < num * num else -min_number % num

            for j in range((num * num - 3) // 2, len(base_primes), num):
                base_primes[j] = False

            for j in range(begin, len(is_prime), num):
                is_prime[j] = False

    yield from (min_number + i for i, prime in enumerate(is_prime) if prime)
