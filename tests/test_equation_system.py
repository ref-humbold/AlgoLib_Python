# -*- coding: utf-8 -*-
"""Tests: Linear equations system structure"""
import unittest

from algolib.mathmat import EquationSystem, InfiniteSolutionsError, \
    NoSolutionError


class EquationSystemTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = EquationSystem(3, [[2, 3, -2], [7, -1, 0], [-1, 6, 4]], [15, 4, 9])

    def tearDown(self):
        self._test_object = None

    def test__mult__when_constant_is_zero__then_raise_value_error(self):
        constant = 0

        with self.assertRaises(ValueError):
            self._test_object.mult(0, constant)

    def test__solve__when_single_solution__then_solution(self):
        result = self._test_object.solve()

        self.assertListEqual([1, 3, -2], result)

    def test__solve__when_no_solution__then_raise_no_solution_error(self):
        self._test_object = EquationSystem(
            3, [[2, 3, -2], [7, -1, 0], [-1, -1.5, 1]], [15, 4, -1])

        with self.assertRaises(NoSolutionError):
            self._test_object.solve()

    def test__solve__when_infinite_solutions__then_raise_infinite_solutions_error(self):
        self._test_object = EquationSystem(3, [[2, 3, -2], [7, -1, 0], [4, 6, -4]], [15, 4, 30])

        with self.assertRaises(InfiniteSolutionsError):
            self._test_object.solve()
