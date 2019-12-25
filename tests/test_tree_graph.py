# -*- coding: utf-8 -*-
"""Tests: Tree graphs structure."""
import unittest

from algolib.graphs import CycleError, NotConnectedError, TreeGraph


class TreeGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = TreeGraph(10, [(0, 6), (1, 2), (2, 3), (3, 4), (4, 5), (6, 4), (7, 3),
                                           (8, 3), (9, 7)])

    def tearDown(self):
        self._test_object = None

    def test__add_vertex__when_one_neighbour(self):
        result = self._test_object.add_vertex([2])

        self.assertEqual(10, result)
        self.assertListEqual([2], list(self._test_object.get_neighbours(result)))

    def test__add_vertex__when_no_neighbours(self):
        with self.assertRaises(NotConnectedError):
            self._test_object.add_vertex([])

    def test__add_vertex__when_many_neighbours(self):
        with self.assertRaises(CycleError):
            self._test_object.add_vertex([2, 9, 5])

    def test__add_edge(self):
        vertex1 = 1
        vertex2 = 5

        with self.assertRaises(CycleError):
            self._test_object.add_edge(vertex2, vertex1)
