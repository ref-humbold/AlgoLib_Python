# -*- coding: utf-8 -*-
"""Structure of linear equation"""
from typing import Iterable, Sequence


class Equation:
    def __init__(self, coefficients: Iterable[float], free: float):
        self.coefficients = list(coefficients)
        self.free = free

    def __str__(self):
        """:return: string representation of the equation"""
        terms = [f'{c} x_{i}' for i, c in enumerate(self.coefficients) if c != 0]
        return f"{' + '.join(terms)} = {self.free}"

    def __len__(self):
        """:returns: number of variables"""
        return len(self.coefficients)

    def __getitem__(self, i: int) -> float:
        """:param i: index of a variable
        :returns: coefficient by i-th variable"""
        return self.coefficients[i]

    def __imul__(self, constant: float):
        """Multiplies equation by a constant.

        :param constant: constant
        :raises ValueError: if the constant is equal to zero"""
        if constant == 0:
            raise ValueError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self.coefficients[i] *= constant

        self.free *= constant
        return self

    def combine(self, equation: "Equation", constant: float = 1) -> None:
        """Transforms equation through a linear combination with another equation.

        :param equation: equation
        :param constant: linear combination constant
        :raises ValueError: if the constant is equal to zero or equations sizes differ"""
        if len(equation) != self.__len__():
            raise ValueError("Equation has different number of variables")

        if constant == 0:
            raise ValueError("Constant cannot be equal to zero")

        for i in range(len(self)):
            self.coefficients[i] += constant * equation[i]

        self.free += constant * equation.free

    def is_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve the equation.

        :param solution: values to check
        :return: ``true`` if solution is correct, otherwise ``false``"""
        return len(solution) == len(self) and sum(
            map(lambda c, s: c * s, self.coefficients, solution)) == self.free
