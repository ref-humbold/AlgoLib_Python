# -*- coding: utf-8 -*-
"""Structure of fraction"""
from .maths import gcd


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        self._numerator = numerator
        self._denominator = denominator
        self._normalize()

    def __hash__(self):
        return hash((self._numerator, self._denominator))

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __float__(self):
        return self._numerator / self._denominator

    def __int__(self):
        return self._numerator // self._denominator

    def __bool__(self):
        return self._numerator != 0

    def __eq__(self, frac: "Fraction"):
        return self._numerator == frac._numerator and self._denominator == frac._denominator

    def __ne__(self, frac: "Fraction"):
        return not self == frac

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __invert__(self):
        if self._numerator == 0:
            raise ArithmeticError("Inverting zero")

        return Fraction(self._denominator, self._numerator)

    def __abs__(self):
        return Fraction(abs(self._numerator), self._denominator)

    def _normalize(self):
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

            gcd_val = gcd(self._numerator, self._denominator)

            self._numerator /= gcd_val
            self._denominator /= gcd_val
