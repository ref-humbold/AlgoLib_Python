# -*- coding: utf-8 -*-
"""Tests: Linear equations system structure"""
import unittest

from mathmat.equation import Equation


class EquationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = Equation([2, 3, -2], 15)

    def tearDown(self):
        self._test_object = None

    def test__imul__when_constant_is_non_zero__then_multiplied(self):
        self._test_object *= 2

        self.assertListEqual([4, 6, -4], self._test_object.coefficients)
        self.assertEqual(30, self._test_object.free)

    def test__imul__when_constant_is_zero__then_raise_value_error(self):
        with self.assertRaises(ValueError):
            self._test_object *= 0

    def test__combine__when_constant_is_non_zero__then_combined(self):
        self._test_object.combine(Equation([1, -1, 10], 5), -2)

        self.assertListEqual([0, 5, -22], self._test_object.coefficients)
        self.assertEqual(5, self._test_object.free)

    def test__combine__when_constant_is_zero__then_raise_value_error(self):
        with self.assertRaises(ValueError):
            self._test_object.combine(Equation([1, -1, 10], 5), 0)
