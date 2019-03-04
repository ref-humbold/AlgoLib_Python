# -*- coding: utf-8 -*-
"""Tests for minimal spanning tree algorithms"""
import unittest
from algolib.graphs import kruskal, prim, UndirectedWeightedSimpleGraph


class MSTTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__graph = None

    def setUp(self):
        self.__graph = UndirectedWeightedSimpleGraph(
            5, [(0, 1, -1), (0, 2, 4), (1, 2, 9), (1, 3, 7), (1, 4, 12), (2, 4, 6), (3, 4, 3)])

    def tearDown(self):
        self.__graph = None

    def test_kruskal(self):
        result = kruskal(self.__graph)

        self.assertEqual(12, result)

    def test_prim(self):
        result = prim(self.__graph, 0)

        self.assertEqual(12, result)

    def test_prim_when_diffrent_sources(self):
        result1 = prim(self.__graph, 1)
        result4 = prim(self.__graph, 4)

        self.assertEqual(12, result1)
        self.assertEqual(12, result4)
