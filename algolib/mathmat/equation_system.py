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
        # Coefficients matrix
        self.__coeffs = coeffs if coeffs is not None else [[0.0] * numeq for _ in range(numeq)]
        self.__frees = frees if frees is not None else [0.0] * numeq  # Free values vector

    def __len__(self):
        return self.__equations

    def solve(self):
        """Wyliczanie rozwiązań układu równań liniowych
        :returns: wektor wyniku równania"""
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

    def mult(self, equ, constant):
        """Pomnożenie równania przez niezerową stałą
        :param equ: numer równania
        :param constant: stała"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(self.__equations):
            self.__coeffs[equ][i] *= constant

        self.__frees[equ] *= constant

    def swap(self, equ1, equ2):
        """Zamiana równań miejscami
        :param equ1: numer pierwszego równania
        :param equ2: numer drugiego równania"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i], self.__coeffs[equ2][i] = \
                self.__coeffs[equ2][i], self.__coeffs[equ1][i]

        self.__frees[equ1], self.__frees[equ2] = self.__frees[equ2], self.__frees[equ1]

    def combine(self, equ1, equ2, constant):
        """Przekształcenie równania przez kombinację liniową z innym równaniem
        :param equ1: numer równania przekształcanego
        :param equ2: numer drugiego równania
        :param constant: stała kombinacji liniowej"""
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
