# -*- coding: utf-8 -*-
"""Tests: Hopcroft-Karp algorithm for matching in bipartite graph"""
import unittest

from algolib.graphs import MultipartiteGraph
from algolib.graphs.algorithms import match


class MatchingTest(unittest.TestCase):
    def test__match__when_matching_exists__then_maximal_matching(self):
        # given
        graph = MultipartiteGraph(2, [[0, 2, 4, 6], [1, 3, 5, 7]])
        graph.add_edge_between(0, 3)
        graph.add_edge_between(0, 5)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(3, 4)
        graph.add_edge_between(3, 6)
        graph.add_edge_between(6, 7)
        # when
        result = match(graph)
        # then
        self.assertDictEqual({0: 5, 1: 2, 2: 1, 3: 4, 4: 3, 5: 0, 6: 7, 7: 6}, result)

    def test__match__when_vertices_only_in_group_0__then_empty(self):
        # given
        graph = MultipartiteGraph(2, [[0, 1, 2, 3, 4]])
        # when
        result = match(graph)
        # then
        self.assertDictEqual({}, result)

    def test__match__when_vertices_only_in_group_1__then_empty(self):
        # given
        graph = MultipartiteGraph(2, [[], [0, 1, 2, 3, 4]])
        # when
        result = match(graph)
        # then
        self.assertDictEqual({}, result)
