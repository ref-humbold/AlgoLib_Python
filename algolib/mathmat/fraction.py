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

    def __bool__(self):
        return self._numerator != 0

    def __int__(self):
        return self._numerator // self._denominator

    def __float__(self):
        return self._numerator / self._denominator

    def __eq__(self, frac: "Fraction"):
        return self._numerator == frac._numerator and self._denominator == frac._denominator

    def __ne__(self, frac: "Fraction"):
        return not self == frac

    def __add__(self, frac: "Fraction") -> "Fraction":
        pass

    def __iadd__(self, frac: "Fraction"):
        pass

    def __sub__(self, frac: "Fraction") -> "Fraction":
        pass

    def __isub__(self, frac: "Fraction"):
        pass

    def __mul__(self, frac: "Fraction") -> "Fraction":
        return Fraction(self._numerator * frac._numerator, self._denominator * frac._denominator)

    def __imul__(self, frac: "Fraction"):
        self._numerator *= frac._numerator
        self._denominator *= frac._denominator
        self._normalize()
        return self

    def __truediv__(self, frac: "Fraction") -> "Fraction":
        if frac._numerator == 0:
            raise ZeroDivisionError()

        return Fraction(self._numerator * frac._denominator, self._denominator * frac._numerator)

    def __itruediv__(self, frac: "Fraction"):
        self._numerator *= frac._denominator
        self._denominator *= frac._numerator
        self._normalize()
        return self

    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __abs__(self) -> "Fraction":
        return Fraction(abs(self._numerator), self._denominator)

    def __invert__(self) -> "Fraction":
        if self._numerator == 0:
            raise ArithmeticError("Inverting zero")

        return Fraction(self._denominator, self._numerator)

    def _normalize(self):
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

            gcd_val = gcd(self._numerator, self._denominator)

            self._numerator /= gcd_val
            self._denominator /= gcd_val
