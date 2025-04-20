# -*- coding: utf-8 -*-
"""Algorithms for searching for prime numbers."""
from math import sqrt
from typing import Iterable


def find_primes(*numbers: int) -> Iterable[int]:
    """Searches for prime numbers inside given range of numbers.

    :param numbers: the range borders; the minimum inclusive (defaults to 0), the maximum exclusive
    :return: the prime numbers"""
    if len(numbers) == 1:
        return _find_primes_range(0, numbers[0])

    if len(numbers) == 2:
        return _find_primes_range(numbers[0], numbers[1])

    raise TypeError(f"Expected 1 or 2 arguments, got {len(numbers)}")


def _find_primes_range(minimum, maximum):
    # Searches for prime numbers inside given range (minimum inclusive, maximum exclusive)
    if maximum <= minimum or maximum <= 2:
        return

    segment_size = int(sqrt(maximum))
    base_primes = _get_base_primes(segment_size)

    if minimum < segment_size:
        yield from (p for p in [2, *base_primes] if p >= minimum)

    for i in range(max(minimum, segment_size), maximum, segment_size):
        yield from _get_segment_primes(i, min(i + segment_size, maximum), base_primes)


def _get_base_primes(base_maximum):
    # Extracts prime numbers between zero and given maximum value.
    is_prime = [True] * ((base_maximum - 1) // 2)

    for i in range(0, int(sqrt(base_maximum) / 2)):
        if is_prime[i]:
            prime_value = 2 * i + 3

            for j in range(prime_value * prime_value, base_maximum + 1, 2 * prime_value):
                is_prime[(j - 3) // 2] = False

    return [2 * index + 3 for index, flag in enumerate(is_prime) if flag]


def _get_segment_primes(segment_start, segment_end, base_primes):
    # Extracts prime numbers from given range using given basic prime numbers.
    segment_begin = segment_start + 1 - segment_start % 2
    is_prime = [i > 2 for i in range(segment_begin, segment_end, 2)]

    for prime in base_primes:
        prime_multiple = (segment_begin + prime - 1) // prime * prime
        multiple_start = prime_multiple + prime if prime_multiple % 2 == 0 else prime_multiple

        for i in range(multiple_start, segment_end, 2 * prime):
            is_prime[(i - segment_begin) // 2] = False

    return (segment_begin + 2 * index for index, flag in enumerate(is_prime) if flag)
