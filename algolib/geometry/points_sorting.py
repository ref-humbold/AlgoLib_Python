# -*- coding: utf-8 -*-
"""Points sorting algorithms"""


def angle_sorted(points):
    """Immutably sorts 2D points with respect to their polar coordinates
    First sorts by angle, then by radius.
    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.angle, pt.radius)))


def sorted_by_x(points):
    """Immutably sorts 2D points with respect to their coordinates
    First sorts by X coordinate, then by Y coordinate.
    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points))


def sorted_by_y(points):
    """Immutably sorts 2D points with respect to their coordinates
    First sorts by Y coordinate, then by X coordinate.
    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.y, pt.x)))
