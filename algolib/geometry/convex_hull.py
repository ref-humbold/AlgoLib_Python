# -*- coding: utf-8 -*-
"""Algorithm for convex hull on a plane (monotone chain)"""
from .points_sorting import sorted_by_x


def convex_hull(points):
    """Constructs a convex hull of specified set of points.

    :param points: sequence of points
    :return: hull points list"""
    if len(points) < 3:
        return []

    points = sorted_by_x(points)
    upper_hull = _create_half_hull(points)
    lower_hull = _create_half_hull(reversed(points))

    upper_hull.pop()
    lower_hull.pop()

    return upper_hull + lower_hull


def _create_half_hull(points):
    # Creates a half of a convex hull for specified points
    hull = []

    for pt in points:
        while len(hull) > 1 and _cross_product(hull[-2], hull[-1], pt) <= 0:
            hull.pop()

        hull.append(pt)

    return hull


def _cross_product(pt1, pt2, pt3):
    return (pt1.x - pt2.x) * (pt3.y - pt2.y) - (pt3.x - pt2.x) * (pt1.y - pt2.y)
