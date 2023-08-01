# -*- coding: utf-8 -*-
"""Algorithms for prime numbers"""
from math import sqrt
from random import randint
from typing import Iterable

from algolib.maths.maths import gcd, power


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

        if gcd(witness, number) > 1 and power(witness, number - 1, number) != 1:
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

        if power(witness, multiplicand, number) != 1:
            exponents = []
            exp = multiplicand

            while exp <= number // 2:
                exponents.append(exp)
                exp *= 2

            if all(map(lambda d, wit=witness: power(wit, d, number) != number - 1, exponents)):
                return False

    return True


def _find_primes_range(minimum, maximum):
    # Finds prime numbers inside a specified range (minimum inclusive, maximum exclusive)
    if maximum <= minimum or maximum <= 2:
        return

    segment_size = int(sqrt(maximum))
    base_primes = _get_base_primes(segment_size)

    if minimum < segment_size:
        yield from (p for p in [2, *base_primes] if p >= minimum)

    for i in range(max(minimum, segment_size), maximum, segment_size):
        yield from _get_segment_primes(i, min(i + segment_size, maximum), base_primes)


def _get_base_primes(base_maximum):
    # Extracts prime numbers between 0 and given maximum value
    is_prime = [True] * ((base_maximum - 1) // 2)

    for i in range(0, int(sqrt(base_maximum) / 2)):
        if is_prime[i]:
            prime_value = 2 * i + 3

            for j in range(prime_value * prime_value, base_maximum, 2 * prime_value):
                is_prime[(j - 3) // 2] = False

    return [2 * index + 3 for index, flag in enumerate(is_prime) if flag]


def _get_segment_primes(segment_start, segment_end, base_primes):
    # Extracts prime numbers from given range using given basic prime numbers
    segment_begin = segment_start + 1 - segment_start % 2
    is_prime = [i > 2 for i in range(segment_begin, segment_end, 2)]

    for p in base_primes:
        prime_multiple = (segment_begin + p - 1) // p * p
        multiple_start = prime_multiple + p if prime_multiple % 2 == 0 else prime_multiple

        for i in range(multiple_start, segment_end, 2 * p):
            is_prime[(i - segment_begin) // 2] = False

    return (segment_begin + 2 * index for index, flag in enumerate(is_prime) if flag)
