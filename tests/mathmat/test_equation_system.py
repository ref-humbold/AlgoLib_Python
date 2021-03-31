# -*- coding: utf-8 -*-
"""Tests: Structure of linear equations system """
import unittest

from algolib.mathmat import Equation, EquationSystem, InfiniteSolutionsError, NoSolutionError


class EquationSystemTest(unittest.TestCase):
    def test__solve__when_single_solution__then_solution(self):
        # given
        test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([-1, 6, 4], 9)])
        # when
        result = test_object.solve()
        # then
        self.assertListEqual([1, 3, -2], result)
        self.assertTrue(test_object.is_solution(result))
        self.assertFalse(test_object.is_solution([-2, -18, -36.5]))

    def test__solve__when_no_solution__then_raise_no_solution_error(self):
        # given
        test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([-1, -1.5, 1], -1)])
        # then
        with self.assertRaises(NoSolutionError):
            # when
            test_object.solve()
        # then
        self.assertFalse(test_object.is_solution([1, 3, -2]))
        self.assertFalse(test_object.is_solution([-2, -18, -36.5]))

    def test__solve__when_infinite_solutions__then_raise_infinite_solutions_error(self):
        # given
        test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([4, 6, -4], 30)])
        # then
        with self.assertRaises(InfiniteSolutionsError):
            # when
            test_object.solve()
        # then
        self.assertTrue(test_object.is_solution([1, 3, -2]))
        self.assertTrue(test_object.is_solution([-2, -18, -36.5]))
