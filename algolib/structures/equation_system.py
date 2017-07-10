# -*- coding: utf-8 -*-
"""STRUKTURA UKŁADÓW RÓWNAŃ LINIOWYCH Z ALGORYTMEM ELIMINACJI GAUSSA"""


class InfiniteSolutionsException(ValueError):
    pass


class NoSolutionException(ValueError):
    pass


class EquationSystem:
    def __init__(self, numeq):
        # Liczba równań układu.
        self.__equations = numeq
        # Macierz współczynników równania.
        self.__coeffs = [[0.0] * numeq for i in range(numeq)]
        # Wektor wyrazów wolnych równania.
        self.__free_terms = [0.0] * numeq

    @property
    def equations_number(self):
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
                self.change(index_min, equ)

                for i in range(equ + 1, self.__equations):
                    param = self.__coeffs[i][equ] / self.__coeffs[equ][equ]
                    self.linear_comb(i, equ, -param)

    def change(self, equ1, equ2):
        """Zamiana równań miejscami.
        :param eq1: numer pierwszego równania
        :param eq2: numer drugiego równania"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i], self.__coeffs[equ2][i] = \
                self.__coeffs[equ2][i], self.__coeffs[equ1][i]

        self.__free_terms[equ1], self.__free_terms[equ2] = \
            self.__free_terms[equ2], self.__free_terms[equ1]

    def linear_comb(self, equ1, equ2, constant):
        """Przekształcenie równania przez kombinację liniową z innym równaniem.
        :param eq1: numer równania przekształcanego
        :param eq2: numer drugiego równania
        :param constant: stała kombinacji liniowej"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i] += constant * self.__coeffs[equ2][i]

        self.__free_terms[equ1] += constant * self.__free_terms[equ2]
