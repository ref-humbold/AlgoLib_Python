# -*- coding: utf-8 -*-
"""Tests: Algorithms for points sorting"""
import unittest

from algolib.geometry import Point2D, Point3D, sorted_by_angle, sorted_by_xy, sorted_by_xyz, \
    sorted_by_yx


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    def test__sorted_by_angle__when_empty_list__then_empty_list(self):
        # given
        sequence = []
        # when
        result = sorted_by_angle(sequence)
        # then
        self.assertListEqual([], result)

    # endregion
    # region sorted_by_xy

    def test__sorted_by_xy__then_new_sorted_list(self):
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_xy(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-3, -2),
                Point2D(-3, 2),
                Point2D(-2, -3),
                Point2D(-2, 3),
                Point2D(0, 0),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(3, -2),
                Point2D(3, 2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_xy_when_argument_is_tuple__then_sorted_list(self):
        # given
        sequence = (Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2))
        # when
        result = sorted_by_xy(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-3, -2),
                Point2D(-3, 2),
                Point2D(-2, -3),
                Point2D(-2, 3),
                Point2D(0, 0),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(3, -2),
                Point2D(3, 2)], result)

    def test__sorted_by_xy__when_empty_list__then_empty_list(self):
        # given
        sequence = []
        # when
        result = sorted_by_xy(sequence)
        # then
        self.assertListEqual([], result)

    # endregion
    # region sorted_by_yx

    def test__sorted_by_yx__then_new_sorted_list(self):
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_yx(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(0, 0),
                Point2D(-3, 2),
                Point2D(3, 2),
                Point2D(-2, 3),
                Point2D(2, 3)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_yx__when_argument_is_set__then_sorted_list(self):
        # given
        sequence = {Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)}
        # when
        result = sorted_by_yx(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(0, 0),
                Point2D(-3, 2),
                Point2D(3, 2),
                Point2D(-2, 3),
                Point2D(2, 3)], result)

    def test__sorted_by_yx__when_empty_list__then_empty_list(self):
        # given
        sequence = []
        # when
        result = sorted_by_yx(sequence)
        # then
        self.assertListEqual([], result)

    # endregion
    # region sorted_by_xy

    def test__sorted_by_xyz__then_new_sorted_list(self):
        # given
        sequence = [Point3D(0, 0, 0), Point3D(2, 3, 7), Point3D(-2, -3, -7), Point3D(2, -3, -7),
                    Point3D(-2, 3, 7), Point3D(2, 3, -7), Point3D(-2, -3, 7)]
        sequence_copy = sequence[:]
        # when
        result = sorted_by_xyz(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point3D(-2, -3, -7),
                Point3D(-2, -3, 7),
                Point3D(-2, 3, 7),
                Point3D(0, 0, 0),
                Point3D(2, -3, -7),
                Point3D(2, 3, -7),
                Point3D(2, 3, 7)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_xyz__when_empty_list__then_empty_list(self):
        # given
        sequence = []
        # when
        result = sorted_by_xyz(sequence)
        # then
        self.assertListEqual([], result)

    # endregion
