# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic geometrical computations in 2D"""
import unittest

from algolib.geometry.dim2 import Point2D, sorted_by_angle, sorted_by_x, sorted_by_y


class Geometry2DTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__sorted_by_x__when_list__then_new_stably_sorted_list_ascending_by_x_coordinate(self):
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0)]
        # when
        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point2D(-3.0, 2.0), Point2D(-3.0, -2.0), Point2D(-2.0, -3.0),
                              Point2D(-2.0, 3.0), Point2D(0.0, 0.0), Point2D(2.0, 3.0),
                              Point2D(2.0, -3.0), Point2D(3.0, -2.0), Point2D(3.0, 2.0)], result)

    def test__sorted_by_y__when_tuple__then_new_stably_sorted_list_ascending_by_y_coordinate(self):
        # given
        sequence = (Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0))
        # when
        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([Point2D(-2.0, -3.0), Point2D(2.0, -3.0), Point2D(3.0, -2.0),
                              Point2D(-3.0, -2.0), Point2D(0.0, 0.0), Point2D(-3.0, 2.0),
                              Point2D(3.0, 2.0), Point2D(2.0, 3.0), Point2D(-2.0, 3.0)], result)

    def test__sorted_by_angle__then_new_sorted_list(self):
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        # when
        result = sorted_by_angle(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point2D(0, 0), Point2D(3, 2), Point2D(2, 3), Point2D(-2, 3),
                              Point2D(-3, 2), Point2D(-3, -2), Point2D(-2, -3), Point2D(2, -3),
                              Point2D(3, -2)], result)
