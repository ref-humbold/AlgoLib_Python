# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic geometrical computations in 2D"""
import unittest

from algolib.geometry.dim2 import Point2D, Vector2D, distance, sorted_by_angle, sorted_by_x, \
    sorted_by_y, translate


class Geometry2DTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__sorted_by_x__when_list__then_new_list_sorted_stably_ascending(self):
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0)]
        # when
        result = sorted_by_x(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point2D(-3.0, 2.0), Point2D(-3.0, -2.0), Point2D(-2.0, -3.0),
                              Point2D(-2.0, 3.0), Point2D(0.0, 0.0), Point2D(2.0, 3.0),
                              Point2D(2.0, -3.0), Point2D(3.0, -2.0), Point2D(3.0, 2.0)], result)

    def test__sorted_by_y__when_tuple__then_new_list_sorted_stably_ascending(self):
        # given
        sequence = (Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0))
        # when
        result = sorted_by_y(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertListEqual([Point2D(-2.0, -3.0), Point2D(2.0, -3.0), Point2D(3.0, -2.0),
                              Point2D(-3.0, -2.0), Point2D(0.0, 0.0), Point2D(-3.0, 2.0),
                              Point2D(3.0, 2.0), Point2D(2.0, 3.0), Point2D(-2.0, 3.0)], result)

    def test__sorted_by_angle__then_new_list_sorted_ascending(self):
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        # when
        result = sorted_by_angle(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point2D(0, 0), Point2D(3, 2), Point2D(2, 3), Point2D(-2, 3),
                              Point2D(-3, 2), Point2D(-3, -2), Point2D(-2, -3), Point2D(2, -3),
                              Point2D(3, -2)], result)

    def test__sorted_by_angle__when_equal_angles__then_compare_radius(self):
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(1.0, 1.0), Point2D(-2.0, -2.0), Point2D(-3.0, -3.0),
                    Point2D(4.0, 4.0)]
        # when
        result = sorted_by_angle(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point2D(0.0, 0.0), Point2D(1.0, 1.0), Point2D(4.0, 4.0),
                              Point2D(-2.0, -2.0), Point2D(-3.0, -3.0)], result)

    def test__distance__when_different_points__then_distance(self):
        # when
        result = distance(Point2D(4.0, 5.0), Point2D(-2.0, -3.0))
        # then
        self.assertEqual(10.0, result)

    def test__distance__when_same_point__then_zero(self):
        # given
        point = Point2D(13.5, 6.5)
        # when
        result = distance(point, point)
        # then
        self.assertEqual(0.0, result)

    def test__translate__then_point_translated(self):
        # when
        result = translate(Point2D(13.7, 6.5), Vector2D(-10.4, 3.3))
        # then
        self.assertEqual(Point2D(3.3, 9.8), result)

    def test__translate__when_zero_vector__then_same_point(self):
        # given
        point = Point2D(13.5, 6.5)
        # when
        result = translate(point, Vector2D(0.0, 0.0))
        # then
        self.assertEqual(point, result)
