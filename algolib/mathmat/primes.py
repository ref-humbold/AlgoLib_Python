# -*- coding: utf-8 -*-
"""Algorithms for prime numbers"""
from math import sqrt
from random import randint
from typing import Generator

from algolib.mathmat.maths import gcd, power_mod


def find_primes(*numbers: int) -> Generator[int, None, None]:
    """Finds prime numbers inside a range of integers.

    :param numbers: range borders; beginning inclusive, ending exclusive; beginning can be omitted,
    then defaults to 0
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

    if number in (2, 3):
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    return all(
        map(lambda rdv: gcd(rdv, number) == 1 and power_mod(rdv, number - 1, number) == 1,
            [randint(1, number - 1) for _ in range(15)]))


def test_miller(number: int) -> bool:
    """Checks whether specified number is prime running Miller-Rabin's prime test.

    :param number: number to check
    :return: ``true`` if the number is probably prime, otherwise ``false``"""
    number = abs(number)

    if number in (2, 3):
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    multiplicand = number - 1

    while multiplicand % 2 == 0:
        multiplicand >>= 1

    for _ in range(15):
        rdv = randint(1, number - 1)
        exponent = multiplicand

        if power_mod(rdv, exponent, number) != 1:
            is_composite = True

            while exponent <= number / 2:
                pwm = power_mod(rdv, exponent, number)
                is_composite = is_composite and pwm != number - 1
                exponent <<= 1

            if is_composite:
                return False

    return True


def _find_primes_range(min_number: int, max_number: int) -> Generator[int, None, None]:
    # Finds prime numbers inside a specified range (minimum inclusive, maximum exclusive)
    if max_number <= min_number or max_number < 2:
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
