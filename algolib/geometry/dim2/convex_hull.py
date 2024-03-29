# -*- coding: utf-8 -*-
"""Algorithm for convex hull in 2D (monotone chain)."""
from typing import List, Sequence

from .geometry_2d import sorted_by_x
from .point_2d import Point2D
from .vector_2d import Vector2D


def find_convex_hull(points: Sequence[Point2D]) -> List[Point2D]:
    """Computes convex hull of given points.

    :param points: the points
    :return: the points in the convex hull"""
    if len(points) < 3:
        return []

    points = sorted_by_x(points)
    lower_hull = _create_half_hull(points)
    upper_hull = _create_half_hull(reversed(points))

    lower_hull.pop()
    upper_hull.pop()
    return lower_hull + upper_hull


def _create_half_hull(points):
    # Creates a half of a convex hull for specified points.
    hull = []

    for pt in points:
        while len(hull) > 1 and _cross_product(hull[-2], hull[-1], pt) >= 0:
            hull.pop()

        hull.append(pt)

    return hull


def _cross_product(pt1, pt2, pt3):
    return Vector2D.area(Vector2D.between(pt2, pt1), Vector2D.between(pt2, pt3))
