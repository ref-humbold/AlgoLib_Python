# -*- coding: utf-8 -*-
"""Algorithm for searching pair of closest points in 2D."""
from typing import Iterable, Tuple

from .geometry_2d import distance, sorted_by_x, sorted_by_y
from .point_2d import Point2D


def find_closest_points(points: Iterable[Point2D]) -> Tuple[Point2D, Point2D]:
    """Searches for the pair of closest points among given points.

    :param points: the points
    :return: the pair of closest points
    :exception ValueError: if no points specified"""
    points = list(points)

    if len(points) == 0:
        raise ValueError("Sequence contains no points")

    points_x = sorted_by_x(points)
    points_y = sorted_by_y(points)
    return _search_closest(points_x, points_y, 0, len(points))


def _search_closest(points_x, points_y, index_begin, index_end):
    # Searches for closest points in given sublist of points.
    # Points are given sorted by X coordinate and by Y coordinate.
    if index_end - index_begin <= 2:
        return points_x[index_begin], points_x[index_end - 1]

    if index_end - index_begin == 3:
        return _search_three(points_x[index_begin], points_x[index_begin + 1],
                             points_x[index_begin + 2])

    index_middle = (index_begin + index_end) // 2
    middle_x = (points_x[index_middle - 1].x + points_x[index_middle].x) // 2
    closest_left = _search_closest(points_x, (p for p in points_y if p.x < middle_x), index_begin,
                                   index_middle)
    closest_right = _search_closest(points_x, (p for p in points_y if p.x >= middle_x),
                                    index_middle, index_end)
    closest_points = \
        closest_left if distance(*closest_left) <= distance(*closest_right) else closest_right
    belt_points = _check_belt(points_y, middle_x, distance(closest_points[0], closest_points[1]))
    return belt_points if belt_points is not None else closest_points


def _check_belt(points_y, middle_x, width):
    # Searches for closest points inside a belt of given width.
    # The resulting distance should not be less than belt width.
    closest_points = None
    min_distance = width
    belt_points = [p for p in points_y if middle_x - width <= p.x <= middle_x + width]

    for i, point1 in enumerate(belt_points):
        for j in range(i + 1, len(belt_points)):
            point2 = belt_points[j]

            if point2.y > point1.y + width:
                break

            if point1.x <= middle_x < point2.x or point2.x <= middle_x < point1.x:
                points_distance = distance(point1, point2)

                if points_distance < min_distance:
                    min_distance = points_distance
                    closest_points = tuple(sorted_by_x([point1, point2]))

    return closest_points


def _search_three(point1, point2, point3):
    # Searches for closest points among three of them.
    distance12 = distance(point1, point2)
    distance23 = distance(point2, point3)
    distance31 = distance(point3, point1)

    if distance23 >= distance12 <= distance31:
        return point1, point2

    if distance12 >= distance23 <= distance31:
        return point2, point3

    return point1, point3
