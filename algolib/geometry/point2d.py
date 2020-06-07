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
    def angle_deg(self):
        """:return: angle from X axis in degrees (0 <= angle < 360)"""
        return (self.angle_rad * 180.0 / pi) % 360.0

    @property
    def angle_rad(self):
        """:return: angle from X axis in radians (-PI < angle <= PI)"""
        return atan2(self._y, self._x)

    @property
    def radius(self):
        """:return: distance between this point from zero point"""
        return sqrt(self._x**2 + self._y**2)

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, pt):
        return (self._x, self._y) == (pt.x, pt.y)

    def __ne__(self, pt):
        return not self == pt

    def __lt__(self, pt):
        return (self._x, self._y) < (pt.x, pt.y)

    def __le__(self, pt):
        return (self._x, self._y) <= (pt.x, pt.y)

    def __gt__(self, pt):
        return not self <= pt

    def __ge__(self, pt):
        return not self < pt

    def __str__(self):
        return f"({self._x}, {self._y})"
