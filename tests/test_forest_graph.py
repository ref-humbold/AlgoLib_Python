# -*- coding: utf-8 -*-
"""TEST : Tree graphs structure."""
import unittest

from algolib.graphs import CycleException, ForestGraph


class ForestGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = ForestGraph(10)

    def tearDown(self):
        self._test_object = None

    def test_trees_number(self):
        result = self._test_object.trees_number

        self.assertEqual(10, result)

    def test_add_vertex(self):
        result = self._test_object.add_vertex()

        self.assertEqual(10, result)
        self.assertListEqual([], list(self._test_object.get_neighbours(result)))

    def test_add_edge_when_no_cycle(self):
        vertex1 = 1
        vertex2 = 2

        self._test_object.add_edge(vertex1, vertex2)

        self.assertIn(vertex2, self._test_object.get_neighbours(vertex1))
        self.assertIn(vertex1, self._test_object.get_neighbours(vertex2))

    def test_add_edge_when_cycle(self):
        vertex1 = 1
        vertex2 = 2
        vertex3 = 3

        self._test_object.add_edge(vertex1, vertex2)
        self._test_object.add_edge(vertex2, vertex3)

        with self.assertRaises(CycleException):
            self._test_object.add_edge(vertex3, vertex1)

    def test_is_same_tree_when_connected(self):
        vertex1 = 1
        vertex2 = 2

        self._test_object.add_edge(vertex1, vertex2)
        result = self._test_object.is_same_tree(vertex1, vertex2)

        self.assertTrue(result)

    def test_is_same_tree_when_not_connected(self):
        vertex1 = 1
        vertex2 = 2

        result = self._test_object.is_same_tree(vertex1, vertex2)

        self.assertFalse(result)
