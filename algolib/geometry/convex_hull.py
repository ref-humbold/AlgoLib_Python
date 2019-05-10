# -*- coding: utf-8 -*-
"""Graham's algorithm for convex hull on a plane."""
from .points_sorting import sorted_by_x


def convex_hull(points):
    """Wyznaczanie otoczki wypukłej.
    :param points: lista punktów na płaszczyźnie
    :returns: lista punktów otoczki"""
    def cross_product(pt1, pt2, pt3):
        return (pt1.x - pt2.x) * (pt3.y - pt2.y) - (pt3.x - pt2.x) * (pt1.y - pt2.y)

    points_sorted = sorted_by_x(points)
    hull = points_sorted[:2]

    for point in points_sorted[2:]:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            del hull[-1]

        hull.append(point)

    upper_size = len(hull)

    for point in reversed(points_sorted[:-1]):
        while len(hull) > upper_size and cross_product(hull[-2], hull[-1], point) <= 0:
            del hull[-1]

        hull.append(point)

    return hull[:-1]
