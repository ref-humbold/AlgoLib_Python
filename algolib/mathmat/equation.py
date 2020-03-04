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
        return f"{' + '.join(f'{c} x_{i}' for i, c in enumerate(self.coefficients))} = {self.free}"

    def __len__(self):
        return len(self.coefficients)

    def __getitem__(self, i):
        return self.coefficients[i]

    def __mul__(self, constant):
        """Multiplies an equation by a constant
        :param constant: constant
        :raises ValueError: if the constant is zero"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(len(self)):
            self.coefficients[i] *= constant

        self.free *= constant

    def combine(self, equation, constant):
        """Transforms a equation through a linear combination with another equation
        :param equation: equation
        :param constant: linear combination constant"""
        for i in range(len(self)):
            self.coefficients[i] += constant * equation[i]

        self.free += constant * equation._free
