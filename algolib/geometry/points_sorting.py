# -*- coding: utf-8 -*-
"""Algorithms for points sorting"""


def sorted_by_dim(i, points):
    """Immutably sorts points by given coordinate index. Sorting is guaranteed to be stable.
    :param i: coordinate index
    :param points: a list of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt[i])


def sorted_by_x(points):
    """Immutably sorts points with respect to their X coordinate.
    Sorting is guaranteed to be stable.

    :param points: a sequence of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.x)


def sorted_by_y(points):
    """Immutably sorts points with respect to their Y coordinate.
    Sorting is guaranteed to be stable.

    :param points: a sequence of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.y)


def sorted_by_z(points):
    """Immutably sorts points with respect to their Z coordinate.
    Sorting is guaranteed to be stable.

    :param points: a sequence of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.z)


def sorted_by_angle(points):
    """Immutably sorts 2D points with respect to their polar coordinates.
    First sorts by angle, then by radius.

    :param points: a sequence of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: (pt.angle_deg, pt.radius))
