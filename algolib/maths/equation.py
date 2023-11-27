# -*- coding: utf-8 -*-
"""Structure of linear equation."""
from typing import Iterable, Sequence


class Equation:
    def __init__(self, coefficients: Iterable[float], free_term: float):
        self._coefficients = list(coefficients)
        self._free_term = free_term

    @property
    def coefficients(self):
        return self._coefficients

    @property
    def free_term(self):
        return self._free_term

    def __repr__(self):
        return f"Equation({self._coefficients!r}, {self._free_term!r})"

    def __str__(self):
        terms = [f"{c} x_{i}" for i, c in enumerate(self._coefficients) if c != 0]
        return f"{' + '.join(terms)} = {self._free_term}"

    def __len__(self):
        """Gets the number of variables in this equation.

        :return: the number of variables"""
        return len(self._coefficients)

    def __pos__(self):
        """Copies this equation

        :return: the copy of equation"""
        return Equation([+c for c in self._coefficients], +self._free_term)

    def __neg__(self):
        """Negates this equation.

        :return: the equation with all coefficients negated"""
        return Equation([-c for c in self._coefficients], -self._free_term)

    def __add__(self, equation: "Equation") -> "Equation":
        """Adds given equation to this equation.

        :param equation: the other equation
        :return: the equation with coefficients added
        :raise ValueError: if equations have different number of variables"""
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 + c2 for (c1, c2) in zip(self._coefficients, equation._coefficients)),
                        self._free_term + equation.free_term)

    def __iadd__(self, equation: "Equation"):
        """Adds given equation to this equation.

        :param equation: the other equation
        :return: ``self``
        :raise ValueError: if equations have different number of variables"""
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self._coefficients[i] += equation._coefficients[i]

        self._free_term += equation.free_term
        return self

    def __sub__(self, equation: "Equation") -> "Equation":
        """Subtracts given equation from this equation.

        :param equation: the other equation
        :return: the equation with coefficients subtracted
        :raise ValueError: if equations have different number of variable"""
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 - c2 for (c1, c2) in zip(self._coefficients, equation._coefficients)),
                        self._free_term - equation.free_term)

    def __isub__(self, equation: "Equation"):
        """Subtracts given equation from this equation.

        :param equation: the other equation
        :return: ``self``
        :raise ValueError: if equations have different number of variable"""
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self._coefficients[i] -= equation._coefficients[i]

        self._free_term -= equation.free_term
        return self

    def __mul__(self, constant: float) -> "Equation":
        """Multiplies this equation by given constant.

        :param constant: the constant
        :return: the equation with all coefficients multiplied
        :raise ArithmeticError: if constant is equal to zero"""
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        return Equation((c * constant for c in self._coefficients), self._free_term * constant)

    __rmul__ = __mul__

    def __imul__(self, constant: float):
        """Multiplies this equation by given constant.

        :param constant: the constant
        :return: ``self``
        :raise ArithmeticError: if constant is equal to zero"""
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self._coefficients[i] *= constant

        self._free_term *= constant
        return self

    def __truediv__(self, constant: float) -> "Equation":
        """Divides this equation by given constant.

        :param constant: the constant
        :return: the equation with all coefficients divided
        :raise ArithmeticError: if constant is equal to zero"""
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        return Equation((c / constant for c in self._coefficients), self._free_term / constant)

    __rtruediv__ = __truediv__

    def __itruediv__(self, constant: float):
        """Divides this equation by given constant.

        :param constant: the constant
        :return: ``self``
        :raise ArithmeticError: if constant is equal to zero"""
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self._coefficients[i] /= constant

        self._free_term /= constant
        return self

    def has_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve this equation.

        :param solution: the values
        :return: ``True`` if the solution is correct, otherwise ``False``"""
        return len(solution) == len(self) and \
            sum(map(lambda c, s: c * s, self._coefficients, solution)) == self._free_term
