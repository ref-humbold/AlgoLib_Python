# -*- coding: utf-8 -*-
"""Algorithms for basic mathematical computations"""
from typing import Optional, Union


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


def multiply(factor1: int, factor2: int, modulo: Optional[int] = None) -> int:
    """Performs a fast multiplication of two numbers.

    :param factor1: a first factor
    :param factor2: a second factor
    :param modulo: a modulo value
    :return: multiplication result"""
    result = 0

    if modulo is not None and modulo <= 0:
        raise ArithmeticError("Non-positive modulo")

    the_modulo = 0 if modulo is None else modulo

    if factor1 < 0 and factor2 < 0:
        return multiply(-factor1, -factor2, modulo)

    if factor1 < 0:
        return the_modulo - multiply(-factor1, factor2, modulo)

    if factor2 < 0:
        return the_modulo - multiply(factor1, -factor2, modulo)

    while factor2 > 0:
        if factor2 % 2 == 1:
            result = factor1 + result if modulo is None else (factor1 + result) % the_modulo

        factor1 = factor1 + factor1 if modulo is None else (factor1 + factor1) % the_modulo
        factor2 //= 2

    return result


def power(base: int, exponent: int, modulo: Optional[int] = None) -> Union[int, float]:
    """Performs a fast exponentiation of two numbers.

    :param base: a base value
    :param exponent: an exponent value
    :param modulo: a modulo value
    :return: exponentiation result"""
    result = 1

    if modulo is not None and modulo <= 0:
        raise ArithmeticError("Non-positive modulo")

    if exponent < 0:
        raise ArithmeticError("Negative exponent")

    if base == 0 and exponent == 0:
        return float('nan')

    while exponent > 0:
        if exponent % 2 == 1:
            result = multiply(base, result, modulo)

        base = multiply(base, base, modulo)
        exponent //= 2

    return result
