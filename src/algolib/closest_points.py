# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZANIA NAJBLIŻSZEJ PARY PUNKTÓW NA PŁASZCZYŹNIE"""
from math import hypot


def find_closest_points(points):
    """FUNKCJA OBSŁUGUJĄCA DO WYSZUKIWANIA PUNKTÓW
    :param points: lista punktów
    :returns: para najbliższych punktów"""
    points_x = sorted(points)
    points_y = [(pt[0], pt[1], i) for i, pt in enumerate(points_x)]
    points_y.sort(key=lambda p: (p[1], p[0], p[2]), reverse=True)

    return _search_closest(points_x, points_y)


def _search_closest(points_x, points_y, index_begin=0, index_end=-1):
    """ZNAJDOWANIE NAJBLIŻSZEJ PARY PUNKTÓW
    :param points_x: lista punktów posortowana po współrzędnej x
    :param points_y: lista punktów posortowana po współrzędnej y
    :param index_begin: początek fragmentu listy punktów po x
    :param index_end: koniec fragmentu listy punktów po x
    :returns: para najbliższych punktów"""
    index_begin %= len(points_x)
    index_end %= len(points_x)

    if index_end - index_begin == 1:
        return (points_x[index_begin][0], points_x[index_end][0])

    if index_end - index_begin == 2:
        index_middle = index_begin + 1
        distance12 = distance(points_x[index_begin], points_x[index_middle])
        distance23 = distance(points_x[index_middle], points_x[index_end])
        distance31 = distance(points_x[index_begin], points_x[index_end])

        if distance12 <= distance23 and distance12 <= distance31:
            return (points_x[index_begin][0], points_x[index_middle][0])
        elif distance23 <= distance12 and distance23 <= distance31:
            return (points_x[index_middle][0], points_x[index_end][0])
        else:
            return (points_x[index_begin][0], points_x[index_end][0])

    index_middle = (index_begin + index_end) // 2
    middle_x = (points_x[index_middle][0] + points_x[index_middle + 1][0]) // 2
    points_yl = [p for p in points_y if p[2] <= index_middle]
    points_yr = [p for p in points_y if p[2] > index_middle]

    closest_l = _search_closest(points_x, points_yl, index_begin, index_middle)
    closest_r = _search_closest(
        points_x, points_yr, index_middle + 1, index_end)
    min_distance = min(distance(closest_l[0], closest_l[1]), distance(
        closest_r[0], closest_r[1]))
    belt_width = min_distance
    belt_points = [(i, pt[2] <= index_middle) for i, pt in enumerate(points_y)
                   if middle_x - belt_width <= pt[0] <= middle_x + belt_width]

    for i in range(1, len(belt_points)):
        for j in range(i - 1, -1, -1):
            pt1 = belt_points[i][0]
            pt2 = belt_points[j][0]

            if points_y[pt2][1] < points_y[pt1][1] + belt_width:
                break

            if belt_points[i][1] != belt_points[j][1]:
                points_distance = distance(points_y[pt1], points_y[pt2])

                if points_distance < min_distance:
                    min_distance = points_distance
                    closest_points = (points_y[pt1], points_y[pt2])

    return closest_points


def distance(pt1, pt2):
    """Wyznaczanie odległości punktów od siebie
    :param pt1: punkt 1
    :param pt2: punkt 2
    :returns: odległość między punktami"""
    return hypot(pt1[0] - pt2[0], pt1[1] - pt2[1])
