# -*- coding: utf-8 -*-

from .point import Point2D, Point3D
from .vector import Vector2D, Vector3D


def translate(point, vector):
    if isinstance(point, Point2D) and isinstance(vector, Vector2D):
        return Point2D(point.x + vector.x, point.y + vector.y)

    if isinstance(point, Point3D) and isinstance(vector, Vector3D):
        return Point3D(point.x + vector.x, point.y + vector.y, point.z + vector.z)

    raise TypeError("Inappropriate types of arguments")
