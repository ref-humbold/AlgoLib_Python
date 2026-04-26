# -*- coding: utf-8 -*-
"""Algorithms for convex hull in 2D."""
from typing import Any, List, Sequence

from .geometry_2d import sorted_by_angle, sorted_by_x, translate
from .point_2d import Point2D
from .vector_2d import Vector2D


def find_andrew_convex_hull(points: Sequence[Point2D]) -> List[Point2D]:
    """Computes convex hull of given points using Andrew's monotone chain.

    :param points: the points
    :return: the points in the convex hull"""
    if len(points) < 3:
        return []

    sorted_points = sorted_by_x(points)
    lower_hull = _collect_hull(sorted_points)
    upper_hull = _collect_hull(list(reversed(sorted_points)))

    return lower_hull[:-1] + upper_hull[:-1]


def find_graham_convex_hull(points: Sequence[Point2D]) -> List[Point2D]:
    """Computes convex hull of given points using Graham's scan.

    :param points: the points
    :return: the points in the convex hull"""
    if len(points) < 3:
        return []

    min_point = min(points, key=lambda p: (p.y, p.x))
    moving = Vector2D.between(min_point, Point2D(0, 0))
    angle_points = sorted_by_angle(translate(pt, moving) for pt in points)
    hull = _collect_hull(angle_points)

    return [translate(pt, -moving) for pt in hull]


def _collect_hull(points: list[Point2D]) -> list[Any]:
    hull = []

    for pt in points:
        while len(hull) > 1 and _cross_product(hull[-2], hull[-1], pt) >= 0:
            hull.pop()

        hull.append(pt)

    return hull


def _cross_product(pt1, pt2, pt3):
    return Vector2D.area(Vector2D.between(pt2, pt1), Vector2D.between(pt2, pt3))
