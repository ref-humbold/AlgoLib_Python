# -*- coding: utf-8 -*-
"""Tests: Hopcroft-Karp algorithm for matching in bipartite graph"""
import unittest

from assertpy import assert_that

from algolib.graphs import MultipartiteGraph
from algolib.graphs.algorithms import match


class MatchingTest(unittest.TestCase):
    @staticmethod
    def test__match__when_matching_exists__then_maximal_matching():
        # given
        graph = MultipartiteGraph(2, [[0, 2, 4, 6], [1, 3, 5, 7]])
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(6))
        graph.add_edge_between(graph.get_vertex(6), graph.get_vertex(7))
        # when
        result = match(graph)
        # then
        assert_that(result).is_equal_to({graph.get_vertex(0): graph.get_vertex(5),
                                         graph.get_vertex(1): graph.get_vertex(2),
                                         graph.get_vertex(2): graph.get_vertex(1),
                                         graph.get_vertex(3): graph.get_vertex(4),
                                         graph.get_vertex(4): graph.get_vertex(3),
                                         graph.get_vertex(5): graph.get_vertex(0),
                                         graph.get_vertex(6): graph.get_vertex(7),
                                         graph.get_vertex(7): graph.get_vertex(6)})

    @staticmethod
    def test__match__when_vertices_only_in_group_0__then_empty():
        # given
        graph = MultipartiteGraph(2, [[0, 1, 2, 3, 4]])
        # when
        result = match(graph)
        # then
        assert_that(result).is_empty()

    @staticmethod
    def test__match__when_vertices_only_in_group_1__then_empty():
        # given
        graph = MultipartiteGraph(2, [[], [0, 1, 2, 3, 4]])
        # when
        result = match(graph)
        # then
        assert_that(result).is_empty()
