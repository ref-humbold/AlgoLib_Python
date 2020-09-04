# -*- coding: utf-8 -*-
"""Structure of vector on a plane or in a space"""
from math import sqrt


class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __hash__(self):
        return hash((self._x, self._y, 0x9e3d79b9))

    def __str__(self):
        return f"[{self._x}, {self._y}]"

    def __len__(self):
        return sqrt(self._x * self._x + self._y * self._y)

    def __eq__(self, vec):
        return (self._x, self._y) == (vec.x, vec.y)

    def __ne__(self, vec):
        return not self == vec

    def __add__(self, vec):
        return Vector2D(self._x + vec.x, self._y + vec.y)

    def __iadd__(self, vec):
        self._x += vec.x
        self._y += vec.y
        return self

    def __sub__(self, vec):
        return Vector2D(self._x - vec.x, self._y - vec.y)

    def __isub__(self, vec):
        self._x -= vec.x
        self._y -= vec.y
        return self

    def __mul__(self, constant):
        return Vector2D(self._x * constant, self._y * constant)

    def __rmul__(self, constant):
        return self.__mul__(constant)

    def __imul__(self, constant):
        self._x *= constant
        self._y *= constant
        return self

    def __truediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        return Vector2D(self._x / constant, self._y / constant)

    def __itruediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        self._x /= constant
        self._y /= constant
        return self

    def __matmul__(self, vec):
        return self._x * vec.x + self._y * vec.y

    @staticmethod
    def area(vec1, vec2):
        return vec1.x * vec2.y - vec1.y * vec2.x


class Vector3D:
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

    def __hash__(self):
        return hash((self._x, self._y, self._z, 0x9e3d79b9))

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"

    def __len__(self):
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __eq__(self, vec):
        return (self._x, self._y, self._z) == (vec.x, vec.y, vec.z)

    def __ne__(self, vec):
        return not self == vec

    def __add__(self, vec):
        return Vector3D(self._x + vec.x, self._y + vec.y, self._z + vec.z)

    def __iadd__(self, vec):
        self._x += vec.x
        self._y += vec.y
        self._z += vec.z
        return self

    def __sub__(self, vec):
        return Vector3D(self._x - vec.x, self._y - vec.y, self._z - vec.z)

    def __isub__(self, vec):
        self._x -= vec.x
        self._y -= vec.y
        self._z -= vec.z
        return self

    def __mul__(self, constant):
        return Vector3D(self._x * constant, self._y * constant, self._z * constant)

    def __rmul__(self, constant):
        return self.__mul__(constant)

    def __imul__(self, constant):
        self._x *= constant
        self._y *= constant
        self._z *= constant
        return self

    def __truediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        return Vector3D(self._x / constant, self._y / constant, self._z / constant)

    def __itruediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        self._x /= constant
        self._y /= constant
        self._z /= constant
        return self

    def __matmul__(self, vec):
        return self._x * vec.x + self._y * vec.y + self._z * vec.z

    def __xor__(self, vec):
        return Vector3D(self._y * vec.z - self._z * vec.y, self._z * vec.x - self._x * vec.z,
                        self._x * vec.y - self._y * vec.x)

    @staticmethod
    def area(vec1, vec2):
        return len(vec1 ^ vec2)

    @staticmethod
    def volume(vec1, vec2, vec3):
        return vec1 @ (vec2 ^ vec3)
