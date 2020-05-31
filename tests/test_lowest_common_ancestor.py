# -*- coding: utf-8 -*-
"""Tests: lowest common ancestor algorithm"""
import unittest

from algolib.old_graphs import TreeGraph
from algolib.old_graphs.algorithms import find_lca


class LCATest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._trees = None

    def setUp(self):
        self._trees = TreeGraph(10, [(0, 1), (0, 2), (1, 3), (1, 4), (1, 5), (2, 6), (4, 7), (6, 8),
                                     (6, 9)])

    def tearDown(self):
        self._trees = None

    def test__find_lca__when_same_vertex(self):
        vertex = 6

        result = find_lca(self._trees, vertex, vertex)

        self.assertEqual(vertex, result)

    def test__find_lca__when_vertices_changed(self):
        vertex1 = 5
        vertex2 = 7

        result1 = find_lca(self._trees, vertex1, vertex2)
        result2 = find_lca(self._trees, vertex2, vertex1)

        self.assertEqual(1, result1)
        self.assertEqual(1, result2)

    def test__find_lca__when_vertices_in_different_subtrees(self):
        vertex1 = 5
        vertex2 = 7

        result = find_lca(self._trees, vertex1, vertex2)

        self.assertEqual(1, result)

    def test__find_lca__when_root_is_lca(self):
        vertex1 = 3
        vertex2 = 9
        root = 0

        result = find_lca(self._trees, vertex1, vertex2, root)

        self.assertEqual(root, result)

    def test__find_lca__when_vertices_are_offsprings(self):
        vertex1 = 8
        vertex2 = 2

        result = find_lca(self._trees, vertex1, vertex2)

        self.assertEqual(vertex2, result)

    def test__find_lca__when_root_is_one_of_vertices(self):
        vertex1 = 4
        vertex2 = 0

        result = find_lca(self._trees, vertex1, vertex2, vertex2)

        self.assertEqual(vertex2, result)
