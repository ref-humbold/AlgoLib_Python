# -*- coding: utf-8 -*-
"""Tests: Algorithms for points sorting"""
import unittest

from algolib.geometry.space import Point3D, sorted_by_x, sorted_by_y, sorted_by_z


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__sorted_by_x__when_tuple__then_new_stably_sorted_list_ascending_by_x_coordinate(
            self):
        # given
        sequence = (Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0,
                                                      -5.0), Point3D(3.0, 2.0,
                                                                     5.0), Point3D(-3.0, 2.0, 5.0))
        # when
        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([Point3D(-3.0, 2.0, 5.0), Point3D(-2.0, -3.0, 5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(3.0, 2.0, 5.0)], result)

    def test__sorted_by_y__when_list__then_new_stably_sorted_list_ascending_by_y_coordinate(
            self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point3D(-2.0, -3.0, 5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(3.0, 2.0, 5.0), Point3D(-3.0, 2.0, 5.0),
                              Point3D(2.0, 3.0, -5.0)], result)

    def test__sorted_by_z__when_list__then_new_stably_sorted_list_ascending_by_z_coordinate(
            self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_z(sequence)

        self.assertIsInstance(result, list)
        self.assertIsNot(sequence, result)
        self.assertListEqual([Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                              Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                              Point3D(-2.0, -3.0, 5.0), Point3D(3.0, 2.0, 5.0),
                              Point3D(-3.0, 2.0, 5.0)], result)
