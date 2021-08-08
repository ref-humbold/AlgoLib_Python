# -*- coding: utf-8 -*-
"""Structure of vector in 2D"""
from math import sqrt
from typing import Tuple

from .point_2d import Point2D
from ..geometry_object import GeometryObject


class Vector2D(GeometryObject):
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
    def length(self) -> float:
        return sqrt(self._x * self._x + self._y * self._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, vec: "Vector2D"):
        return self._are_equal(self._x, vec.x) and self._are_equal(self._y, vec.y)

    def __ne__(self, vec: "Vector2D"):
        return not self == vec

    def __repr__(self):
        return f"Vector2D({self._x}, {self._y})"

    def __str__(self):
        return f"[{self._x}, {self._y}]"

    def __pos__(self):
        return Vector2D(+self._x, +self._y)

    def __neg__(self):
        return Vector2D(-self._x, -self._y)

    def __add__(self, vec: "Vector2D") -> "Vector2D":
        return Vector2D(self._x + vec.x, self._y + vec.y)

    def __iadd__(self, vec: "Vector2D"):
        self._x += vec.x
        self._y += vec.y
        return self

    def __sub__(self, vec: "Vector2D") -> "Vector2D":
        return Vector2D(self._x - vec.x, self._y - vec.y)

    def __isub__(self, vec: "Vector2D"):
        self._x -= vec.x
        self._y -= vec.y
        return self

    def __mul__(self, constant: float) -> "Vector2D":
        return Vector2D(self._x * constant, self._y * constant)

    __rmul__ = __mul__

    def __imul__(self, constant: float):
        self._x *= constant
        self._y *= constant
        return self

    def __truediv__(self, constant: float) -> "Vector2D":
        if constant == 0:
            raise ZeroDivisionError()

        return Vector2D(self._x / constant, self._y / constant)

    def __itruediv__(self, constant: float) -> "Vector2D":
        if constant == 0:
            raise ZeroDivisionError()

        self._x /= constant
        self._y /= constant
        return self

    @staticmethod
    def between(begin: Point2D, end: Point2D) -> "Vector2D":
        return Vector2D(end.x - begin.x, end.y - begin.y)

    @staticmethod
    def dot(vec1: "Vector2D", vec2: "Vector2D") -> float:
        return vec1.x * vec2.x + vec1.y * vec2.y

    @staticmethod
    def area(vec1: "Vector2D", vec2: "Vector2D") -> float:
        return vec1.x * vec2.y - vec1.y * vec2.x
