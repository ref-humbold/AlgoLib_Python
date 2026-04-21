# -*- coding: utf-8 -*-
"""Structure of point in 2D."""
from math import atan2, sqrt
from typing import Tuple

from .angle import Angle, AngleUnit
from ..geometry_comparator import GeometryComparator


class Point2D:
    __COMPARATOR = GeometryComparator()

    def __init__(self, x: float, y: float):
        super().__init__()
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def coordinates(self) -> Tuple[float, ...]:
        return self._x, self._y

    @property
    def angle(self) -> Angle:
        """:return: angle from X axis"""
        return Angle(atan2(self._y, self._x), AngleUnit.RADIANS)

    @property
    def radius(self) -> float:
        """:return: distance of the point from zero point"""
        return sqrt(self._x * self._x + self._y * self._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __repr__(self):
        return f"Point2D({self._x}, {self._y})"

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __eq__(self, pt: "Point2D"):
        return self.__COMPARATOR.compare(self._x, pt.x) == 0 and self.__COMPARATOR.compare(
                self._y, pt.y) == 0

    def __ne__(self, pt: "Point2D"):
        return not self == pt
