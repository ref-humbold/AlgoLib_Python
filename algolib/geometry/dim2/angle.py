# -*- coding: utf-8 -*-
from enum import Enum
import math

from ..geometry_comparator import GeometryComparator


class AngleUnit(Enum):
    DEGREES = "deg"
    RADIANS = "rad"


class Angle:
    __COMPARATOR = GeometryComparator()
    _FULL_ANGLE_DEG = 360.0

    def __init__(self, value: float, unit: AngleUnit):
        match unit:
            case AngleUnit.DEGREES:
                self._degrees = value % self._FULL_ANGLE_DEG
            case AngleUnit.RADIANS:
                self._degrees = math.degrees(value) % self._FULL_ANGLE_DEG

    @property
    def degrees(self) -> float:
        return self._degrees

    @property
    def radians(self) -> float:
        return math.radians(self._degrees)

    def __hash__(self):
        return hash(self.degrees)

    def __eq__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) == 0

    def __ne__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) != 0

    def __lt__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) < 0

    def __le__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) <= 0

    def __gt__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) > 0

    def __ge__(self, angle: "Angle"):
        return self.__COMPARATOR.compare(self.degrees, angle.degrees) >= 0

    def __repr__(self):
        return f"Angle({self._degrees!r}, {AngleUnit.DEGREES!s})"

    __str__ = __repr__
