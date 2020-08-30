# -*- coding: utf-8 -*-
import unittest

from algolib.geometry import Point2D, find_convex_hull


class ConvexHullTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test__find_convex_hull__when_one_point__then_empty_convex_hull(self):
        # when
        result = find_convex_hull([Point2D(3.0, 2.0)])
        # then
        self.assertEqual(0, len(result))

    def test__find_convex_hull__when_two_points__then_empty_convex_hull(self):
        # given
        points = [Point2D(2.0, 3.0), Point2D(3.0, 2.0)]
        # when
        result = find_convex_hull(points)
        # then
        self.assertEqual(0, len(result))

    def test__find_convex_hull__when_three_points__then_these_points_in_convex_hull(self):
        # given
        points = [Point2D(1.0, -1.0), Point2D(5.0, 1.0), Point2D(3.0, 4.0)]
        # when
        result = find_convex_hull(points)
        # then
        self.assertListEqual(points, result)

    def test__find_convex_hull__then_points_in_convex_hull(self):
        # given
        points = [
                Point2D(1, -3),
                Point2D(-4, 6),
                Point2D(-5, -7),
                Point2D(-8, -7),
                Point2D(-3, -4),
                Point2D(5, 9),
                Point2D(-1, -8),
                Point2D(-5, 10),
                Point2D(8, 0),
                Point2D(3, -6),
                Point2D(-2, 1),
                Point2D(-2, 8),
                Point2D(10, 2),
                Point2D(6, 3),
                Point2D(-7, 7),
                Point2D(6, -4)]
        # when
        result = find_convex_hull(points)
        # then
        self.assertListEqual([
                Point2D(-8, -7),
                Point2D(-1, -8),
                Point2D(3, -6),
                Point2D(6, -4),
                Point2D(10, 2),
                Point2D(5, 9),
                Point2D(-5, 10),
                Point2D(-7, 7)], result)

    def test__find_convex_hull__when_multiple_points_are_collinear__then_convex_hull_omits_inner_points(
            self):
        # given
        points = [
                Point2D(-1, -3),
                Point2D(-3, -3),
                Point2D(-3, -1),
                Point2D(2, -3),
                Point2D(-3, 5),
                Point2D(0, -3),
                Point2D(7, -3),
                Point2D(-3, -2)]
        # when
        result = find_convex_hull(points)
        # then
        self.assertListEqual([Point2D(-3, -3), Point2D(7, -3), Point2D(-3, 5)], result)
