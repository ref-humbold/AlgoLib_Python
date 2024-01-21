# -*- coding: utf-8 -*-
"""Tests: Algorithm for convex hull in 2D (monotone chain)."""
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Point2D, find_convex_hull


class ConvexHullTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__find_convex_hull__when_one_point__then_empty():
        # when
        result = find_convex_hull([Point2D(3.0, 2.0)])
        # then
        assert_that(result).is_length(0)

    @staticmethod
    def test__find_convex_hull__when_two_points__then_empty():
        # when
        result = find_convex_hull([Point2D(2.0, 3.0), Point2D(3.0, 2.0)])
        # then
        assert_that(result).is_length(0)

    @staticmethod
    def test__find_convex_hull__when_three_points__then_these_points_are_hull():
        # given
        points = [Point2D(1.0, -1.0), Point2D(5.0, 1.0), Point2D(3.0, 4.0)]
        # when
        result = find_convex_hull(points)
        # then
        assert_that(result).is_equal_to(points)

    @staticmethod
    def test__find_convex_hull__then_points_in_hull():
        # when
        result = find_convex_hull(
            [Point2D(1, -3), Point2D(-4, 6), Point2D(-5, -7), Point2D(-8, -7), Point2D(-3, -4),
             Point2D(5, 9), Point2D(-1, -8), Point2D(-5, 10), Point2D(8, 0), Point2D(3, -6),
             Point2D(-2, 1), Point2D(-2, 8), Point2D(10, 2), Point2D(6, 3), Point2D(-7, 7),
             Point2D(6, -4)])
        # then
        assert_that(result).is_equal_to(
            [Point2D(-8, -7), Point2D(-1, -8), Point2D(3, -6), Point2D(6, -4), Point2D(10, 2),
             Point2D(5, 9), Point2D(-5, 10), Point2D(-7, 7)])

    @staticmethod
    def test__find_convex_hull__when_multiple_points_are_collinear__then_inner_points_omitted():
        # when
        result = find_convex_hull(
            [Point2D(-1, -3), Point2D(-3, -3), Point2D(-3, -1), Point2D(2, -3), Point2D(-3, 5),
             Point2D(0, -3), Point2D(7, -3), Point2D(-3, -2)])
        # then
        assert_that(result).is_equal_to([Point2D(-3, -3), Point2D(7, -3), Point2D(-3, 5)])
