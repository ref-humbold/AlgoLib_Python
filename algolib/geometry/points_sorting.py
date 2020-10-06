# -*- coding: utf-8 -*-
"""Algorithms for points sorting"""
from typing import Iterable, List, Union

from .point import Point, Point2D, Point3D


def sorted_by_dim(i: int, points: Iterable[Point]) -> List[Point]:
    """Immutably sorts points by given coordinate index. Sorting is guaranteed to be stable.
    :param i: coordinate index
    :param points: a list of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt[i])


def sorted_by_x(points: Iterable[Union[Point2D, Point3D]]) -> List[Union[Point2D, Point3D]]:
    """Immutably sorts points by their X coordinate.
    Sorting is guaranteed to be stable.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.x)


def sorted_by_y(points: Iterable[Union[Point2D, Point3D]]) -> List[Union[Point2D, Point3D]]:
    """Immutably sorts points by their Y coordinate.
    Sorting is guaranteed to be stable.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.y)


def sorted_by_z(points: Iterable[Point3D]) -> List[Point3D]:
    """Immutably sorts points by their Z coordinate.
    Sorting is guaranteed to be stable.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.z)


def sorted_by_angle(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts 2D points by their polar coordinates.
    First sorts by angle, then by radius.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: (pt.angle_deg, pt.radius))
