# -*- coding: utf-8 -*-
"""TESTY DLA ALGORYTMU NAJNIŻSZEGO WSPÓLNEGO PRZODKA"""
import unittest
from algolib.graphs import find_lca, ForestGraph, UndirectedGraph


class LCATest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__trees = None

    def setUp(self):
        self.__trees = ForestGraph(UndirectedGraph(
            12), [(0, 1), (0, 2), (1, 3), (1, 4), (1, 5), (2, 6), (4, 7), (6, 8), (6, 9), (10, 11)])

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

    def test_find_lca_1(self):
        vertex1 = 5
        vertex2 = 7

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(1, result)

    def test_find_lca_2(self):
        vertex1 = 3
        vertex2 = 9

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(0, result)

    def test_find_lca_3(self):
        vertex1 = 8
        vertex2 = 2

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(2, result)

    def test_find_lca_4(self):
        vertex1 = 4
        vertex2 = 0

        result = find_lca(self.__trees, vertex1, vertex2)

        self.assertEqual(0, result)

    def test_find_lca_5(self):
        vertex1 = 11
        vertex2 = 10

        result = find_lca(self.__trees, vertex1, vertex2, 11)

        self.assertEqual(11, result)
