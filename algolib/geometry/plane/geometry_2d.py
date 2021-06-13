# -*- coding: utf-8 -*-
from math import sqrt
from typing import Iterable, List

from .point_2d import Point2D
from .vector_2d import Vector2D


def sorted_by_x(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts points by their X coordinate.
    Sorting is guaranteed to be stable.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.x)


def sorted_by_y(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts points by their Y coordinate.
    Sorting is guaranteed to be stable.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: pt.y)


def sorted_by_angle(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts 2D points by their polar coordinates.
    First sorts by angle, then by radius.

    :param points: a Iterable of points
    :return: sorted list of points"""
    return sorted(points, key=lambda pt: (pt.angle_deg, pt.radius))


def distance(point1: Point2D, point2: Point2D) -> float:
    return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                + (point2.y - point1.y) * (point2.y - point1.y))


def translate(point: Point2D, vector: Vector2D) -> Point2D:
    return Point2D(point.x + vector.x, point.y + vector.y)
