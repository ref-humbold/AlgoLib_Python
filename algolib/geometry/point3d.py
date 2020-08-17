# -*- coding: utf-8 -*-
"""Structure of point in a space"""
from math import sqrt


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
        return hash((self._x, self._y, 0x933ff53))

    def __eq__(self, p):
        return (self._x, self._y, self._z) == (p.x, p.y, p.z)

    def __ne__(self, p):
        return not self == p

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"
