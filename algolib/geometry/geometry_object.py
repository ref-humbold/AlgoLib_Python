# -*- coding: utf-8 -*-
from abc import ABCMeta


class GeometryObject(metaclass=ABCMeta):
    _EPSILON = 1e-15

    @staticmethod
    def _equal(ft1: float, ft2: float) -> bool:
        return abs(ft1 - ft2) < GeometryObject._EPSILON
