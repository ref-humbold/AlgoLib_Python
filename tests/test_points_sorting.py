# -*- coding: utf-8 -*-
"""Tests: Algorithms for points sorting"""
import unittest

from algolib.geometry import Point2D, sorted_by_angle, sorted_by_x, sorted_by_y


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__sorted_by_angle(self):
        sequence = [
                Point2D(0, 0),
                Point2D(-2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(-2, 3),
                Point2D(3, 2),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(-3, 2)
        ]
        sequence_copy = sequence[:]

        result = sorted_by_angle(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(0, 0),
                Point2D(3, 2),
                Point2D(2, 3),
                Point2D(-2, 3),
                Point2D(-3, 2),
                Point2D(-3, -2),
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(3, -2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_angle__when_argument_is_not_list(self):
        sequence = {
                Point2D(0, 0),
                Point2D(-2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(-2, 3),
                Point2D(3, 2),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(-3, 2)
        }

        result = sorted_by_angle(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(0, 0),
                Point2D(3, 2),
                Point2D(2, 3),
                Point2D(-2, 3),
                Point2D(-3, 2),
                Point2D(-3, -2),
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(3, -2)], result)

    def test__sorted_by_angle__when_all_equal(self):
        sequence = [
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2)
        ]

        result = sorted_by_angle(sequence)

        self.assertListEqual([
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2),
                Point2D(1, 2)], result)

    def test__sorted_by_angle__when_empty_list(self):
        sequence = []

        result = sorted_by_angle(sequence)

        self.assertListEqual([], result)

    def test__sorted_by_x(self):
        sequence = [
                Point2D(0, 0),
                Point2D(-2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(-2, 3),
                Point2D(3, 2),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(-3, 2)
        ]
        sequence_copy = sequence[:]

        result = sorted_by_x(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-3, -2),
                Point2D(-3, 2),
                Point2D(-2, -3),
                Point2D(-2, 3),
                Point2D(0, 0),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(3, -2),
                Point2D(3, 2)], result)
        self.assertListEqual(sequence_copy, sequence)

    def test__sorted_by_y(self):
        sequence = [
                Point2D(0, 0),
                Point2D(-2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(-2, 3),
                Point2D(3, 2),
                Point2D(2, -3),
                Point2D(2, 3),
                Point2D(-3, 2)
        ]
        sequence_copy = sequence[:]

        result = sorted_by_y(sequence)

        self.assertIsInstance(result, list)
        self.assertListEqual([
                Point2D(-2, -3),
                Point2D(2, -3),
                Point2D(-3, -2),
                Point2D(3, -2),
                Point2D(0, 0),
                Point2D(-3, 2),
                Point2D(3, 2),
                Point2D(-2, 3),
                Point2D(2, 3)], result)
        self.assertListEqual(sequence_copy, sequence)
