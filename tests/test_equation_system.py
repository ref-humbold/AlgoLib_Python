# -*- coding: utf-8 -*-
"""Tests for linear equations system structure"""
import unittest
from algolib.math import EquationSystem, NoSolutionException, InfiniteSolutionsException


class EquationSystemTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__test_object = None

    def setUp(self):
        self.__test_object = EquationSystem(3, [[2, 3, -2], [7, -1, 0], [-1, 6, 4]], [15, 4, 9])

    def tearDown(self):
        self.__test_object = None

    def test_mult_when_constant_is_zero(self):
        constant = 0

        with self.assertRaises(ValueError):
            self.__test_object.mult(0, constant)

    def test_solve_when_single_solution(self):
        result = self.__test_object.solve()

        self.assertListEqual([1, 3, -2], result)

    def test_solve_when_no_solution(self):
        self.__test_object = EquationSystem(
            3, [[2, 3, -2], [7, -1, 0], [-1, -1.5, 1]], [15, 4, -1])

        with self.assertRaises(NoSolutionException):
            self.__test_object.solve()

    def test_solve_when_infinite_solutions(self):
        self.__test_object = EquationSystem(3, [[2, 3, -2], [7, -1, 0], [4, 6, -4]], [15, 4, 30])

        with self.assertRaises(InfiniteSolutionsException):
            self.__test_object.solve()
