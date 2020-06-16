# -*- coding: utf-8 -*-
"""Tests: Algorithms for topological sorting"""
import unittest

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.algorithms import sort_topological1, sort_topological2


class TopologicalSortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__sort_topological1__when_acyclic_graph__then_topological_order(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 4)
        graph.add_edge_between(1, 0)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(3, 1)
        graph.add_edge_between(3, 0)
        graph.add_edge_between(3, 2)
        graph.add_edge_between(5, 1)
        graph.add_edge_between(5, 2)
        graph.add_edge_between(5, 4)
        # when
        result = sort_topological1(graph)
        # then
        self.assertListEqual([3, 5, 1, 0, 2, 4], list(result))

    def test__sort_topological1__when_cyclic_graph__then_ValueError(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 4)
        graph.add_edge_between(1, 0)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(2, 1)
        graph.add_edge_between(3, 1)
        graph.add_edge_between(3, 0)
        graph.add_edge_between(3, 2)
        graph.add_edge_between(5, 1)
        graph.add_edge_between(5, 2)
        graph.add_edge_between(5, 4)
        # then
        with self.assertRaises(ValueError):
            sort_topological1(graph)

    def test__sort_topological1__when_empty_graph__then_natural_order(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        # when
        result = sort_topological1(graph)
        # then
        self.assertListEqual([0, 1, 2, 3, 4, 5], list(result))

    def test__sort_topological2__when_acyclic_graph__then_topological_order(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 4)
        graph.add_edge_between(1, 0)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(3, 1)
        graph.add_edge_between(3, 0)
        graph.add_edge_between(3, 2)
        graph.add_edge_between(5, 1)
        graph.add_edge_between(5, 2)
        graph.add_edge_between(5, 4)
        # when
        result = sort_topological2(graph)
        # then
        self.assertIn(list(result), [[3, 5, 1, 0, 2, 4], [5, 3, 1, 0, 2, 4], [3, 5, 1, 0, 4, 2],
                                     [5, 3, 1, 0, 4, 2]])

    def test__sort_topological2__when_cyclic_graph__then_ValueError(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 4)
        graph.add_edge_between(1, 0)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(2, 1)
        graph.add_edge_between(3, 1)
        graph.add_edge_between(3, 0)
        graph.add_edge_between(3, 2)
        graph.add_edge_between(5, 1)
        graph.add_edge_between(5, 2)
        graph.add_edge_between(5, 4)
        # then
        with self.assertRaises(ValueError):
            # when
            sort_topological2(graph)

    def test__sort_topological2__when_empty_graph__then_natural_order(self):
        # given
        graph = DirectedSimpleGraph(range(6))
        # when
        result = sort_topological2(graph)
        # then
        self.assertListEqual([0, 1, 2, 3, 4, 5], list(result))
