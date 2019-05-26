# -*- coding: utf-8 -*-
"""TEST : Tree graphs structure."""
import unittest

from algolib.graphs import CycleException, TreeGraph


class TreeGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = TreeGraph(10, [(0, 6), (1, 2), (2, 3), (3, 4), (4, 5), (6, 4), (7, 3),
                                           (8, 3), (9, 7)])

    def tearDown(self):
        self._test_object = None

    def test_add_vertex_when_one_neighbour(self):
        result = self._test_object.add_vertex([2])

        self.assertEqual(10, result)
        self.assertListEqual([2], list(self._test_object.get_neighbours(result)))

    def test_add_vertex_when_no_neighbours(self):
        with self.assertRaises(ValueError):
            self._test_object.add_vertex([])

    def test_add_vertex_when_many_neighbours(self):
        with self.assertRaises(ValueError):
            self._test_object.add_vertex([2, 9, 5])

    def test_add_edge(self):
        vertex1 = 1
        vertex2 = 9

        with self.assertRaises(CycleException):
            self._test_object.add_edge(vertex2, vertex1)
