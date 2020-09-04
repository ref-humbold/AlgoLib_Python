# -*- coding: utf-8 -*-
"""Tests: Algorithms for points sorting"""
import unittest

from algolib.geometry import Point2D, Point3D, sorted_by_angle, sorted_by_x, sorted_by_y, \
    sorted_by_z


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region sorted_by_x

    def test__sorted_by_x__when_list_2d__then_new_stably_sorted_list_ascending_by_x_coordinate(
            self):
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-3.0, 2.0),
                Point2D(-3.0, -2.0),
                Point2D(-2.0, -3.0),
                Point2D(-2.0, 3.0),
                Point2D(0.0, 0.0),
                Point2D(2.0, 3.0),
                Point2D(2.0, -3.0),
                Point2D(3.0, -2.0),
                Point2D(3.0, 2.0)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_x__when_tuple_3d__then_new_stably_sorted_list_ascending_by_x_coordinate(
            self):
        # given
        sequence = (Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0,
                                                      -5.0), Point3D(3.0, 2.0,
                                                                     5.0), Point3D(-3.0, 2.0, 5.0))
        # when
        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point3D(-3.0, 2.0, 5.0),
                Point3D(-2.0, -3.0, 5.0),
                Point3D(-2.0, -3.0, -5.0),
                Point3D(0.0, 0.0, 0.0),
                Point3D(2.0, 3.0, -5.0),
                Point3D(2.0, -3.0, -5.0),
                Point3D(3.0, 2.0, 5.0)], result)

    # endregion
    # region sorted_by_y

    def test__sorted_by_y__when_tuple_2d__then_new_stably_sorted_list_ascending_by_y_coordinate(
            self):
        # given
        sequence = (Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0))
        # when
        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-2.0, -3.0),
                Point2D(2.0, -3.0),
                Point2D(3.0, -2.0),
                Point2D(-3.0, -2.0),
                Point2D(0.0, 0.0),
                Point2D(-3.0, 2.0),
                Point2D(3.0, 2.0),
                Point2D(2.0, 3.0),
                Point2D(-2.0, 3.0)], result)

    def test__sorted_by_y__when_list_3d__then_new_stably_sorted_list_ascending_by_y_coordinate(
            self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point3D(-2.0, -3.0, 5.0),
                Point3D(2.0, -3.0, -5.0),
                Point3D(-2.0, -3.0, -5.0),
                Point3D(0.0, 0.0, 0.0),
                Point3D(3.0, 2.0, 5.0),
                Point3D(-3.0, 2.0, 5.0),
                Point3D(2.0, 3.0, -5.0)], result)
        self.assertListEqual(sequence_copy, sequence)

    # endregion
    # region sorted_by_z

    def test__sorted_by_z__when_list_3d__then_new_stably_sorted_list_ascending_by_z_coordinate(
            self):
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_z(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point3D(2.0, 3.0, -5.0),
                Point3D(2.0, -3.0, -5.0),
                Point3D(-2.0, -3.0, -5.0),
                Point3D(0.0, 0.0, 0.0),
                Point3D(-2.0, -3.0, 5.0),
                Point3D(3.0, 2.0, 5.0),
                Point3D(-3.0, 2.0, 5.0)], result)
        self.assertListEqual(sequence_copy, sequence)

    # endregion
    # region sorted_by_angle

    def test__sorted_by_angle__then_new_sorted_list(self):
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_angle(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(0, 0),
                Point2D(3, 2),
                Point2D(2, 3),
                Point2D(-2, 3),
                Point2D(-3, 2),
                Point2D(-3, -2),
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(3, -2)], result)
        self.assertListEqual(sequence_copy, sequence)

    # endregion
