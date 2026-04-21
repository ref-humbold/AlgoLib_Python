# -*- coding: utf-8 -*-
from typing import final


@final
class GeometryComparator:
    __EPSILON = 1e-12

    @classmethod
    def compare(cls, ft1: float, ft2: float) -> int:
        return 0 if abs(ft1 - ft2) < cls.__EPSILON else -1 if ft1 < ft2 else 1
