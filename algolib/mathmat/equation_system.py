# -*- coding: utf-8 -*-
"""Structure of linear equation system with Gauss elimination algorithm"""


class InfiniteSolutionsError(ValueError):
    pass


class NoSolutionError(ValueError):
    pass


class EquationSystem:
    def __init__(self, equations):
        self._equations = list(equations)

        if any(len(eq) != len(self._equations) for eq in self._equations):
            raise ValueError("Incorrect number of variables in one of equations")

    def __len__(self):
        """:return: number of equations"""
        return len(self._equations)

    def __getitem__(self, i):
        """:param i: index of equation
        :return: equation object"""
        return self._equations[i]

    def __iter__(self):
        return iter(self._equations)

    def __reversed__(self):
        return reversed(self._equations)

    def solve(self):
        """Computes the solution of this equation system
        :return: solution vector
        :raises NoSolutionError: if there is no solution
        :raises InfiniteSolutionsError: if there is infinitely many solutions"""
        self.gaussian_reduce()

        if self[-1][-1] == 0 and self[-1].free == 0:
            raise InfiniteSolutionsError()

        if self[-1][-1] == 0 and self[-1].free != 0:
            raise NoSolutionError()

        solution = [None] * self.__len__()
        solution[-1] = self[-1].free / self[-1][-1]

        for i in range(-2, -self.__len__() - 1, -1):
            solution[i] = sum((-self[i][j] * solution[j]
                               for j in range(-1, i, -1)), self[i].free) / self[i][i]

        return solution

    def gaussian_reduce(self):
        """Gauss elimination algorithm"""
        for i in range(self.__len__() - 1):
            index_min = i

            for j in range(i + 1, self.__len__()):
                min_coef = self[index_min][i]
                act_coef = self[j][i]

                if act_coef != 0 and (min_coef == 0 or abs(act_coef) < abs(min_coef)):
                    index_min = j

            if self[index_min][i] != 0:
                self.swap(index_min, i)

                for j in range(i + 1, self.__len__()):
                    param = self[j][i] / self[i][i]

                    if param != 0:
                        self[j].combine(self[i], -param)

    def swap(self, i, j):
        """Swaps two equations
        :param i: index of first equation
        :param j: index of second equation"""
        self._equations[i], self._equations[j] = self._equations[j], self._equations[i]

    def is_solution(self, solution):
        """Checks whether given values solve this equation system
        :param solution: values to check
        :return: ``true`` if solution is correct, otherwise ``false``"""
        return all(eq.is_solution(solution) for eq in self._equations)
