# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic geometrical computations in 3D"""
import unittest

from assertpy import assert_that

from algolib.geometry.dim3 import Point3D, Vector3D, distance, sorted_by_x, sorted_by_y, \
    sorted_by_z, translate


class Geometry3DTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__sorted_by_x__when_tuple__then_new_list_sorted_stably_ascending():
        # given
        sequence = (Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0))
        # when
        result = sorted_by_x(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point3D(-3.0, 2.0, 5.0), Point3D(-2.0, -3.0, 5.0),
                                         Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                                         Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                                         Point3D(3.0, 2.0, 5.0)])

    @staticmethod
    def test__sorted_by_y__when_list__then_new_list_sorted_stably_ascending():
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_y(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point3D(-2.0, -3.0, 5.0), Point3D(2.0, -3.0, -5.0),
                                         Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                                         Point3D(3.0, 2.0, 5.0), Point3D(-3.0, 2.0, 5.0),
                                         Point3D(2.0, 3.0, -5.0)])

    @staticmethod
    def test__sorted_by_z__when_list__then_new_list_sorted_stably_ascending():
        # given
        sequence = [Point3D(0.0, 0.0, 0.0), Point3D(2.0, 3.0, -5.0), Point3D(-2.0, -3.0, 5.0),
                    Point3D(2.0, -3.0, -5.0), Point3D(-2.0, -3.0, -5.0), Point3D(3.0, 2.0, 5.0),
                    Point3D(-3.0, 2.0, 5.0)]
        # when
        result = sorted_by_z(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point3D(2.0, 3.0, -5.0), Point3D(2.0, -3.0, -5.0),
                                         Point3D(-2.0, -3.0, -5.0), Point3D(0.0, 0.0, 0.0),
                                         Point3D(-2.0, -3.0, 5.0), Point3D(3.0, 2.0, 5.0),
                                         Point3D(-3.0, 2.0, 5.0)])

    @staticmethod
    def test__distance__when_different_points__then_distance():
        # when
        result = distance(Point3D(4.0, 8.0, 5.0), Point3D(-2.0, -1.0, 3.0))
        # then
        assert_that(result).is_equal_to(11.0)

    @staticmethod
    def test__distance__when_same_point__then_zero():
        # given
        point = Point3D(13.5, 6.5, -4.2)
        # when
        result = distance(point, point)
        # then
        assert_that(result).is_equal_to(0.0)

    @staticmethod
    def test__translate__then_point_translated():
        # when
        result = translate(Point3D(13.7, 6.5, -4.2), Vector3D(-10.4, 3.3, 1.1))
        # then
        assert_that(result).is_equal_to(Point3D(3.3, 9.8, -3.1))

    @staticmethod
    def test__translate__when_zero_vector__then_same_point():
        # given
        point = Point3D(13.5, 6.5, -4.2)
        # when
        result = translate(point, Vector3D(0.0, 0.0, 0.0))
        # then
        assert_that(result).is_equal_to(point)
