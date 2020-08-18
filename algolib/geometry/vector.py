# -*- coding: utf-8 -*-
"""Structure of vector on a plane"""
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
        return hash((self._x, self._y, 0x953ee66))

    def __len__(self):
        return sqrt(self._x * self._x + self._y * self._y)

    def __eq__(self, v):
        return (self._x, self._y) == (v.x, v.y)

    def __ne__(self, v):
        return not self == v

    def __str__(self):
        return f"[{self._x}, {self._y}]"

    def __add__(self, v):
        return Vector2D(self._x + v.x, self._y + v.y)

    def __iadd__(self, v):
        self._x += v.x
        self._y += v.y
        return self

    def __sub__(self, v):
        return Vector2D(self._x - v.x, self._y - v.y)

    def __isub__(self, v):
        self._x -= v.x
        self._y -= v.y
        return self

    def __mul__(self, c):
        return Vector2D(self._x * c, self._y * c)

    def __rmul__(self, c):
        return self.__mul__(c)

    def __imul__(self, c):
        self._x *= c
        self._y *= c
        return self

    def __truediv__(self, c):
        if c == 0:
            raise ZeroDivisionError()

        return Vector2D(self._x / c, self._y / c)

    def __itruediv__(self, c):
        if c == 0:
            raise ZeroDivisionError()

        self._x /= c
        self._y /= c
        return self

    def __matmul__(self, v):
        return self._x * v.x + self._y * v.y


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
        return hash((self._x, self._y, self._z, 0x953ee66))

    def __len__(self):
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __eq__(self, v):
        return (self._x, self._y, self._z) == (v.x, v.y, v.z)

    def __ne__(self, v):
        return not self == v

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"

    def __add__(self, v):
        return Vector3D(self._x + v.x, self._y + v.y, self._z + v.z)

    def __iadd__(self, v):
        self._x += v.x
        self._y += v.y
        self._z += v.z
        return self

    def __sub__(self, v):
        return Vector3D(self._x - v.x, self._y - v.y, self._z - v.z)

    def __isub__(self, v):
        self._x -= v.x
        self._y -= v.y
        self._z -= v.z
        return self

    def __mul__(self, c):
        return Vector3D(self._x * c, self._y * c, self._z * c)

    def __rmul__(self, c):
        return self.__mul__(c)

    def __imul__(self, c):
        self._x *= c
        self._y *= c
        self._z *= c
        return self

    def __truediv__(self, c):
        if c == 0:
            raise ZeroDivisionError()

        return Vector3D(self._x / c, self._y / c, self._z / c)

    def __itruediv__(self, c):
        if c == 0:
            raise ZeroDivisionError()

        self._x /= c
        self._y /= c
        self._z /= c
        return self

    def __matmul__(self, v):
        return self._x * v.x + self._y * v.y + self._z * v.z

    def __xor__(self, v):
        return Vector3D(self._y * v.z - self._z * v.y, self._z * v.x - self._x * v.z,
                        self._x * v.y - self._y * v.x)
