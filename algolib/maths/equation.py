# -*- coding: utf-8 -*-
"""Structure of linear equation"""
from typing import Iterable, Sequence


class Equation:
    def __init__(self, coefficients: Iterable[float], free: float):
        self._coefficients = list(coefficients)
        self._free = free

    @property
    def free(self):
        return self._free

    def __repr__(self):
        return f"Equation({self._coefficients!r}, {self._free!r})"

    def __str__(self):
        terms = [f"{c} x_{i}" for i, c in enumerate(self._coefficients) if c != 0]
        return f"{' + '.join(terms)} = {self._free}"

    def __len__(self):
        """:returns: number of variables in the equation"""
        return len(self._coefficients)

    def __getitem__(self, i: int) -> float:
        """:param i: index of a variable
        :returns: coefficient by i-th variable"""
        return self._coefficients[i]

    def __pos__(self):
        return Equation([+c for c in self._coefficients], +self._free)

    def __neg__(self):
        return Equation([-c for c in self._coefficients], -self._free)

    def __add__(self, equation: "Equation") -> "Equation":
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 + c2 for (c1, c2) in zip(self._coefficients, equation._coefficients)),
                        self._free + equation.free)

    def __iadd__(self, equation: "Equation"):
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self._coefficients[i] += equation[i]

        self._free += equation.free
        return self

    def __sub__(self, equation: "Equation") -> "Equation":
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 - c2 for (c1, c2) in zip(self._coefficients, equation._coefficients)),
                        self._free - equation.free)

    def __isub__(self, equation: "Equation"):
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self._coefficients[i] -= equation[i]

        self._free -= equation.free
        return self

    def __mul__(self, constant: float) -> "Equation":
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        return Equation((c * constant for c in self._coefficients), self._free * constant)

    __rmul__ = __mul__

    def __imul__(self, constant: float):
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self._coefficients[i] *= constant

        self._free *= constant
        return self

    def __truediv__(self, constant: float) -> "Equation":
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        return Equation((c / constant for c in self._coefficients), self._free / constant)

    __rtruediv__ = __truediv__

    def __itruediv__(self, constant: float):
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self._coefficients[i] /= constant

        self._free /= constant
        return self

    def has_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve the equation.

        :param solution: values to check
        :return: ``true`` if solution is correct, otherwise ``false``"""
        return len(solution) == len(self) and \
            sum(map(lambda c, s: c * s, self._coefficients, solution)) == self._free
