# -*- coding: utf-8 -*-
"""Tests: Algorithms for minimal spanning tree."""
import unittest

from assertpy import assert_that

from algolib.graphs import UndirectedSimpleGraph
from algolib.graphs.algorithms import kruskal, prim


class MinimalSpanningTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph = None

    def setUp(self):
        self.graph = UndirectedSimpleGraph(range(5))
        self.graph.add_edge_between(self.graph.get_vertex(0), self.graph.get_vertex(1),
                                    self._Weight(-1))
        self.graph.add_edge_between(self.graph.get_vertex(0), self.graph.get_vertex(2),
                                    self._Weight(4))
        self.graph.add_edge_between(self.graph.get_vertex(1), self.graph.get_vertex(2),
                                    self._Weight(9))
        self.graph.add_edge_between(self.graph.get_vertex(1), self.graph.get_vertex(3),
                                    self._Weight(7))
        self.graph.add_edge_between(self.graph.get_vertex(1), self.graph.get_vertex(4),
                                    self._Weight(12))
        self.graph.add_edge_between(self.graph.get_vertex(2), self.graph.get_vertex(4),
                                    self._Weight(6))
        self.graph.add_edge_between(self.graph.get_vertex(3), self.graph.get_vertex(4),
                                    self._Weight(3))

    def test__kruskal__then_mst(self):
        # when
        result = kruskal(self.graph)
        # then
        assert_that(sorted(result.vertices)).is_equal_to(sorted(self.graph.vertices))
        assert_that(sorted(result.edges)).is_equal_to([self.graph.get_edge(0, 1),
                                                       self.graph.get_edge(0, 2),
                                                       self.graph.get_edge(2, 4),
                                                       self.graph.get_edge(3, 4)])
        assert_that(sum(result.properties[edge].weight for edge in result.edges)).is_equal_to(12)

    def test__prim__then_mst(self):
        # when
        result = prim(self.graph, self.graph.get_vertex(0))
        # then
        assert_that(sorted(result.vertices)).is_equal_to(sorted(self.graph.vertices))
        assert_that(sorted(result.edges)).is_equal_to([self.graph.get_edge(0, 1),
                                                       self.graph.get_edge(0, 2),
                                                       self.graph.get_edge(2, 4),
                                                       self.graph.get_edge(3, 4)])
        assert_that(sum(result.properties[edge].weight for edge in result.edges)).is_equal_to(12)

    def test__prim__when_different_sources__then_same_mst(self):
        # when
        result1 = prim(self.graph, self.graph.get_vertex(1))
        result4 = prim(self.graph, self.graph.get_vertex(4))
        # then
        assert_that(result1.edges_count).is_equal_to(result4.edges_count)
        assert_that(sorted(result1.edges)).is_equal_to(sorted(result4.edges))

    class _Weight:
        def __init__(self, weight):
            self.weight = weight
