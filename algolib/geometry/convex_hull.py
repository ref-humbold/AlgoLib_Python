# -*- coding: utf-8 -*-
"""Graham's algorithm for convex hull on a plane."""
from .points_sorting import sorted_by_x


def convex_hull(points):
    """Constructs convex hull of set of points.
    :param points: sequence of points
    :returns: hull points list"""

    points = sorted_by_x(points)
    hull = points[:2]

    for point in points[2:]:
        _add_point(point, hull, 1)

    upper_size = len(hull)

    for point in reversed(points[:-1]):
        _add_point(point, hull, upper_size)

    hull.pop()

    return hull


def _add_point(point, hull, min_size):
    while len(hull) > min_size and _cross_product(hull[-2], hull[-1], point) <= 0:
        hull.pop()

    hull.append(point)


def _cross_product(pt1, pt2, pt3):
    return (pt1.x - pt2.x) * (pt3.y - pt2.y) - (pt3.x - pt2.x) * (pt1.y - pt2.y)
