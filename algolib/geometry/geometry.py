# -*- coding: utf-8 -*-

from math import sqrt

from .point import Point2D, Point3D
from .vector import Vector2D, Vector3D


def make_vector(begin, end):
    if isinstance(begin, Point2D) and isinstance(end, Point2D):
        return Vector2D(end.x - begin.x, end.y - begin.y)

    if isinstance(begin, Point3D) and isinstance(end, Point3D):
        return Vector3D(end.x - begin.x, end.y - begin.y, end.z - begin.z)

    raise TypeError("Inappropriate types of arguments")


def distance(point1, point2):
    if isinstance(point1, Point2D) and isinstance(point2, Point2D):
        return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                    + (point2.y - point1.y) * (point2.y - point1.y))

    if isinstance(point1, Point3D) and isinstance(point2, Point3D):
        return sqrt((point2.x - point1.x) * (point2.x - point1.x)
                    + (point2.y - point1.y) * (point2.y - point1.y)
                    + (point2.z - point1.z) * (point2.z - point1.z))

    raise TypeError("Inappropriate types of arguments")


def translate(point, vector):
    if isinstance(point, Point2D) and isinstance(vector, Vector2D):
        return Point2D(point.x + vector.x, point.y + vector.y)

    if isinstance(point, Point3D) and isinstance(vector, Vector3D):
        return Point3D(point.x + vector.x, point.y + vector.y, point.z + vector.z)

    raise TypeError("Inappropriate types of arguments")
