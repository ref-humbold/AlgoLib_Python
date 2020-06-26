# -*- coding: utf-8 -*-
"""Tests: Structure of point on a plane"""
from math import pi
from unittest import TestCase

from algolib.geometry import Point2D


class Point2DTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        pass

    def tearDown(self):
        self._test_object = None

    def test__angle_deg__when_point_in_first_quarter__then_between_0_and_90(self):
        # given
        self._test_object = Point2D(3, 7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(0 < result < 90)

    def test__angle_deg__when_point_in_second_quarter__then_between_90_and_180(self):
        # given
        self._test_object = Point2D(-3, 7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(90 < result < 180)

    def test__angle_deg__when_point_in_third_quarter__then_between_180_and_270(self):
        # given
        self._test_object = Point2D(-3, -7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(180 < result < 270)

    def test__angle_deg__when_point_in_fourth_quarter__then_between_270_and_360(self):
        # given
        self._test_object = Point2D(3, -7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(270 < result < 360)

    def test__angle_rad__when_point_on_positive_x_axis__then_zero(self):
        # given
        self._test_object = Point2D(6, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(0, result)

    def test__angle_rad__when_point_on_negative_x_axis__then_pi(self):
        # given
        self._test_object = Point2D(-6, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(pi, result)

    def test__angle_rad__when_point_on_positive_y_axis__then_pi_half(self):
        # given
        self._test_object = Point2D(0, 6)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(pi / 2, result)

    def test__angle_rad__when_point_on_negative_y_axis__then_minus_pi_half(self):
        # given
        self._test_object = Point2D(0, -6)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(-pi / 2, result)

    def test__angle_rad__when_zero_point__then_zero(self):
        # given
        self._test_object = Point2D(0, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(0, result)

    def test__radius__when_zero_point__then_zero(self):
        # given
        self._test_object = Point2D(0, 0)
        # when
        result = self._test_object.radius
        # then
        self.assertEqual(0, result)

    def test__radius__when_point_on_plane__then_squared_distance_from_zero(self):
        # given
        self._test_object = Point2D(3, -4)
        # when
        result = self._test_object.radius
        # then
        self.assertEqual(5, result)

    def test__eq__when_same_coordinates__then_true(self):
        # given
        self._test_object = Point2D(7, -5)
        # when
        result = self._test_object == Point2D(7, -5)
        # then
        self.assertTrue(result)

    def test__ne__when_different_coordinates__then_true(self):
        # given
        self._test_object = Point2D(7, -5)
        # when
        result = self._test_object != Point2D(-7, 5)
        # then
        self.assertTrue(result)

    def test__gt__when_x_coordinate_is_greater__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object > Point2D(3, 5)
        # then
        self.assertTrue(result)

    def test__ge__when_y_coordinate_is_greater__then_true(self):
        # given
        self._test_object = Point2D(7, 15)
        # when
        result = self._test_object >= Point2D(7, 8)
        # then
        self.assertTrue(result)

    def test__lt__when_x_coordinate_is_less__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object < Point2D(16, 5)
        # then
        self.assertTrue(result)

    def test__le__when_y_coordinate_is_less__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object <= Point2D(7, 11)
        # then
        self.assertTrue(result)
