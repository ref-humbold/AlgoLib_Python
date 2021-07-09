# -*- coding: utf-8 -*-
"""Structure of point in 2D"""
from math import atan2, pi, sqrt
from typing import Tuple

from ..geometry_object import GeometryObject


class Point2D(GeometryObject):
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
    def angle_rad(self) -> float:
        """:return: angle from X axis in radians (-PI < angle <= PI)"""
        return atan2(self._y, self._x)

    @property
    def angle_deg(self) -> float:
        """:return: angle from X axis in degrees (0 <= angle < 360)"""
        return (self.angle_rad * 180.0 / pi) % 360.0

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
        return self._are_equal(self._x, pt.x) and self._are_equal(self._y, pt.y)

    def __ne__(self, pt: "Point2D"):
        return not self == pt
