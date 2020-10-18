# -*- coding: utf-8 -*-
"""Tests: Structure of linear equations system """
import unittest

from algolib.mathmat import Equation, EquationSystem, InfiniteSolutionsError, NoSolutionError


class EquationSystemTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([-1, 6, 4], 9)])

    def tearDown(self):
        self.test_object = None

    def test__solve__when_single_solution__then_solution(self):
        result = self.test_object.solve()

        self.assertListEqual([1, 3, -2], result)
        self.assertTrue(self.test_object.is_solution(result))
        self.assertFalse(self.test_object.is_solution([-2, -18, -36.5]))

    def test__solve__when_no_solution__then_raise_no_solution_error(self):
        self.test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([-1, -1.5, 1], -1)])

        with self.assertRaises(NoSolutionError):
            self.test_object.solve()

        self.assertFalse(self.test_object.is_solution([1, 3, -2]))
        self.assertFalse(self.test_object.is_solution([-2, -18, -36.5]))

    def test__solve__when_infinite_solutions__then_raise_infinite_solutions_error(self):
        self.test_object = EquationSystem(
            [Equation([2, 3, -2], 15),
             Equation([7, -1, 0], 4),
             Equation([4, 6, -4], 30)])

        with self.assertRaises(InfiniteSolutionsError):
            self.test_object.solve()

        self.assertTrue(self.test_object.is_solution([1, 3, -2]))
        self.assertTrue(self.test_object.is_solution([-2, -18, -36.5]))
