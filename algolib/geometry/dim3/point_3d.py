# -*- coding: utf-8 -*-
"""Structure of point in 3D."""
from math import sqrt
from typing import Tuple

from ..geometry_comparator import GeometryComparator


class Point3D:
    __COMPARATOR = GeometryComparator()

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
    def coordinates(self) -> Tuple[float, ...]:
        return self._x, self._y, self._z

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
        return self.__COMPARATOR.compare(self._x, pt.x) == 0 and self.__COMPARATOR.compare(
                self._y, pt.y) == 0 and self.__COMPARATOR.compare(self._z, pt.z) == 0

    def __ne__(self, pt: "Point3D"):
        return not self == pt
