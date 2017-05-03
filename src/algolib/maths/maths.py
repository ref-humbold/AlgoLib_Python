# -*- coding: utf-8 -*-
"""ALGORYTMY MATEMATYCZNE"""
def gcd(number1, number2):
    """Największy wspólny dzielnik dwóch liczb.
    :param number1: pierwsza liczba
    :param number2: druga liczba
    :returns: największy wspólny dzielnik"""
    number_pair = (min(number1, number2), max(number1, number2))

    while number_pair[0] > 0:
        number_pair = (number_pair[1]%number_pair[0], number_pair[0])

    return number_pair[1]


def lcm(number1, number2):
    """Najmniejsza wspólna wielokrotność dwóch liczb.
    :param number1: pierwsza liczba
    :param number2: druga liczba
    :returns: najmniejsza wspólna wielokrotność"""
    min_number = min(number1, number2)
    max_number = max(number1, number2)

    return max_number//gcd(number1, number2)*min_number


def power(base, exponent, modulo=0):
    """Szybkie potęgowanie binarne modulowane.
    :param base: podstawa
    :param exponent: wykładnik
    :param modulo: modulo
    :returns: wynik potęgowania"""
    result = 1

    while exponent > 0:
        if (exponent&1) == 1:
            result = mult(result, base, modulo)

        base = mult(base, base, modulo)
        exponent >>= 1

    return result


def mult(factor1, factor2, modulo=0):
    """Szybkie mnożenie binarne modulowane.
    :param factor1: pierwszy czynnik
    :param factor2: drugi czynnik
    :param modulo: modulo
    :returns: wynik mnożenia wzięty modulo"""
    result = 0

    while factor2 > 0:
        if (factor2&1) == 1:
            result = result+factor1 if modulo == 0 else (result+factor1)%modulo

        factor2 >>= 1
        factor1 = factor1+factor1 if modulo == 0 else (factor1+factor1)%modulo

    return result
