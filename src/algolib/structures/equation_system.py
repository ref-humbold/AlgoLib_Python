# -*- coding: utf-8 -*-
"""STRUKTURA UKŁADÓW RÓWNAŃ LINIOWYCH Z ALGORYTMEM ELIMINACJI GAUSSA"""
class EquationSystem:
    def __init__(self, numeq):
        self.__equations = numeq    # liczba równań układu
        self.__coeffs = [[0.0] * numeq for i in range(numeq)]    # macierz współczynników równania
        self.__free_terms = [0.0] * numeq    # wektor wyrazów wolnych równania

    def equation(self):
        """Getter dla układu równań
        :returns: macierz układu i wektor wyrazów wolnych"""
        return self.__coeffs, self.__free_terms

    def solve(self):
        """Wyliczanie rozwiązań układu równań liniowych.
        :returns: wektor wyniku równania"""
        self.gaussian_reduce()

        if self.__coeffs[-1][-1] == 0 and self.__free_terms[-1] == 0:
            raise Exception("System of equations has got infinitely many solutions.")

        if self.__coeffs[-1][-1] == 0 and self.__free_terms[-1] != 0:
            raise Exception("System of equations has got no solution.")

        solution = [self.__free_terms[-1] / self.__coeffs[-1][-1]]

        for equ in range(-2, -self.__equations-1, -1):
            value = self.__free_terms[equ]

            for i, sol in enumerate(solution):
                value -= self.__coeffs[equ][-1 - i]*sol

            solution.append(value / self.__coeffs[equ][equ])

        solution.reverse()

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
                self.__change(index_min, equ)

                for i in range(equ+1, self.__equations):
                    param = self.__coeffs[i][equ] / self.__coeffs[equ][equ]
                    self.__linear_comb(i, equ, -param)

    def __change(self, equ1, equ2):
        """Zamiana równań miejscami.
        :param eq1: numer pierwszego równania
        :param eq2: numer drugiego równania"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i], self.__coeffs[equ2][i] = \
                self.__coeffs[equ2][i], self.__coeffs[equ1][i]

        self.__free_terms[equ1], self.__free_terms[equ2] = \
            self.__free_terms[equ2], self.__free_terms[equ1]

    def __linear_comb(self, equ1, equ2, cst):
        """Przekształcenie równania przez kombinację liniową z innym równaniem.
        :param eq1: numer równania przekształcanego
        :param eq2: numer drugiego równania
        :param cst: stała kombinacji liniowej"""
        for i in range(self.__equations):
            self.__coeffs[equ1][i] += cst * self.__coeffs[equ2][i]

        self.__free_terms[equ1] += cst * self.__free_terms[equ2]
