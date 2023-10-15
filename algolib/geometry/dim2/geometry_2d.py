# -*- coding: utf-8 -*-
"""Algorithms for basic geometrical operations in 2D."""
from math import sqrt
from typing import Iterable, List

from .point_2d import Point2D
from .vector_2d import Vector2D


def sorted_by_x(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts given points by their X coordinate. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: pt.x)


def sorted_by_y(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts given points by their Y coordinate. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: pt.y)


def sorted_by_angle(points: Iterable[Point2D]) -> List[Point2D]:
    """Immutably sorts given points by their polar coordinates.
    First sorts by angle, then by radius. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: (pt.angle_deg, pt.radius))


def distance(point1: Point2D, point2: Point2D) -> float:
    """Calculates distance between given points.

    :param point1: the first point
    :param point2: the second point
    :return: the distance between the points"""
    return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                + (point2.y - point1.y) * (point2.y - point1.y))


def translate(point: Point2D, vector: Vector2D) -> Point2D:
    """Translates given point by given vector.

    :param point: the point
    :param vector: the vector of translation
    :return: the translated point"""
    return Point2D(point.x + vector.x, point.y + vector.y)


def reflect(point: Point2D, centre: Point2D) -> Point2D:
    """Reflects given point in another point.

    :param point: the point
    :param centre: the point of reflection
    :return: the reflected point"""
    return Point2D(-point.x + 2 * centre.x, -point.y + 2 * centre.y)
