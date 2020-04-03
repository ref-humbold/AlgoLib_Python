# -*- coding: utf-8 -*-
"""Tests: Minimal spanning tree algorithms"""
import unittest

from algolib.graphs import UndirectedWeightedSimpleGraph
from algolib.graphs.algorithms import kruskal, prim


class MSTTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graph = None

    def setUp(self):
        self._graph = UndirectedWeightedSimpleGraph(5, [(0, 1, -1), (0, 2, 4), (1, 2, 9), (1, 3, 7),
                                                        (1, 4, 12), (2, 4, 6), (3, 4, 3)])

    def tearDown(self):
        self._graph = None

    def test__kruskal(self):
        result = kruskal(self._graph)

        self.assertEqual(12, result)

    def test__prim(self):
        result = prim(self._graph, 0)

        self.assertEqual(12, result)

    def test__prim__when_diffrent_sources(self):
        result1 = prim(self._graph, 1)
        result4 = prim(self._graph, 4)

        self.assertEqual(12, result1)
        self.assertEqual(12, result4)
