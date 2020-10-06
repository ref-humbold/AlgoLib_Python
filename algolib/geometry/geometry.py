# -*- coding: utf-8 -*-
from math import sqrt

from .point import Point, Point2D, Point3D, PointType
from .vector import Vector2D, Vector3D, VectorType


def distance(point1: PointType, point2: PointType) -> float:
    if isinstance(point1, Point2D) and isinstance(point2, Point2D):
        return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                    + (point2.y - point1.y) * (point2.y - point1.y))

    if isinstance(point1, Point3D) and isinstance(point2, Point3D):
        return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                    + (point2.y - point1.y) * (point2.y - point1.y)
                    + (point2.z - point1.z) * (point2.z - point1.z))

    new_dims = max(point1.dims, point2.dims)
    pt1 = point1.project(new_dims)
    pt2 = point2.project(new_dims)

    return sqrt(sum(map(lambda c: c * c, [pt2[i] - pt1[i] for i in range(1, new_dims + 1)])))


def translate(point: PointType, vector: VectorType) -> PointType:
    if isinstance(point, Point2D) and isinstance(vector, Vector2D):
        return Point2D(point.x + vector.x, point.y + vector.y)

    if isinstance(point, Point3D) and isinstance(vector, Vector3D):
        return Point3D(point.x + vector.x, point.y + vector.y, point.z + vector.z)

    new_dims = max(point.dims, vector.dims)
    pt = point.project(new_dims)
    vec = vector.project(new_dims)

    return Point(*(pt[i] + vec[i] for i in range(1, new_dims + 1)))
