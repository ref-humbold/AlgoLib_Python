# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Tuple


class GeometryObject(metaclass=ABCMeta):
    EPSILON = 1e-12

    @property
    @abstractmethod
    def coordinates(self) -> Tuple[float, ...]:
        pass

    @staticmethod
    def _are_equal(ft1: float, ft2: float) -> bool:
        return abs(ft1 - ft2) < GeometryObject.EPSILON
