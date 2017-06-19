# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZJĄCY OTOCZKĘ WYPUKŁĄ PUNKTÓW NA PŁASZCZYŹNIE"""


def convex_hull(points):
    """Wyznaczanie otoczki wypukłej.
    :param points: lista punktów na płaszczyźnie
    :returns: lista punktów otoczki"""
    def cross_product(pt1, pt2, pt3):
        return (pt1[0] - pt2[0]) * (pt3[1] - pt2[1]) - (pt3[0] - pt2[0]) * (pt1[1] - pt2[1])

    points_sorted = sorted(points)
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
