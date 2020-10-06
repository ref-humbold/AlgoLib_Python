# -*- coding: utf-8 -*-
"""Algorithms for basic mathematical computations"""
from typing import Union


def gcd(number1: int, number2: int) -> int:
    """Counts a greatest common divisor of two numbers.

    :param number1: a first number
    :param number2: a second number
    :return: greatest common divisor"""
    number_pair = (min(abs(number1), abs(number2)), max(abs(number1), abs(number2)))

    while number_pair[0] > 0:
        number_pair = (number_pair[1] % number_pair[0], number_pair[0])

    return number_pair[1]


def lcm(number1: int, number2: int) -> int:
    """Counts a lowest common multiple of two numbers.

    :param number1: a first number
    :param number2: a second number
    :return: lowest common multiple"""
    min_number = min(abs(number1), abs(number2))
    max_number = max(abs(number1), abs(number2))
    return max_number // gcd(number1, number2) * min_number


def mult_mod(factor1: int, factor2: int, modulo: int = 0) -> int:
    """Performs a fast multiplication of two numbers with modulo taken.

    :param factor1: a first factor
    :param factor2: a second factor
    :param modulo: a modulo value
    :return: multiplication result with modulo taken"""
    result = 0

    if modulo < 0:
        raise ArithmeticError("Negative modulo")

    if factor1 < 0 and factor2 < 0:
        return mult_mod(-factor1, -factor2, modulo)

    if factor1 < 0:
        return modulo - mult_mod(-factor1, factor2, modulo)

    if factor2 < 0:
        return modulo - mult_mod(factor1, -factor2, modulo)

    while factor2 > 0:
        if factor2 % 2 == 1:
            result = factor1 + result if modulo == 0 else (factor1 + result) % modulo

        factor1 = factor1 + factor1 if modulo == 0 else (factor1 + factor1) % modulo
        factor2 >>= 1

    return result


def power_mod(base: int, exponent: int, modulo: int = 0) -> Union[int, float]:
    """Performs a fast exponentiation of two numbers with modulo taken.

    :param base: a base value
    :param exponent: an exponent value
    :param modulo: a modulo value
    :return: exponentiation result with modulo taken"""
    result = 1

    if modulo < 0:
        raise ArithmeticError("Negative modulo")

    if exponent < 0:
        raise ArithmeticError("Negative exponent")

    if base == 0 and exponent == 0:
        return float('nan')

    while exponent > 0:
        if exponent % 2 == 1:
            result = mult_mod(base, result, modulo)

        base = mult_mod(base, base, modulo)
        exponent >>= 1

    return result
