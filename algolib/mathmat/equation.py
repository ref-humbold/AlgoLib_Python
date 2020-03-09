# -*- coding: utf-8 -*-
"""Structure of linear equation"""


class Equation:
    def __init__(self, coefficients, free):
        self.coefficients = list(coefficients)
        self.free = free

    @property
    def values(self):
        return self.coefficients, self.free

    def __str__(self):
        vars = [f'{c} x_{i}' for i, c in enumerate(self.coefficients) if c != 0]
        return f"{' + '.join(vars)} = {self.free}"

    def __len__(self):
        """:returns: number of variables"""
        return len(self.coefficients)

    def __getitem__(self, i):
        """:param i: index of a variable
        :returns: coefficient by i-th variable"""
        return self.coefficients[i]

    def __imul__(self, constant):
        """Multiplies equation by a constant
        :param constant: constant
        :raises ValueError: if the constant is zero"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(len(self)):
            self.coefficients[i] *= constant

        self.free *= constant
        return self

    def combine(self, equation, constant=1):
        """Transforms equation through a linear combination with another equation
        :param equation: equation
        :param constant: linear combination constant
        :raises ValueError: if the constant is zero"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(len(self)):
            self.coefficients[i] += constant * equation[i]

        self.free += constant * equation.free