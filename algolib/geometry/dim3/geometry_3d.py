# -*- coding: utf-8 -*-
"""Algorithms for basic geometrical operations in 3D."""
from math import sqrt
from typing import Iterable, List

from .point_3d import Point3D
from .vector_3d import Vector3D


def sorted_by_x(points: Iterable[Point3D]) -> List[Point3D]:
    """Immutably sorts given points by their X coordinate. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: pt.x)


def sorted_by_y(points: Iterable[Point3D]) -> List[Point3D]:
    """Immutably sorts given points by their Y coordinate. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: pt.y)


def sorted_by_z(points: Iterable[Point3D]) -> List[Point3D]:
    """Immutably sorts given points by their Z coordinate. Sorting is guaranteed to be stable.

    :param points: the points
    :return: the sorted points"""
    return sorted(points, key=lambda pt: pt.z)


def distance(point1: Point3D, point2: Point3D) -> float:
    """Calculates distance between given points.

    :param point1: the first point
    :param point2: the second point
    :return: the distance between the points"""
    return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                + (point2.y - point1.y) * (point2.y - point1.y)
                + (point2.z - point1.z) * (point2.z - point1.z))


def translate(point: Point3D, vector: Vector3D) -> Point3D:
    """Translates given point by given vector.

    :param point: the point
    :param vector: the vector of translation
    :return: the translated point"""
    return Point3D(point.x + vector.x, point.y + vector.y, point.z + vector.z)


def reflect(point: Point3D, centre: Point3D) -> Point3D:
    """Reflects given point in another point.

    :param point: the point
    :param centre: the point of reflection
    :return: the reflected point"""
    return Point3D(-point.x + 2 * centre.x, -point.y + 2 * centre.y, -point.z + 2 * centre.z)
