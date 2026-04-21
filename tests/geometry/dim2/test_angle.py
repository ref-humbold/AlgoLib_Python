# -*- coding: utf-8 -*-
from math import pi
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Angle, AngleUnit


class AngleTest(unittest.TestCase):
    OFFSET = 1e-12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params_degrees_from_radians = [
                [0.0, 0.0], [pi / 6, 30.0], [pi / 4, 45.0], [pi / 3, 60.0], [pi / 2, 90.0],
                [pi, 180.0], [2 * pi, 0.0], [3 * pi, 180.0], [-pi / 6, 330.0], [-pi / 4, 315.0],
                [-pi / 3, 300.0], [-pi / 2, 270.0], [-pi, 180.0], [-2 * pi, 0.0], [-3 * pi, 180.0]
        ]
        self.params_radians_from_degrees = [
                [0.0, 0.0], [30.0, pi / 6], [45.0, pi / 4], [60.0, pi / 3], [90.0, pi / 2],
                [180.0, pi], [360.0, 0.0], [540.0, pi], [-30.0, 11 * pi / 6], [-45.0, 7 * pi / 4],
                [-60.0, 5 * pi / 3], [-90.0, 3 * pi / 2], [-180.0, pi], [-360.0, 0.0], [-540.0, pi]
        ]

    def test__degrees__when_from_radians__then_positive_degrees_in_range(self):
        for radians, degrees in self.params_degrees_from_radians:
            with self.subTest(param=radians):
                # given
                angle = Angle(radians, AngleUnit.RADIANS)

                # when
                result = angle.degrees

                # then
                assert_that(result).is_close_to(degrees, self.OFFSET)

    def test__radians__when_from_degrees__then_positive_radians_in_range(self):
        for degrees, radians in self.params_radians_from_degrees:
            with self.subTest(param=degrees):
                # given
                angle = Angle(degrees, AngleUnit.DEGREES)

                # when
                result = angle.radians

                # then
                assert_that(result).is_close_to(radians, self.OFFSET)

    @staticmethod
    def test__op_str__then_string_representation():
        # when
        result = str(Angle(150.123456789, AngleUnit.DEGREES))

        # then
        assert_that(result).is_equal_to(f"Angle(150.123456789, AngleUnit.DEGREES)")
