# -*- coding: utf-8 -*-
import unittest

from assertpy import assert_that

from algolib.geometry.dim3 import Point3D


class Point3DTest(unittest.TestCase):
    OFFSET = 1e-12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params_for__radius = [
            (Point3D(0.0, 0.0, 0.0), 0.0), (Point3D(14.0, 0.0, 0.0), 14.0),
            (Point3D(-14.0, 0.0, 0.0), 14.0), (Point3D(0.0, 14.0, 0.0), 14.0),
            (Point3D(0.0, -14.0, 0.0), 14.0), (Point3D(0.0, 0.0, 14.0), 14.0),
            (Point3D(0.0, 0.0, -14.0), 14.0), (Point3D(8.0, 6.0, 0.0), 10.0),
            (Point3D(8.0, -6.0, 0.0), 10.0), (Point3D(-8.0, 6.0, 0.0), 10.0),
            (Point3D(-8.0, -6.0, 0.0), 10.0), (Point3D(8.0, 0.0, 6.0), 10.0),
            (Point3D(8.0, 0.0, -6.0), 10.0), (Point3D(-8.0, 0.0, 6.0), 10.0),
            (Point3D(-8.0, 0.0, -6.0), 10.0), (Point3D(0.0, 8.0, 6.0), 10.0),
            (Point3D(0.0, 8.0, -6.0), 10.0), (Point3D(0.0, -8.0, 6.0), 10.0),
            (Point3D(0.0, -8.0, -6.0), 10.0), (Point3D(18.0, 6.0, 13.0), 23.0),
            (Point3D(18.0, 6.0, -13.0), 23.0), (Point3D(18.0, -6.0, 13.0), 23.0),
            (Point3D(18.0, -6.0, -13.0), 23.0), (Point3D(-18.0, 6.0, 13.0), 23.0),
            (Point3D(-18.0, 6.0, -13.0), 23.0), (Point3D(-18.0, -6.0, 13.0), 23.0),
            (Point3D(-18.0, -6.0, -13.0), 23.0)
        ]

    @staticmethod
    def test__coordinates__then_tuple():
        # when
        result = Point3D(150.123456789, -3700.987654321, 0.55555555).coordinates

        # then
        assert_that(result).is_equal_to((150.123456789, -3700.987654321, 0.55555555))

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
        result = str(Point3D(150.123456789, -3700.987654321, 0.55555555))

        # then
        assert_that(result).is_equal_to("(150.123456789, -3700.987654321, 0.55555555)")
