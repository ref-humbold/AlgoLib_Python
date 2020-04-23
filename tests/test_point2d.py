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

    def test_angle_deg__when_point_in_first_quarter__then_between_0_and_90(self):
        # given
        self._test_object = Point2D(3, 7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(0 < result < 90)

    def test_angle_deg__when_point_in_second_quarter__then_between_90_and_180(self):
        # given
        self._test_object = Point2D(-3, 7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(90 < result < 180)

    def test_angle_deg__when_point_in_third_quarter__then_between_180_and_270(self):
        # given
        self._test_object = Point2D(-3, -7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(180 < result < 270)

    def test_angle_deg__when_point_in_fourth_quarter__then_between_270_and_360(self):
        # given
        self._test_object = Point2D(3, -7)
        # when
        result = self._test_object.angle_deg
        # then
        self.assertTrue(270 < result < 360)

    def test_angle_rad__when_point_on_positive_X_axis__then_zero(self):
        # given
        self._test_object = Point2D(6, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(0, result)

    def test_angle_rad__when_point_on_negative_X_axis__then_pi(self):
        # given
        self._test_object = Point2D(-6, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(pi, result)

    def test_angle_rad__when_point_on_positive_Y_axis__then_pi_half(self):
        # given
        self._test_object = Point2D(0, 6)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(pi / 2, result)

    def test_angle_rad__when_point_on_negative_Y_axis__then_minus_pi_half(self):
        # given
        self._test_object = Point2D(0, -6)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(-pi / 2, result)

    def test_angle_rad__when_zero_point__then_zero(self):
        # given
        self._test_object = Point2D(0, 0)
        # when
        result = self._test_object.angle_rad
        # then
        self.assertEqual(0, result)

    def test_radius__when_zero_point__then_zero(self):
        # given
        self._test_object = Point2D(0, 0)
        # when
        result = self._test_object.radius
        # then
        self.assertEqual(0, result)

    def test_radius__when_point_on_plane__then_squared_distance_from_zero(self):
        # given
        self._test_object = Point2D(3, -4)
        # when
        result = self._test_object.radius
        # then
        self.assertEqual(5, result)

    def test_eq__when_same_coordinates__then_true(self):
        # given
        self._test_object = Point2D(7, -5)
        # when
        result = self._test_object == Point2D(7, -5)
        # then
        self.assertTrue(result)

    def test_ne__when_different_coordinates__then_true(self):
        # given
        self._test_object = Point2D(7, -5)
        # when
        result = self._test_object != Point2D(-7, 5)
        # then
        self.assertTrue(result)

    def test_gt__when_X_coordinate_is_greater__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object > Point2D(3, 5)
        # then
        self.assertTrue(result)

    def test_ge__when_Y_coordinate_is_greater__then_true(self):
        # given
        self._test_object = Point2D(7, 15)
        # when
        result = self._test_object >= Point2D(7, 8)
        # then
        self.assertTrue(result)

    def test_lt__when_X_coordinate_is_less__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object < Point2D(16, 5)
        # then
        self.assertTrue(result)

    def test_le__when_Y_coordinate_is_less__then_true(self):
        # given
        self._test_object = Point2D(7, 5)
        # when
        result = self._test_object <= Point2D(7, 11)
        # then
        self.assertTrue(result)
