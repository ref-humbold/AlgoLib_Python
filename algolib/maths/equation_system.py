# -*- coding: utf-8 -*-
"""Structure of system of linear equations."""
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
        """Gets the number of equations in this system.

        :return: the number of equations"""
        return len(self._equations)

    def __getitem__(self, i: int) -> Equation:
        """Gets the equation at given index.

        :param i: the index of equation
        :return: the equation of this system specified by the index"""
        return self._equations[i]

    def __iter__(self):
        return iter(self._equations)

    def __reversed__(self):
        return reversed(self._equations)

    def solve(self) -> List[float]:
        """Computes solution of this equation system.

        :return: the solution
        :raises InfiniteSolutionsError: if there are infinitely many solutions
        :raises NoSolutionError: if there is no solution"""
        self.gaussian_reduce()

        if self[-1].coefficients[-1] == 0 and self[-1].free_term == 0:
            raise InfiniteSolutionsError("Equation system has an infinite number of solutions")

        if self[-1].coefficients[-1] == 0 and self[-1].free_term != 0:
            raise NoSolutionError("Equation system has no solution")

        solution = [0.0] * len(self)
        solution[-1] = self[-1].free_term / self[-1].coefficients[-1]

        for i in range(-2, -len(self) - 1, -1):
            solution[i] = (self[i].free_term + sum(-self[i].coefficients[j] * solution[j]
                                                   for j in range(-1, i, -1))) / \
                          self[i].coefficients[i]

        return solution

    def gaussian_reduce(self):
        """Runs the Gaussian elimination algorithm on this equation system."""
        for i in range(len(self) - 1):
            index_min = self._min_coefficient_index(i)

            if self[index_min].coefficients[i] != 0:
                self.swap(index_min, i)

                for j in range(i + 1, len(self)):
                    param = self[j].coefficients[i] / self[i].coefficients[i]

                    if param != 0:
                        self._equations[j] += self[i] * -param

    def swap(self, i: int, j: int):
        """Swaps two equations in this system.

        :param i: the index of the first equation
        :param j: the index of the second equation"""
        self._equations[i], self._equations[j] = self._equations[j], self._equations[i]

    def has_solution(self, solution: Sequence[float]) -> bool:
        """Checks whether given values solve this equation system.

        :param solution: the values
        :return: ``True`` if the solution is correct, otherwise ``False``"""
        return all(eq.has_solution(solution) for eq in self._equations)

    def _min_coefficient_index(self, starting_index):
        index_min = starting_index
        for j in range(starting_index + 1, len(self)):
            min_coefficient = self[index_min].coefficients[starting_index]
            current_coefficient = self[j].coefficients[starting_index]

            if current_coefficient != 0 and (min_coefficient == 0
                                             or abs(current_coefficient) < abs(min_coefficient)):
                index_min = j
        return index_min
