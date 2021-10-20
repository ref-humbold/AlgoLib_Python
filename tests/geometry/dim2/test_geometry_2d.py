# -*- coding: utf-8 -*-
"""Tests: Algorithms for basic geometrical computations in 2D"""
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Point2D, Vector2D, distance, sorted_by_angle, sorted_by_x, \
    sorted_by_y, translate


class Geometry2DTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__sorted_by_x__when_list__then_new_list_sorted_stably_ascending():
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0)]
        # when
        result = sorted_by_x(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point2D(-3.0, 2.0), Point2D(-3.0, -2.0),
                                         Point2D(-2.0, -3.0), Point2D(-2.0, 3.0), Point2D(0.0, 0.0),
                                         Point2D(2.0, 3.0), Point2D(2.0, -3.0), Point2D(3.0, -2.0),
                                         Point2D(3.0, 2.0)])

    @staticmethod
    def test__sorted_by_y__when_tuple__then_new_list_sorted_stably_ascending():
        # given
        sequence = (Point2D(0.0, 0.0), Point2D(-2.0, -3.0), Point2D(-3.0, 2.0), Point2D(2.0, 3.0),
                    Point2D(3.0, -2.0), Point2D(-2.0, 3.0), Point2D(3.0, 2.0), Point2D(2.0, -3.0),
                    Point2D(-3.0, -2.0))
        # when
        result = sorted_by_y(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point2D(-2.0, -3.0), Point2D(2.0, -3.0),
                                         Point2D(3.0, -2.0), Point2D(-3.0, -2.0), Point2D(0.0, 0.0),
                                         Point2D(-3.0, 2.0), Point2D(3.0, 2.0), Point2D(2.0, 3.0),
                                         Point2D(-2.0, 3.0)])

    @staticmethod
    def test__sorted_by_angle__then_new_list_sorted_ascending():
        # given
        sequence = [Point2D(0, 0), Point2D(-2, -3), Point2D(-3, -2), Point2D(3, -2), Point2D(-2, 3),
                    Point2D(3, 2), Point2D(2, -3), Point2D(2, 3), Point2D(-3, 2)]
        # when
        result = sorted_by_angle(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point2D(0, 0), Point2D(3, 2), Point2D(2, 3),
                                         Point2D(-2, 3), Point2D(-3, 2), Point2D(-3, -2),
                                         Point2D(-2, -3), Point2D(2, -3), Point2D(3, -2)])

    @staticmethod
    def test__sorted_by_angle__when_equal_angles__then_compare_radius():
        # given
        sequence = [Point2D(0.0, 0.0), Point2D(1.0, 1.0), Point2D(-2.0, -2.0), Point2D(-3.0, -3.0),
                    Point2D(4.0, 4.0)]
        # when
        result = sorted_by_angle(sequence)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to([Point2D(0.0, 0.0), Point2D(1.0, 1.0), Point2D(4.0, 4.0),
                                         Point2D(-2.0, -2.0), Point2D(-3.0, -3.0)])

    @staticmethod
    def test__distance__when_different_points__then_distance():
        # when
        result = distance(Point2D(4.0, 5.0), Point2D(-2.0, -3.0))
        # then
        assert_that(result).is_equal_to(10.0)

    @staticmethod
    def test__distance__when_same_point__then_zero():
        # given
        point = Point2D(13.5, 6.5)
        # when
        result = distance(point, point)
        # then
        assert_that(result).is_equal_to(0.0)

    @staticmethod
    def test__translate__then_point_translated():
        # when
        result = translate(Point2D(13.7, 6.5), Vector2D(-10.4, 3.3))
        # then
        assert_that(result).is_equal_to(Point2D(3.3, 9.8))

    @staticmethod
    def test__translate__when_zero_vector__then_same_point():
        # given
        point = Point2D(13.5, 6.5)
        # when
        result = translate(point, Vector2D(0.0, 0.0))
        # then
        assert_that(result).is_equal_to(point)
