# -*- coding: utf-8 -*-
"""TEST : lowest common ancestor algorithm."""
import unittest

from algolib.graphs import ForestGraph, find_lca


class LCATest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__trees = None

    def setUp(self):
        self.__trees = ForestGraph(
            12, [(0, 1), (0, 2), (1, 3), (1, 4), (1, 5), (2, 6), (4, 7), (6, 8), (6, 9), (10, 11)])

    def tearDown(self):
        self.__trees = None

    def test_find_lca_when_vertices_not_in_same_tree(self):
        vertex1 = 1
        vertex2 = 11

        with self.assertRaises(ValueError):
            find_lca(self.__trees, vertex1, vertex2)

    def test_find_lca_when_root_not_in_same_tree(self):
        vertex1 = 1
        vertex2 = 9
        root = 10

        with self.assertRaises(ValueError):
            find_lca(self.__trees, vertex1, vertex2, root)

    def test_find_lca_when_same_vertex(self):
        vertex = 6

        result = find_lca(self.__trees, vertex, vertex)

        self.assertEqual(vertex, result)

    def test_find_lca_when_vertices_changed(self):
        vertex1 = 5
        vertex2 = 7

        result1 = find_lca(self.__trees, vertex1, vertex2)
        result2 = find_lca(self.__trees, vertex2, vertex1)

        self.assertEqual(1, result1)
        self.assertEqual(1, result2)

    def test_find_lca_when_vertices_in_different_subtrees(self):
        vertex1 = 5
        vertex2 = 7

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(1, result)

    def test_find_lca_when_root_is_lca(self):
        vertex1 = 3
        vertex2 = 9
        root = 0

        result = find_lca(self.__trees, vertex1, vertex2, root)

        self.assertEqual(root, result)

    def test_find_lca_when_vertices_are_offsprings(self):
        vertex1 = 8
        vertex2 = 2

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(vertex2, result)

    def test_find_lca_root_is_one_of_vertices_1(self):
        vertex1 = 11
        vertex2 = 10

        result = find_lca(self.__trees, vertex1, vertex2, vertex1)

        self.assertEqual(vertex1, result)

    def test_find_lca_when_root_is_one_of_vertices_2(self):
        vertex1 = 4
        vertex2 = 0

        result = find_lca(self.__trees, vertex1, vertex2, vertex2)

        self.assertEqual(vertex2, result)
