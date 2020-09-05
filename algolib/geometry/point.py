# -*- coding: utf-8 -*-
"""Structure of point on a plane or in a space"""
from math import atan2, pi, sqrt


class Point:
    def __init__(self, *coordinates):
        self._coordinates = list(map(float, coordinates))

    @property
    def dims(self):
        return len(self._coordinates)

    @property
    def radius(self):
        """:return: distance between this point from zero point"""
        return sqrt(sum(c * c for c in self._coordinates))

    def __getitem__(self, i):
        if i <= 0 or i > self.dims:
            raise IndexError(f"Coordinate index has to be between 1 and {self.dims}")

        return self._coordinates[i - 1]

    def __hash__(self):
        return hash(self._coordinates)

    def __str__(self):
        return f"({', '.join(map(str, self._coordinates))})"

    def __eq__(self, pt):
        return self._coordinates == pt._coordinates

    def __ne__(self, pt):
        return not self == pt

    def project(self, dimensions):
        if dimensions <= 0:
            raise ValueError("Dimensions count has to be positive")

        if dimensions == len(self._coordinates):
            return self

        if dimensions < len(self._coordinates):
            return Point(*self._coordinates[:dimensions])

        return Point(*(self._coordinates + [0] * (dimensions - self.dims)))


class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def angle_rad(self):
        """:return: angle from X axis in radians (-PI < angle <= PI)"""
        return atan2(self._y, self._x)

    @property
    def angle_deg(self):
        """:return: angle from X axis in degrees (0 <= angle < 360)"""
        return (self.angle_rad * 180.0 / pi) % 360.0

    @property
    def radius(self):
        """:return: distance between this point from zero point"""
        return sqrt(self._x * self._x + self._y * self._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __eq__(self, pt):
        return (self._x, self._y) == (pt.x, pt.y)

    def __ne__(self, pt):
        return not self == pt

    def to_point(self):
        return Point(self._x, self._y)

    @staticmethod
    def from_point(pt):
        if pt.dims != 2:
            raise ValueError("Point should have exactly 2 dimensions")

        return Point2D(pt[1], pt[2])


class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def radius(self):
        """:return: distance between this point from zero point"""
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __hash__(self):
        return hash((self._x, self._y, self._z))

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __eq__(self, pt):
        return (self._x, self._y, self._z) == (pt.x, pt.y, pt.z)

    def __ne__(self, pt):
        return not self == pt

    def to_point(self):
        return Point(self._x, self._y, self._z)

    @staticmethod
    def from_point(pt):
        if pt.dims != 3:
            raise ValueError("Point should have exactly 3 dimensions")

        return Point3D(pt[1], pt[2], pt[3])
