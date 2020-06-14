# -*- coding: utf-8 -*-
"""Tests: Algorithms for minimal spanning tree"""
import unittest

from algolib.graphs import UndirectedSimpleGraph
from algolib.graphs.algorithms import kruskal, prim


class MinimalSpanningTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graph = None

    def setUp(self):
        self._graph = UndirectedSimpleGraph(range(5))
        self._graph.add_edge_between(0, 1, self._Weight(-1))
        self._graph.add_edge_between(0, 2, self._Weight(4))
        self._graph.add_edge_between(1, 2, self._Weight(9))
        self._graph.add_edge_between(1, 3, self._Weight(7))
        self._graph.add_edge_between(1, 4, self._Weight(12))
        self._graph.add_edge_between(2, 4, self._Weight(6))
        self._graph.add_edge_between(3, 4, self._Weight(3))

    def tearDown(self):
        del self._graph

    def test__kruskal__then_MST(self):
        # when
        result = kruskal(self._graph)
        # then
        mst_size = sum(result[edge].weight for edge in result.edges)

        self.assertListEqual(sorted(self._graph.vertices), sorted(result.vertices))
        self.assertListEqual(sorted([self._graph.get_edge(0, 1),
                                     self._graph.get_edge(0, 2),
                                     self._graph.get_edge(2, 4),
                                     self._graph.get_edge(3, 4)]), sorted(result.edges))
        self.assertAlmostEqual(12, mst_size, 6)

    def test__prim__then_MST(self):
        # when
        result = prim(self._graph, 0)
        # then
        mst_size = sum(result[edge].weight for edge in result.edges)

        self.assertListEqual(sorted(self._graph.vertices), sorted(result.vertices))
        self.assertListEqual(sorted([self._graph.get_edge(0, 1),
                                     self._graph.get_edge(0, 2),
                                     self._graph.get_edge(2, 4),
                                     self._graph.get_edge(3, 4)]),
                             sorted(result.edges))
        self.assertEqual(12, mst_size)

    def test__prim__when_different_sources__then_same_MST(self):
        # when
        result1 = prim(self._graph, 1)
        result4 = prim(self._graph, 4)
        # then
        self.assertEqual(result1.edges_count, result4.edges_count)
        self.assertListEqual(sorted(result1.edges), sorted(result4.edges))

    class _Weight:
        def __init__(self, weight):
            self.weight = weight
