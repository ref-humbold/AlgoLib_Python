# -*- coding: utf-8 -*-
"""Closest pair of points on a plane"""
from math import hypot

from .points_sorting import sorted_by_x, sorted_by_y


def find_closest_points(points):
    """FUNKCJA OBSŁUGUJĄCA DO WYSZUKIWANIA PUNKTÓW
    :param points: lista punktów
    :return: para najbliższych punktów"""
    points_x = sorted_by_x(points)
    points_y = sorted_by_y(points)
    return _search_closest(points_x, points_y, 0, len(points))


def _search_closest(points_x, points_y, index_begin, index_end):
    """ZNAJDOWANIE NAJBLIŻSZEJ PARY PUNKTÓW
    :param points_x: lista punktów posortowana po współrzędnej X
    :param points_y: generator punktów posortowanych po współrzędnej Y
    :param index_begin: początek fragmentu listy punktów
    :param index_end: koniec fragmentu listy punktów
    :return: para najbliższych punktów"""
    if index_end - index_begin == 1:
        return points_x[index_begin], points_x[index_end]

    if index_end - index_begin == 2:
        return _search_three(points_x[index_begin], points_x[index_begin + 1], points_x[index_end])

    index_middle = (index_begin + index_end) // 2
    middle_x = (points_x[index_middle].x + points_x[index_middle + 1].x) // 2
    closest_l = _search_closest(points_x, (p for p in points_y if p.x <= middle_x), index_begin,
                                index_middle)
    closest_r = _search_closest(points_x, (p for p in points_y if p.x > middle_x), index_middle + 1,
                                index_end)

    if _distance(closest_l.x, closest_l.y) <= _distance(closest_r.x, closest_r.y):
        closest_points = closest_l
        belt_width = _distance(closest_l.x, closest_l.y)
    else:
        closest_points = closest_r
        belt_width = _distance(closest_r.x, closest_r.y)

    belt_points = _check_belt(points_y, middle_x, belt_width)
    return belt_points if belt_points is not None else closest_points


def _check_belt(points_y, middle_x, belt_width):
    """SPRAWDZANIE PUNKTÓW PRZY POŁĄCZENIU POŁÓWEK
    :param points_y: generator punktów posortowanych po współrzędnej Y
    :param middle_x: współrzędna podziału połówek
    :param belt_width: szerokość paska przy połączeniu
    :return: najbliższa para punktów w pasku"""
    closest_points = None
    min_distance = belt_width
    belt_points = [p for p in points_y if middle_x - belt_width <= p.x <= middle_x + belt_width]

    for i in range(1, len(belt_points)):
        for j in range(i + 1, len(belt_points)):
            point1 = belt_points[i]
            point2 = belt_points[j]

            if point2.y > point1.y + belt_width:
                break

            if point1.x <= middle_x < point2.x or point2.x <= middle_x < point1:
                points_distance = _distance(point1, point2)

                if points_distance < min_distance:
                    min_distance = points_distance
                    closest_points = (point1, point2)

    return closest_points


def _search_three(point1, point2, point3):
    distance12 = _distance(point1, point2)
    distance23 = _distance(point2, point3)
    distance31 = _distance(point1, point3)

    if distance23 >= distance12 <= distance31:
        return point1, point2

    if distance12 >= distance23 <= distance31:
        return point2, point3

    return point1, point3


def _distance(pt1, pt2):
    return hypot(pt1.x - pt2.x, pt1.y - pt2.y)
