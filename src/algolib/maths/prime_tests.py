# -*- coding: utf-8 -*-
"""ALGORYTMY TESTOWANIA PIERWSZOŚCI"""
from random import randint
from .maths import gcd, iter_power

def fermat_test(number):
    """Test pierwszości Fermata.
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number == 2 or number == 3:
        return True

    if number < 2 or number %2 == 0 or number%3 == 0:
        return False

    for _ in range(10):
        rdval = randint(2, number - 2)

        if gcd(rdval, number) > 1 or iter_power(rdval, number - 1, number) != 1:
            return False

    return True


def miller_test(number):
    """Test pierwszości Millera-Rabina.
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number == 2 or number == 3:
        return True

    if number < 2 or number %2 == 0 or number%3 == 0:
        return False

    expon, multip = distribute(number-1)

    for _ in range(10):
        rdval = randint(2, number - 2)

        if iter_power(rdval, multip, number) != 1:
            for i in range(expon):
                if iter_power(rdval, (1 << i) * multip, number) == number - 1:
                    return False

    return True


def distribute(number):
    """Rozkładanie liczby do testu Millera-Rabina.
    :param number: rozkładana liczba
    :returns: rozkład liczby"""
    power = 2
    expon = 1

    while number % power == 0:
        expon += 1
        power <<= 1

    expon -= 1

    return expon, number // (1 << expon)
