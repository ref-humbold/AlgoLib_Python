# -*- coding: utf-8 -*-
"""Structure of vector on a plane or in a space"""
from math import sqrt
from typing import TypeVar

from .point import Point, Point2D, Point3D


class Vector:
    def __init__(self, *coordinates: float):
        self._coordinates = list(map(float, coordinates))

    @property
    def dims(self) -> int:
        return len(self._coordinates)

    def __getitem__(self, i: int) -> float:
        if i <= 0 or i > self.dims:
            raise IndexError(f"Coordinate index has to be between 1 and {self.dims}")

        return self._coordinates[i - 1]

    def __len__(self) -> float:
        return sqrt(sum(c * c for c in self._coordinates))

    def __hash__(self):
        return hash(self._coordinates)

    def __str__(self):
        return f"[{', '.join(map(str, self._coordinates))}]"

    def __eq__(self, vec: "Vector"):
        return self._coordinates == vec._coordinates

    def __ne__(self, vec: "Vector"):
        return not self == vec

    def __add__(self, vec: "Vector") -> "Vector":
        new_dims = max(self.dims, vec.dims)
        coordinates1 = self._project_coordinates(new_dims)
        coordinates2 = vec._project_coordinates(new_dims)

        return Vector(*(c1 + c2 for c1, c2 in zip(coordinates1, coordinates2)))

    def __iadd__(self, vec: "Vector"):
        for i in range(1, min(vec.dims, self.dims) + 1):
            self._coordinates[i] += vec[i]

        if vec.dims > self.dims:
            for i in range(self.dims + 1, vec.dims + 1):
                self._coordinates.append(vec[i])

        return self

    def __sub__(self, vec: "Vector") -> "Vector":
        new_dims = max(self.dims, vec.dims)
        coordinates1 = self._project_coordinates(new_dims)
        coordinates2 = vec._project_coordinates(new_dims)

        return Vector(*(c1 - c2 for c1, c2 in zip(coordinates1, coordinates2)))

    def __isub__(self, vec: "Vector"):
        for i in range(1, min(vec.dims, self.dims) + 1):
            self._coordinates[i] -= vec[i]

        if vec.dims > self.dims:
            for i in range(self.dims + 1, vec.dims + 1):
                self._coordinates.append(-vec[i])

        return self

    def __mul__(self, constant: float) -> "Vector":
        return Vector(*map(lambda c: c * constant, self._coordinates))

    def __rmul__(self, constant: float):
        return self.__mul__(constant)

    def __imul__(self, constant: float):
        self._coordinates = [c * constant for c in self._coordinates]
        return self

    def __truediv__(self, constant: float) -> "Vector":
        if constant == 0:
            raise ZeroDivisionError()

        return Vector(*map(lambda c: c / constant, self._coordinates))

    def __itruediv__(self, constant: float):
        if constant == 0:
            raise ZeroDivisionError()

        self._coordinates = [c / constant for c in self._coordinates]
        return self

    def project(self, dimensions: int) -> "Vector":
        if dimensions <= 0:
            raise ValueError("Dimensions count has to be positive")

        if dimensions == len(self._coordinates):
            return self

        return Vector(*self._project_coordinates(dimensions))

    def _project_coordinates(self, dimensions):
        if dimensions == len(self._coordinates):
            return self._coordinates

        if dimensions < len(self._coordinates):
            return self._coordinates[:dimensions]

        return self._coordinates + [0] * (dimensions - self.dims)

    @staticmethod
    def between(begin: Point, end: Point) -> "Vector":
        vector_dims = max(begin.dims, end.dims)
        new_begin = begin.project(vector_dims)
        new_end = end.project(vector_dims)

        return Vector(*(new_end[i] - new_begin[i] for i in range(1, vector_dims + 1)))

    @staticmethod
    def dot(vec1: "Vector", vec2: "Vector") -> float:
        new_dims = max(vec1.dims, vec2.dims)
        coordinates1 = vec1._project_coordinates(new_dims)
        coordinates2 = vec2._project_coordinates(new_dims)

        return sum(c1 * c2 for c1, c2 in zip(coordinates1, coordinates2))


class Vector2D:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __len__(self) -> float:
        return sqrt(self._x * self._x + self._y * self._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __str__(self):
        return f"[{self._x}, {self._y}]"

    def __eq__(self, vec: "Vector2D"):
        return (self._x, self._y) == (vec.x, vec.y)

    def __ne__(self, vec: "Vector2D"):
        return not self == vec

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

    def __rmul__(self, constant: float) -> "Vector2D":
        return self.__mul__(constant)

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

    def to_vector(self) -> Vector:
        return Vector(self._x, self._y)

    @staticmethod
    def between(begin: Point2D, end: Point2D) -> "Vector2D":
        return Vector2D(end.x - begin.x, end.y - begin.y)

    @staticmethod
    def from_vector(vec: Vector) -> "Vector2D":
        if vec.dims != 2:
            raise ValueError("Point should have exactly 2 dimensions")

        return Vector2D(vec[1], vec[2])

    @staticmethod
    def dot(vec1: "Vector2D", vec2: "Vector2D") -> float:
        return vec1.x * vec2.x + vec1.y * vec2.y

    @staticmethod
    def area(vec1: "Vector2D", vec2: "Vector2D") -> float:
        return vec1.x * vec2.y - vec1.y * vec2.x


class Vector3D:
    def __init__(self, x: float, y: float, z: float):
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

    def __len__(self) -> float:
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def __hash__(self):
        return hash((self._x, self._y, self._z))

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"

    def __eq__(self, vec: "Vector3D"):
        return (self._x, self._y, self._z) == (vec.x, vec.y, vec.z)

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

    def __rmul__(self, constant: float) -> "Vector3D":
        return self.__mul__(constant)

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

    def to_vector(self) -> Vector:
        return Vector(self._x, self._y, self._z)

    @staticmethod
    def between(begin: Point3D, end: Point3D) -> "Vector3D":
        return Vector3D(end.x - begin.x, end.y - begin.y, end.z - begin.z)

    @staticmethod
    def from_vector(vec: Vector) -> "Vector3D":
        if vec.dims != 3:
            raise ValueError("Point should have exactly 3 dimensions")

        return Vector3D(vec[1], vec[2], vec[3])

    @staticmethod
    def dot(vec1: "Vector3D", vec2: "Vector3D") -> float:
        return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

    @staticmethod
    def cross(vec1: "Vector3D", vec2: "Vector3D") -> "Vector3D":
        return Vector3D(vec1.y * vec2.z - vec1.z * vec2.y, vec1.z * vec2.x - vec1.x * vec2.z,
                        vec1.x * vec2.y - vec1.y * vec2.x)

    @staticmethod
    def area(vec1: "Vector3D", vec2: "Vector3D") -> float:
        return len(Vector3D.cross(vec1, vec2))

    @staticmethod
    def volume(vec1: "Vector3D", vec2: "Vector3D", vec3: "Vector3D") -> float:
        return Vector3D.dot(vec1, Vector3D.cross(vec2, vec3))


TVector = TypeVar("TVector", Vector, Vector2D, Vector3D)
