# -*- coding: utf-8 -*-
"""Tests: Algorithm for pair of closest points in 2D"""
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Point2D, find_closest_points


class ClosestPointsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__find_closest_points__when_one_point__then_this_point():
        # when
        result = find_closest_points([Point2D(2, 2)])
        # then
        assert_that(result).is_equal_to((Point2D(2, 2), Point2D(2, 2)))

    @staticmethod
    def test__find_closest_points__when_two_points__then_these_points():
        # when
        result = find_closest_points([Point2D(2, 2), Point2D(4, 4)])
        # then
        assert_that(result).is_equal_to((Point2D(2, 2), Point2D(4, 4)))

    @staticmethod
    def test__find_closest_points__when_three_points__then_pair_of_closest_points():
        # when
        result = find_closest_points([Point2D(3, 2), Point2D(1, 1), Point2D(7, 0)])
        # then
        assert_that(result).is_equal_to((Point2D(1, 1), Point2D(3, 2)))

    @staticmethod
    def test__find_closest_points__when_multiple_points__then_pair_of_closest_points():
        # when
        result = find_closest_points(
            [Point2D(1, 1), Point2D(-2, 2), Point2D(-4, 4), Point2D(3, -3), Point2D(0, -5),
             Point2D(1, 0), Point2D(-7, 2), Point2D(4, 5)])
        # then
        assert_that(result).is_equal_to((Point2D(1, 1), Point2D(1, 0)))
