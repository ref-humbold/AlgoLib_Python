# -*- coding: utf-8 -*-
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Angle2D, AngleUnit, Point2D


class Point2DTest(unittest.TestCase):
    OFFSET = 1e-12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params_for__angle = [
            (Point2D(0.0, 0.0), 0.0), (Point2D(7.0, 0.0), 0.0), (Point2D(7.0, 7.0), 45.0),
            (Point2D(0.0, 7.0), 90.0), (Point2D(-7.0, 7.0), 135.0), (Point2D(-7.0, 0.0), 180.0),
            (Point2D(-7.0, -7.0), 225.0), (Point2D(0.0, -7.0), 270.0), (Point2D(7.0, -7.0), 315.0)
        ]
        self.params_for__radius = [
            (Point2D(0.0, 0.0), 0.0), (Point2D(14.0, 0.0), 14.0), (Point2D(-14.0, 0.0), 14.0),
            (Point2D(0.0, 14.0), 14.0), (Point2D(0.0, -14.0), 14.0), (Point2D(8.0, 6.0), 10.0),
            (Point2D(8.0, -6.0), 10.0), (Point2D(-8.0, 6.0), 10.0), (Point2D(-8.0, -6.0), 10.0)
        ]

    @staticmethod
    def test__coordinates__then_tuple():
        # when
        result = Point2D(150.123456789, -3700.987654321).coordinates

        # then
        assert_that(result).is_equal_to((150.123456789, -3700.987654321))

    def test__angle__then_counter_clockwise_angle_from_x_axis(self):
        for point, expected in self.params_for__angle:
            with self.subTest(param=point):
                # when
                result = point.angle

                # then
                assert_that(result).is_equal_to(Angle2D(expected, AngleUnit.DEGREES))

    def test__radius__then_distance_from_zero_point(self):
        for point, expected in self.params_for__radius:
            with self.subTest(param=point):
                # when
                result = point.radius

                # then
                assert_that(result).is_close_to(expected, self.OFFSET)

    @staticmethod
    def test__op_str__then_string_representation():
        # when
        result = str(Point2D(150.123456789, -3700.987654321))

        # then
        assert_that(result).is_equal_to("(150.123456789, -3700.987654321)")
