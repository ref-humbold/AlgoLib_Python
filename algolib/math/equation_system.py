# -*- coding: utf-8 -*-
"""LINEAR EQUATIONS SYSTEM WITH GAUSS ELIMINATION ALGORITHM"""


class InfiniteSolutionsException(ValueError):
    pass


class NoSolutionException(ValueError):
    pass


class EquationSystem:
    def __init__(self, numeq, coef=None, frees=None):
        EquationSystem.__validate(coef, frees, numeq)

        # Liczba równań układu.
        self.__equations = numeq
        # Macierz współczynników równania.
        self.__coeffs = coef if coef is not None \
            else [[0.0] * numeq for _ in range(numeq)]
        # Wektor wyrazów wolnych równania.
        self.__free_terms = frees if frees is not None else [0.0] * numeq

    def __len__(self):
        return self.__equations

    def solve(self):
        """Wyliczanie rozwiązań układu równań liniowych.
        :returns: wektor wyniku równania"""
        self.gaussian_reduce()

        if self.__coeffs[-1][-1] == 0 and self.__free_terms[-1] == 0:
            raise InfiniteSolutionsException()

        if self.__coeffs[-1][-1] == 0 and self.__free_terms[-1] != 0:
            raise NoSolutionException()

        solution = [None] * self.__equations
        solution[-1] = self.__free_terms[-1] / self.__coeffs[-1][-1]

        for equ in range(-2, -self.__equations - 1, -1):
            solution[equ] = sum((-self.__coeffs[equ][i] * solution[i] for i in range(-1, equ, -1)),
                                self.__free_terms[equ]) / self.__coeffs[equ][equ]

        return solution

    def gaussian_reduce(self):
        """Algorytm eliminacji Gaussa."""
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
        """Pomnożenie równania przez niezerową stałą.
        :param equ: numer równania
        :param constant: stała"""
        if constant == 0:
            raise ValueError("Constant cannot be zero")

        for i in range(self.__equations):
            self.__coeffs[equ][i] *= constant

        self.__free_terms[equ] *= constant

    def swap(self, equ1, equ2):
        """Zamiana równań miejscami.
        :param eq1: numer pierwszego równania
        :param eq2: numer drugiego równania"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i], self.__coeffs[equ2][i] = \
                self.__coeffs[equ2][i], self.__coeffs[equ1][i]

        self.__free_terms[equ1], self.__free_terms[equ2] = \
            self.__free_terms[equ2], self.__free_terms[equ1]

    def combine(self, equ1, equ2, constant):
        """Przekształcenie równania przez kombinację liniową z innym równaniem.
        :param eq1: numer równania przekształcanego
        :param eq2: numer drugiego równania
        :param constant: stała kombinacji liniowej"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i] += constant * self.__coeffs[equ2][i]

        self.__free_terms[equ1] += constant * self.__free_terms[equ2]

    @staticmethod
    def __validate(coef, frees, numeq):
        if coef is None and frees is None:
            return

        if coef is not None and frees is None \
           or coef is None and frees is not None:
            raise ValueError("Incorrect number of equations")

        if len(coef) != numeq or len(frees) != numeq:
            raise ValueError("Incorrect number of equations")

        if any(map(lambda e: len(e) != numeq, coef)):
            raise ValueError("Coefficient matrix is not a square matrix")
