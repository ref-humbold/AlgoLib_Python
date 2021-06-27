# -*- coding: utf-8 -*-
"""Structure of vector in 3D"""
from math import sqrt

from .point_3d import Point3D
from ..geometry_object import GeometryObject


class Vector3D(GeometryObject):
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
    def length(self) -> float:
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __hash__(self):
        return hash((self._x, self._y, self._z))

    def __repr__(self):
        return f"Vector3D({self._x}, {self._y}, {self._z})"

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"

    def __eq__(self, vec: "Vector3D"):
        return self._equal(self._x, vec.x) and self._equal(self._y, vec.y) \
               and self._equal(self._z, vec.z)

    def __ne__(self, vec: "Vector3D"):
        return not self == vec

    def __add__(self, vec: "Vector3D") -> "Vector3D":
        return Vector3D(self._x + vec.x, self._y + vec.y, self._z + vec.z)

    def __iadd__(self, vec: "Vector3D"):
        self._x += vec.x
        self._y += vec.y
        self._z += vec.z
        return self

    def __sub__(self, vec: "Vector3D") -> "Vector3D":
        return Vector3D(self._x - vec.x, self._y - vec.y, self._z - vec.z)

    def __isub__(self, vec: "Vector3D"):
        self._x -= vec.x
        self._y -= vec.y
        self._z -= vec.z
        return self

    def __mul__(self, constant: float) -> "Vector3D":
        return Vector3D(self._x * constant, self._y * constant, self._z * constant)

    __rmul__ = __mul__

    def __imul__(self, constant: float):
        self._x *= constant
        self._y *= constant
        self._z *= constant
        return self

    def __truediv__(self, constant: float) -> "Vector3D":
        if constant == 0:
            raise ZeroDivisionError()

        return Vector3D(self._x / constant, self._y / constant, self._z / constant)

    def __itruediv__(self, constant: float):
        if constant == 0:
            raise ZeroDivisionError()

        self._x /= constant
        self._y /= constant
        self._z /= constant
        return self

    @staticmethod
    def between(begin: Point3D, end: Point3D) -> "Vector3D":
        return Vector3D(end.x - begin.x, end.y - begin.y, end.z - begin.z)

    @staticmethod
    def dot(vec1: "Vector3D", vec2: "Vector3D") -> float:
        return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

    @staticmethod
    def cross(vec1: "Vector3D", vec2: "Vector3D") -> "Vector3D":
        return Vector3D(vec1.y * vec2.z - vec1.z * vec2.y, vec1.z * vec2.x - vec1.x * vec2.z,
                        vec1.x * vec2.y - vec1.y * vec2.x)

    @staticmethod
    def area(vec1: "Vector3D", vec2: "Vector3D") -> float:
        return Vector3D.cross(vec1, vec2).length

    @staticmethod
    def volume(vec1: "Vector3D", vec2: "Vector3D", vec3: "Vector3D") -> float:
        return Vector3D.dot(vec1, Vector3D.cross(vec2, vec3))
