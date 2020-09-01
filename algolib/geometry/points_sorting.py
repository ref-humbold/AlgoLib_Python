# -*- coding: utf-8 -*-
"""Algorithms for points sorting"""


def sorted_by_xy(points):
    """Immutably sorts 2D points with respect to their coordinates.
    First sorts by X coordinate, then by Y coordinate.

    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.x, pt.y)))


def sorted_by_yx(points):
    """Immutably sorts 2D points with respect to their coordinates.
    First sorts by Y coordinate, then by X coordinate.

    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.y, pt.x)))


def sorted_by_xyz(points):
    """Immutably sorts 3D points with respect to their coordinates.
    First sorts by X coordinate, then by Y coordinate, then by Z coordinate.

    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.x, pt.y, pt.z)))


def sorted_by_angle(points):
    """Immutably sorts 2D points with respect to their polar coordinates.
    First sorts by angle, then by radius.

    :param points: a sequence of points
    :return: sorted list of points"""
    return list(sorted(points, key=lambda pt: (pt.angle_deg, pt.radius)))
