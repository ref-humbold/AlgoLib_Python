# -*- coding: utf-8 -*-
"""Tests: Structure of linear equations system """
import unittest

from assertpy import assert_that

from algolib.maths import Equation, EquationSystem, InfiniteSolutionsError, NoSolutionError


class EquationSystemTest(unittest.TestCase):
    @staticmethod
    def test__solve__when_single_solution__then_solution():
        # given
        test_object = EquationSystem(Equation([2, 3, -2], 15), Equation([7, -1, 0], 4),
                                     Equation([-1, 6, 4], 9))
        # when
        result = test_object.solve()
        # then
        assert_that(result).is_equal_to([1, 3, -2])
        assert_that(test_object.has_solution(result)).is_true()
        assert_that(test_object.has_solution([-2, -18, -36.5])).is_false()

    @staticmethod
    def test__solve__when_no_solution__then_raise_no_solution_error():
        # given
        test_object = EquationSystem(Equation([2, 3, -2], 15), Equation([7, -1, 0], 4),
                                     Equation([-1, -1.5, 1], -1))

        # when
        def function():
            test_object.solve()

        # then
        assert_that(function).raises(NoSolutionError)
        assert_that(test_object.has_solution([1, 3, -2])).is_false()
        assert_that(test_object.has_solution([-2, -18, -36.5])).is_false()

    @staticmethod
    def test__solve__when_infinite_solutions__then_raise_infinite_solutions_error():
        # given
        test_object = EquationSystem(Equation([2, 3, -2], 15), Equation([7, -1, 0], 4),
                                     Equation([4, 6, -4], 30))

        # when
        def function():
            test_object.solve()

        # then
        assert_that(function).raises(InfiniteSolutionsError)
        assert_that(test_object.has_solution([1, 3, -2])).is_true()
        assert_that(test_object.has_solution([-2, -18, -36.5])).is_true()

    @staticmethod
    def test__swap__then_equations_swapped():
        # given
        test_object = EquationSystem(Equation([2, 3, -2], 15), Equation([7, -1, 0], 4),
                                     Equation([-1, 6, 4], 9))
        # when
        test_object.swap(0, 2)
        # then
        assert_that(str(test_object[0])).is_equal_to("-1 x_0 + 6 x_1 + 4 x_2 = 9")
        assert_that(str(test_object[2])).is_equal_to("2 x_0 + 3 x_1 + -2 x_2 = 15")
