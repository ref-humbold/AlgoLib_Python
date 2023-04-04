# -*- coding: utf-8 -*-
"""Structure of linear equation"""
from typing import Iterable, Sequence


class Equation:
    def __init__(self, coefficients: Iterable[float], free: float):
        self.coefficients = list(coefficients)
        self.free = free

    def __repr__(self):
        return f"Equation({self.coefficients!r}, {self.free!r})"

    def __str__(self):
        terms = [f"{c} x_{i}" for i, c in enumerate(self.coefficients) if c != 0]
        return f"{' + '.join(terms)} = {self.free}"

    def __len__(self):
        """:returns: number of variables in the equation"""
        return len(self.coefficients)

    def __getitem__(self, i: int) -> float:
        """:param i: index of a variable
        :returns: coefficient by i-th variable"""
        return self.coefficients[i]

    def __add__(self, equation: "Equation") -> "Equation":
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 + c2 for (c1, c2) in zip(self.coefficients, equation.coefficients)),
                        self.free + equation.free)

    def __iadd__(self, equation: "Equation"):
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self.coefficients[i] += equation[i]

        self.free += equation.free
        return self

    def __sub__(self, equation: "Equation") -> "Equation":
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        return Equation((c1 - c2 for (c1, c2) in zip(self.coefficients, equation.coefficients)),
                        self.free - equation.free)

    def __isub__(self, equation: "Equation"):
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        for i in range(len(self)):
            self.coefficients[i] -= equation[i]

        self.free -= equation.free
        return self

    def __mul__(self, constant: float) -> "Equation":
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        return Equation((c * constant for c in self.coefficients), self.free * constant)

    __rmul__ = __mul__

    def __imul__(self, constant: float):
        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self.coefficients[i] *= constant

        self.free *= constant
        return self

    def __truediv__(self, constant: float) -> "Equation":
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        return Equation((c / constant for c in self.coefficients), self.free / constant)

    __rtruediv__ = __truediv__

    def __itruediv__(self, constant: float):
        if constant == 0:
            raise ZeroDivisionError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self.coefficients[i] /= constant

        self.free /= constant
        return self

    def combine(self, equation: "Equation", constant: float):
        """Transforms equation through a linear combination with another equation.

        :param equation: equation
        :param constant: linear combination constant
        :raises ValueError: if equations sizes differ
        :raises ArithmeticError: if the constant is equal to zero"""
        if len(equation) != len(self):
            raise ValueError("Equation has different number of variables")

        if constant == 0:
            raise ArithmeticError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self.coefficients[i] += constant * equation[i]

        self.free += constant * equation.free

    def is_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve the equation.

        :param solution: values to check
        :return: ``true`` if solution is correct, otherwise ``false``"""
        return len(solution) == len(self) and sum(
                map(lambda c, s: c * s, self.coefficients, solution)) == self.free
