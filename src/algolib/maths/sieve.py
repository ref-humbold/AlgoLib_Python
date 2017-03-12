# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZANIA LICZB PIERWSZYCH PRZEZ SITO ERASTOTENESA"""
from math import sqrt

def primes(*numbers):
    """Funkcja obsługująca.
    :param numbers: granice przedziału
    :returns: lista liczb pierwszych"""
    if len(numbers) == 1:
        return _find_primes(0, numbers[0])
    elif len(numbers) == 2:
        return _find_primes(numbers[0], numbers[1])
    else:
        raise TypeError("Expected 1 or 2 arguments, got "+str( len(numbers) )+".")


def find_primes(min_number, max_number):
    """Wyznaczanie liczb pierwszych na przedziale domknietym.
    :param min_number: dolna granica przedziału
    :param max_number: górna granica przedziału
    :returns: lista liczb pierwszych"""
    if max_number < 2:
        return []

    is_prime = [i == 2 or (i > 2 and i%2 == 1) for i in range(min_number, max_number+1)]
    base_primes = [True]*int(sqrt(max_number)//2)

    for i, prm in enumerate(base_primes):
        if prm:
            n = 2*i+3
            begin = max(n*n-min_number, n-min_number%n)

            for j in range(n*n, len(base_primes), 2*n):
                base_primes[ (j-3)//2 ] = False

            for j in range(begin, len(is_prime), n):
                is_prime[j] = False

    return [min_number+i for i, prm in enumerate(is_prime) if prm]
