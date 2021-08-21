# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic geometrical computations in 3D"""
import unittest

from algolib.geometry.dim3 import Point3D, Vector3D, distance, sorted_by_x, sorted_by_y, \
    sorted_by_z, translate


class Geometry3DTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__sorted_by_x__when_tuple__then_new_list_sorted_stably_ascending(self):
        # given
        sequence = (Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0))
        # when
        result = sorted_by_x(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertListEqual([Point3D(-3.0, 2.0, 5.0), Point3D(-2.0, -3.0, 5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(3.0, 2.0, 5.0)], result)

    def test__sorted_by_y__when_list__then_new_list_sorted_stably_ascending(self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_y(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point3D(-2.0, -3.0, 5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(3.0, 2.0, 5.0), Point3D(-3.0, 2.0, 5.0),
                              Point3D(2.0, 3.0, -5.0)], result)

    def test__sorted_by_z__when_list__then_new_list_sorted_stably_ascending(self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_z(sequence)
        # then
        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(-2.0, -3.0, 5.0), Point3D(3.0, 2.0, 5.0),
                              Point3D(-3.0, 2.0, 5.0)], result)

    def test__distance__when_different_points__then_distance(self):
        # when
        result = distance(Point3D(4.0, 8.0, 5.0), Point3D(-2.0, -1.0, 3.0))
        # then
        self.assertEqual(11.0, result)

    def test__distance__when_same_point__then_zero(self):
        # given
        point = Point3D(13.5, 6.5, -4.2)
        # when
        result = distance(point, point)
        # then
        self.assertEqual(0.0, result)

    def test__translate__then_point_translated(self):
        # when
        result = translate(Point3D(13.7, 6.5, -4.2), Vector3D(-10.4, 3.3, 1.1))
        # then
        self.assertEqual(Point3D(3.3, 9.8, -3.1), result)

    def test__translate__when_zero_vector__then_same_point(self):
        # given
        point = Point3D(13.5, 6.5, -4.2)
        # when
        result = translate(point, Vector3D(0.0, 0.0, 0.0))
        # then
        self.assertEqual(point, result)
