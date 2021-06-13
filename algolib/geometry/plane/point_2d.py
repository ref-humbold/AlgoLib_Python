# -*- coding: utf-8 -*-
"""Structure of point on a plane or in a space"""
from math import atan2, pi, sqrt


class Point2D:
    def __init__(self, x: float, y: float):
        self._x = round(x, 6)
        self._y = round(y, 6)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

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
        return (self._x, self._y) == (pt.x, pt.y)

    def __ne__(self, pt: "Point2D"):
        return not self == pt
