# -*- coding: utf-8 -*-
"""Structure of point on a plane"""
from math import atan2, pi, sqrt


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
        return hash((self._x, self._y, 0x933ff53))

    def __eq__(self, p):
        return (self._x, self._y) == (p.x, p.y)

    def __ne__(self, p):
        return not self == p

    def __str__(self):
        return f"({self._x}, {self._y})"
