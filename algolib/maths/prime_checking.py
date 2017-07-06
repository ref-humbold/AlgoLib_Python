# -*- coding: utf-8 -*-
"""ALGORYTMY TESTOWANIA PIERWSZOŚCI"""
from random import randint
from .maths import gcd, power_mod


def fermat_prime(number):
    """Test pierwszości Fermata.
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number == 2 or number == 3:
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    for _ in range(12):
        rdv = randint(1, number - 1)

        if gcd(rdv, number) > 1 or power_mod(rdv, number - 1, number) != 1:
            return False

    return True


def miller_prime(number):
    """Test pierwszości Millera-Rabina.
    :param number: testowana liczba
    :returns: czy liczba prawdopodobnie jest pierwsza"""
    if number == 2 or number == 3:
        return True

    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    expon, multip = _distribute(number - 1)

    for _ in range(12):
        rdv = randint(1, number - 1)

        if power_mod(rdv, multip, number) != 1 and \
                all(power_mod(rdv, (1 << i) * multip, number) != number - 1 for i in range(expon)):
            return False

    return True


def _distribute(number):
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
