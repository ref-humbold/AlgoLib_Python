# -*- coding: utf-8 -*-
"""Structure of linear equation sysytem with Gauss elimination algorithm"""


class InfiniteSolutionsError(ValueError):
    pass


class NoSolutionError(ValueError):
    pass


class EquationSystem:
    def __init__(self, numeq, coeffs=None, frees=None):
        EquationSystem._validate(coeffs, frees, numeq)
        self.__equations = numeq  # Number of equations
        self.__coeffs = coeffs if coeffs is not None \
            else [[0.0] * numeq for _ in range(numeq)]  # Coefficients matrix
        self.__frees = frees if frees is not None else [0.0] * numeq  # Free values vector

    def __len__(self):
        """:returns: number of equations"""
        return self.__equations

    def solve(self):
        """Counts the solution of this equation system
        :returns: solution vector
        :raises NoSolutionError: if there is no solution
        :raises InfiniteSolutionsError: if there is infinitely many solutions"""
        self.gaussian_reduce()

        if self.__coeffs[-1][-1] == 0 and self.__frees[-1] == 0:
            raise InfiniteSolutionsError()

        if self.__coeffs[-1][-1] == 0 and self.__frees[-1] != 0:
            raise NoSolutionError()

        solution = [None] * self.__equations
        solution[-1] = self.__frees[-1] / self.__coeffs[-1][-1]

        for equ in range(-2, -self.__equations - 1, -1):
            solution[equ] = sum((-self.__coeffs[equ][i] * solution[i] for i in range(-1, equ, -1)),
                                self.__frees[equ]) / self.__coeffs[equ][equ]

        return solution

    def gaussian_reduce(self):
        """Gauss elimination algorithm"""
        for equ in range(self.__equations - 1):
            index_min = equ

            for i in range(equ + 1, self.__equations):
                min_coef = self.__coeffs[index_min][equ]
                act_coef = self.__coeffs[i][equ]

                if act_coef != 0 and (min_coef == 0 or abs(act_coef) < abs(min_coef)):
                    index_min = i

            if self.__coeffs[index_min][equ] != 0:
                self.swap(index_min, equ)

                for i in range(equ + 1, self.__equations):
                    param = self.__coeffs[i][equ] / self.__coeffs[equ][equ]
                    self.combine(i, equ, -param)

    def multiply(self, equ, constant):
        """Multiplies an equation by a constant
        :param equ: index of equation
        :param constant: constant
        :raises ValueError: if the constant is zero"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(self.__equations):
            self.__coeffs[equ][i] *= constant

        self.__frees[equ] *= constant

    def swap(self, equ1, equ2):
        """Swaps two equations
        :param equ1: index of first equation
        :param equ2: index of second equation"""
        self.__coeffs[equ1], self.__coeffs[equ2] = self.__coeffs[equ2], self.__coeffs[equ1]
        self.__frees[equ1], self.__frees[equ2] = self.__frees[equ2], self.__frees[equ1]

    def combine(self, equ1, equ2, constant):
        """Transforms a equation through a linear combination with another equation
        :param equ1: index of equation to be transformed
        :param equ2: index of second equation
        :param constant: linear combination constant"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i] += constant * self.__coeffs[equ2][i]

        self.__frees[equ1] += constant * self.__frees[equ2]

    @staticmethod
    def _validate(coef, frees, numeq):
        if coef is None and frees is None:
            return

        if coef is None or frees is None:
            raise ValueError("Incorrect number of equations")

        if len(coef) != numeq or len(frees) != numeq:
            raise ValueError("Incorrect number of equations")

        if any(map(lambda e: len(e) != numeq, coef)):
            raise ValueError("Coefficient matrix is not a square matrix")
