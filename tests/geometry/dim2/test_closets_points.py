# -*- coding: utf-8 -*-
"""Tests: Algorithm for pair of closest points in 2D"""
import unittest

from algolib.geometry.dim2 import Point2D, find_closest_points


class ClosestPointsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__find_closest_points__when_one_point__then_this_point(self):
        # when
        result = find_closest_points([Point2D(2, 2)])
        # then
        self.assertTupleEqual((Point2D(2, 2), Point2D(2, 2)), result)

    def test__find_closest_points__when_two_points__then_these_points(self):
        # when
        result = find_closest_points([Point2D(2, 2), Point2D(4, 4)])
        # then
        self.assertTupleEqual((Point2D(2, 2), Point2D(4, 4)), result)

    def test__find_closest_points__when_three_points__then_pair_of_closest_points(self):
        # when
        result = find_closest_points([Point2D(3, 2), Point2D(1, 1), Point2D(7, 0)])
        # then
        self.assertTupleEqual((Point2D(1, 1), Point2D(3, 2)), result)

    def test__find_closest_points__when_multiple_points__then_pair_of_closest_points(self):
        # when
        result = find_closest_points(
            [Point2D(1, 1), Point2D(-2, 2), Point2D(-4, 4), Point2D(3, -3), Point2D(0, -5),
             Point2D(1, 0), Point2D(-7, 2), Point2D(4, 5)])
        # then
        self.assertTupleEqual((Point2D(1, 1), Point2D(1, 0)), result)
