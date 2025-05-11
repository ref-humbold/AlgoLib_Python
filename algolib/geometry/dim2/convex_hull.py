# -*- coding: utf-8 -*-
"""Algorithm for convex hull in 2D (Graham's scan)."""
from typing import List, Sequence

from .geometry_2d import sorted_by_angle, translate
from .point_2d import Point2D
from .vector_2d import Vector2D


def find_convex_hull(points: Sequence[Point2D]) -> List[Point2D]:
    """Computes convex hull of given points.

    :param points: the points
    :return: the points in the convex hull"""
    if len(points) < 3:
        return []

    moving = Vector2D.between(Point2D(0, 0), min(points, key=lambda p: (p.y, p.x)))
    angle_points = sorted_by_angle(translate(pt, -moving) for pt in points)

    hull = []

    for pt in angle_points:
        while len(hull) > 1 and _cross_product(hull[-2], hull[-1], pt) >= 0:
            hull.pop()

        hull.append(pt)

    return [translate(pt, moving) for pt in hull]


def _cross_product(pt1, pt2, pt3):
    return Vector2D.area(Vector2D.between(pt2, pt1), Vector2D.between(pt2, pt3))
