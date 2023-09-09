# -*- coding: utf-8 -*-
"""Structure of linear equation system with Gauss elimination algorithm"""
from typing import List, Sequence

from .equation import Equation


class InfiniteSolutionsError(ValueError):
    pass


class NoSolutionError(ValueError):
    pass


class EquationSystem:
    def __init__(self, *equations: Equation):
        if any(len(eq) != len(equations) for eq in equations):
            raise ValueError("Incorrect number of variables in one of equations")

        self._equations = list(equations)

    def __repr__(self):
        return f"EquationSystem({', '.join(repr(eq) for eq in self._equations)})"

    def __str__(self):
        return f"{{ {' ; '.join(str(eq) for eq in self._equations)} }}"

    def __len__(self):
        """:return: number of equations in the system"""
        return len(self._equations)

    def __getitem__(self, i: int) -> Equation:
        """:param i: index of an equation
        :return: i-th equation of the system"""
        return self._equations[i]

    def __iter__(self):
        return iter(self._equations)

    def __reversed__(self):
        return reversed(self._equations)

    def solve(self) -> List[float]:
        """Computes the solution of the equation system.

        :return: solution vector
        :raises InfiniteSolutionsError: if there are infinitely many solutions
        :raises NoSolutionError: if there is no solution"""
        self.gaussian_reduce()

        if self[-1][-1] == 0 and self[-1].free == 0:
            raise InfiniteSolutionsError("Equation system has an infinite number of solutions")

        if self[-1][-1] == 0 and self[-1].free != 0:
            raise NoSolutionError("Equation system has no solution")

        solution = [0.0] * len(self)
        solution[-1] = self[-1].free / self[-1][-1]

        for i in range(-2, -len(self) - 1, -1):
            solution[i] = (self[i].free + sum(-self[i][j] * solution[j]
                                              for j in range(-1, i, -1))) / self[i][i]

        return solution

    def gaussian_reduce(self):
        """Runs the Gauss elimination algorithm on the equation system."""
        for i in range(len(self) - 1):
            index_min = i

            for j in range(i + 1, len(self)):
                min_coef = self[index_min][i]
                act_coef = self[j][i]

                if act_coef != 0 and (min_coef == 0 or abs(act_coef) < abs(min_coef)):
                    index_min = j

            if self[index_min][i] != 0:
                self.swap(index_min, i)

                for j in range(i + 1, len(self)):
                    param = self[j][i] / self[i][i]

                    if param != 0:
                        self._equations[j] += self[i] * -param

    def swap(self, i: int, j: int):
        """Swaps two equations in the system.

        :param i: index of first equation
        :param j: index of second equation"""
        self._equations[i], self._equations[j] = self._equations[j], self._equations[i]

    def has_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve the equation system.

        :param solution: values to check
        :return: ``true`` if solution is correct, otherwise ``false``"""
        return all(eq.has_solution(solution) for eq in self._equations)
