# -*- coding: utf-8 -*-
"""Closest pair of points on a plane."""
from math import hypot


def find_closest_points(points):
    """FUNKCJA OBSŁUGUJĄCA DO WYSZUKIWANIA PUNKTÓW
    :param points: lista punktów
    :returns: para najbliższych punktów"""
    points_x = sorted(points)

    return _search_closest(points_x, 0, len(points_x))


def _search_closest(points_x, index_begin, index_end):
    """ZNAJDOWANIE NAJBLIŻSZEJ PARY PUNKTÓW
    :param points_x: lista punktów posortowana po współrzędnej X
    :param index_begin: początek fragmentu listy punktów
    :param index_end: koniec fragmentu listy punktów
    :returns: para najbliższych punktów"""
    if index_end - index_begin == 1:
        return (points_x[index_begin], points_x[index_end])

    if index_end - index_begin == 2:
        return _search_three(points_x[index_begin],
                             points_x[index_begin + 1],
                             points_x[index_end])

    index_middle = (index_begin + index_end) // 2
    middle_x = (points_x[index_middle][0] + points_x[index_middle + 1][0]) // 2

    closest_l = _search_closest(points_x, index_begin, index_middle)
    closest_r = _search_closest(points_x, index_middle + 1, index_end)

    if _distance(closest_l[0], closest_l[1]) <= _distance(closest_r[0], closest_r[1]):
        closest_points = closest_l
        belt_width = _distance(closest_l[0], closest_l[1])
    else:
        closest_points = closest_r
        belt_width = _distance(closest_r[0], closest_r[1])

    belt_points = _check_belt(points_x, middle_x, belt_width)

    if belt_points is not None:
        return belt_points

    return closest_points


def _search_three(point1, point2, point3):
    distance12 = _distance(point1, point2)
    distance23 = _distance(point2, point3)
    distance31 = _distance(point1, point3)

    if distance12 <= distance23 and distance12 <= distance31:
        return (point1, point2)

    if distance23 <= distance12 and distance23 <= distance31:
        return (point2, point3)

    return (point1, point3)


def _check_belt(points_x, middle_x, belt_width):
    """SPRAWDZANIE PUNKTÓW PRZY POŁĄCZENIU POŁÓWEK
    :param points_x: lista punktów posortowana po współrzędnej X
    :param middle_x: współrzędna podziału połówek
    :param belt_width: szerokość paska przy połączeniu
    :returns: najbliższa para punktów w pasku"""
    closest_points = None
    min_distance = belt_width
    belt_points = sorted([p for p in points_x
                          if middle_x - belt_width <= p[0] <= middle_x + belt_width],
                         key=lambda p: (p[1], p[0]))

    for i in range(1, len(belt_points)):
        for j in range(i - 1, -1, -1):
            point1 = belt_points[i]
            point2 = belt_points[j]

            if point2[1] < point1[1] + belt_width:
                break

            if (point1[0] - middle_x) * (point2[0] - middle_x) < 0:
                points_distance = _distance(point1, point2)

                if points_distance < min_distance:
                    min_distance = points_distance
                    closest_points = (point1, point2)

    return closest_points


def _distance(pt1, pt2):
    return hypot(pt1[0] - pt2[0], pt1[1] - pt2[1])
