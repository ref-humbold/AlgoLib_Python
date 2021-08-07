# -*- coding: utf-8 -*-
"""Algorithm for pair of closest points on a plane"""
from typing import Iterable, Optional, Tuple

from .geometry import distance
from .point import Point2D
from .points_sorting import sorted_by_x, sorted_by_y


def find_closest_points(points: Iterable[Point2D]) -> Tuple[Point2D, Point2D]:
    """Searches for closest points among specified points.

    :param points: an iterable of points
    :return: pair of closest points"""
    points = list(points)
    points_x = sorted_by_x(points)
    points_y = sorted_by_y(points)
    return _search_closest(points_x, points_y, 0, len(points))


def _search_closest(points_x, points_y, index_begin, index_end):
    # Searches for a pair of closest points in specified sublist of points.
    # Points are specified sorted by X coordinate and by Y coordinate.
    # (index_begin inclusive, index_end exclusive)
    if index_end - index_begin <= 2:
        return points_x[index_begin], points_x[index_end - 1]

    if index_end - index_begin == 3:
        return _search_three(points_x[index_begin], points_x[index_begin + 1],
                             points_x[index_end - 1])

    index_middle = (index_begin + index_end) // 2
    middle_x = (points_x[index_middle].x + points_x[index_middle + 1].x) // 2
    closest_left = _search_closest(points_x, (p for p in points_y if p.x <= middle_x), index_begin,
                                   index_middle + 1)
    closest_right = _search_closest(points_x, (p for p in points_y if p.x > middle_x), index_middle,
                                    index_end)
    closest_points = \
        closest_left if distance(*closest_left) <= distance(*closest_right) else closest_right
    belt_points = _check_belt(points_y, middle_x, distance(closest_points[0], closest_points[1]))
    return belt_points if belt_points is not None else closest_points


def _check_belt(points_y: Iterable[Point2D], middle_x: float, belt_width: float) \
        -> Optional[Tuple[Point2D, Point2D]]:
    # Finds closest pair inside a belt of specified width.
    # The resulting distance should not be less than belt width.
    closest_points = None
    min_distance = belt_width
    belt_points = [p for p in points_y if middle_x - belt_width <= p.x <= middle_x + belt_width]

    for i in range(1, len(belt_points)):
        for j in range(i + 1, len(belt_points)):
            point1 = belt_points[i]
            point2 = belt_points[j]

            if point2.y > point1.y + belt_width:
                break

            if point1.x <= middle_x < point2.x or point2.x <= middle_x < point1.x:
                points_distance = distance(point1, point2)

                if points_distance < min_distance:
                    min_distance = points_distance
                    closest_points = tuple(sorted_by_x([point1, point2]))

    return closest_points


def _search_three(point1, point2, point3):
    # Finds closest pair of points among three of them.
    distance12 = distance(point1, point2)
    distance23 = distance(point2, point3)
    distance31 = distance(point1, point3)

    if distance23 >= distance12 <= distance31:
        return point1, point2

    if distance12 >= distance23 <= distance31:
        return point2, point3

    return point1, point3
