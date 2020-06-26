# -*- coding: utf-8 -*-
"""Tests: Strongly connected components algorithm"""
import unittest

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.algorithms import find_scc


class SCCTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__find_scc__when_many_components_then_all_listed(self):
        # given
        graph = DirectedSimpleGraph(range(10))
        graph.add_edge_between(0, 4)
        graph.add_edge_between(0, 5)
        graph.add_edge_between(1, 0)
        graph.add_edge_between(2, 3)
        graph.add_edge_between(3, 1)
        graph.add_edge_between(4, 1)
        graph.add_edge_between(4, 3)
        graph.add_edge_between(6, 5)
        graph.add_edge_between(6, 9)
        graph.add_edge_between(7, 4)
        graph.add_edge_between(7, 6)
        graph.add_edge_between(8, 3)
        graph.add_edge_between(8, 7)
        graph.add_edge_between(9, 8)
        # when
        result = find_scc(graph)
        # then
        self.assertEqual(4, len(result))
        self.assertIn({5}, result)
        self.assertIn({2}, result)
        self.assertIn({0, 1, 3, 4}, result)
        self.assertIn({6, 7, 8, 9}, result)

    def test__find_scc__when_single_component__then_all_vertices(self):
        # given
        graph = DirectedSimpleGraph(range(7))
        graph.add_edge_between(0, 1)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(2, 3)
        graph.add_edge_between(3, 4)
        graph.add_edge_between(4, 5)
        graph.add_edge_between(5, 6)
        graph.add_edge_between(6, 0)
        # when
        result = find_scc(graph)
        # then
        self.assertListEqual([set(graph.vertices)], result)

    def test__find_scc__when_empty_graph__then_each_vertex_is_component(self):
        # given
        graph = DirectedSimpleGraph(range(4))
        # when
        result = find_scc(graph)
        # then
        self.assertEqual(4, len(result))
        self.assertIn({0}, result)
        self.assertIn({1}, result)
        self.assertIn({2}, result)
        self.assertIn({3}, result)
