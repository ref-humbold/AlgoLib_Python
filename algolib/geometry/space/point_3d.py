# -*- coding: utf-8 -*-
"""Structure of point on a plane or in a space"""
from math import sqrt

from ..geometry_object import GeometryObject


class Point3D(GeometryObject):
    def __init__(self, x: float, y: float, z: float):
        super().__init__()
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    @property
    def radius(self) -> float:
        """:return: distance of the point from zero point"""
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __hash__(self):
        return hash((self._x, self._y, self._z))

    def __repr__(self):
        return f"Point3D({self._x}, {self._y}, {self._z})"

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __eq__(self, pt: "Point3D"):
        return self._equal(self._x, pt.x) and self._equal(self._y, pt.y) \
               and self._equal(self._z, pt.z)

    def __ne__(self, pt: "Point3D"):
        return not self == pt
