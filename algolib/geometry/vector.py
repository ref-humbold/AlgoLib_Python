# -*- coding: utf-8 -*-
"""Structure of vector on a plane or in a space"""
from math import sqrt


class Vector:
    def __init__(self, *coordinates):
        self._coordinates = list(map(float, coordinates))

    @property
    def dims(self):
        return len(self._coordinates)

    def __getitem__(self, i):
        if i <= 0 or i > self.dims:
            raise IndexError(f"Coordinate index has to be between 1 and {self.dims}")

        return self._coordinates[i - 1]

    def __len__(self):
        return sqrt(sum(c * c for c in self._coordinates))

    def __hash__(self):
        return hash(self._coordinates)

    def __str__(self):
        return f"[{', '.join(map(str, self._coordinates))}]"

    def __eq__(self, vec):
        return self._coordinates == vec._coordinates

    def __ne__(self, vec):
        return not self == vec

    def __add__(self, vec):
        new_dims = max(self.dims, vec.dims)
        coordinates1 = self._project_coordinates(new_dims)
        coordinates2 = vec._project_coordinates(new_dims)

        return Vector(*(c1 + c2 for c1, c2 in zip(coordinates1, coordinates2)))

    def __iadd__(self, vec):
        for i in range(1, min(vec.dims, self.dims) + 1):
            self._coordinates[i] += vec[i]

        if vec.dims > self.dims:
            for i in range(self.dims + 1, vec.dims + 1):
                self._coordinates.append(vec[i])

        return self

    def __sub__(self, vec):
        new_dims = max(self.dims, vec.dims)
        coordinates1 = self._project_coordinates(new_dims)
        coordinates2 = vec._project_coordinates(new_dims)

        return Vector(*(c1 - c2 for c1, c2 in zip(coordinates1, coordinates2)))

    def __isub__(self, vec):
        for i in range(1, min(vec.dims, self.dims) + 1):
            self._coordinates[i] -= vec[i]

        if vec.dims > self.dims:
            for i in range(self.dims + 1, vec.dims + 1):
                self._coordinates.append(-vec[i])

        return self

    def __mul__(self, constant):
        return Vector(*map(lambda c: c * constant, self._coordinates))

    __rmul__ = __mul__

    def __imul__(self, constant):
        self._coordinates = [c * constant for c in self._coordinates]
        return self

    def __truediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        return Vector(*map(lambda c: c / constant, self._coordinates))

    def __itruediv__(self, constant):
        if constant == 0:
            raise ZeroDivisionError()

        self._coordinates = [c / constant for c in self._coordinates]
        return self

    def project(self, dimensions):
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
    def between(begin, end):
        vector_dims = max(begin.dims, end.dims)
        new_begin = begin.project(vector_dims)
        new_end = end.project(vector_dims)

        return Vector(*(new_end[i] - new_begin[i] for i in range(1, vector_dims + 1)))

    @staticmethod
    def dot(vec1, vec2):
        new_dims = max(vec1.dims, vec2.dims)
        coordinates1 = vec1._project_coordinates(new_dims)
        coordinates2 = vec2._project_coordinates(new_dims)

        return sum(c1 * c2 for c1, c2 in zip(coordinates1, coordinates2))


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
        return hash((self._x, self._y))

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

    __rmul__ = __mul__

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

    def to_vector(self):
        return Vector(self._x, self._y)

    @staticmethod
    def between(begin, end):
        return Vector2D(end.x - begin.x, end.y - begin.y)

    @staticmethod
    def from_vector(vec):
        if vec.dims != 2:
            raise ValueError("Point should have exactly 2 dimensions")

        return Vector2D(vec[1], vec[2])

    @staticmethod
    def dot(vec1, vec2):
        return vec1.x * vec2.x + vec1.y * vec2.y

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
        return hash((self._x, self._y, self._z))

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

    __rmul__ = __mul__

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

    def to_vector(self):
        return Vector(self._x, self._y, self._z)

    @staticmethod
    def between(begin, end):
        return Vector3D(end.x - begin.x, end.y - begin.y, end.z - begin.z)

    @staticmethod
    def from_vector(vec):
        if vec.dims != 3:
            raise ValueError("Point should have exactly 3 dimensions")

        return Vector3D(vec[1], vec[2], vec[3])

    @staticmethod
    def dot(vec1, vec2):
        return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

    @staticmethod
    def cross(vec1, vec2):
        return Vector3D(vec1.y * vec2.z - vec1.z * vec2.y, vec1.z * vec2.x - vec1.x * vec2.z,
                        vec1.x * vec2.y - vec1.y * vec2.x)

    @staticmethod
    def area(vec1, vec2):
        return len(Vector3D.cross(vec1, vec2))

    @staticmethod
    def volume(vec1, vec2, vec3):
        return Vector3D.dot(vec1, Vector3D.cross(vec2, vec3))
