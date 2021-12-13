# -*- coding: utf-8 -*-
"""Tests: Strongly connected components algorithm"""
import unittest

from assertpy import assert_that

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.algorithms import find_scc


class StronglyConnectedComponentsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__find_scc__when_many_components_then_all_listed():
        # given
        graph = DirectedSimpleGraph(range(10))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(2), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(6), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(6), graph.get_vertex(9))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(6))
        graph.add_edge_between(graph.get_vertex(8), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(8), graph.get_vertex(7))
        graph.add_edge_between(graph.get_vertex(9), graph.get_vertex(8))
        # when
        result = list(find_scc(graph))
        # then
        assert_that(result).is_length(4)
        assert_that(result).contains_only(
            {graph.get_vertex(5)},
            {graph.get_vertex(2)},
            {graph.get_vertex(0), graph.get_vertex(1), graph.get_vertex(3), graph.get_vertex(4)},
            {graph.get_vertex(6), graph.get_vertex(7), graph.get_vertex(8), graph.get_vertex(9)})

    @staticmethod
    def test__find_scc__when_single_component__then_all_vertices():
        # given
        graph = DirectedSimpleGraph(range(7))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(2), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(6))
        graph.add_edge_between(graph.get_vertex(6), graph.get_vertex(0))
        # when
        result = find_scc(graph)
        # then
        assert_that(list(result)).is_equal_to([set(graph.vertices)])

    @staticmethod
    def test__find_scc__when_empty_graph__then_each_vertex_is_component():
        # given
        graph = DirectedSimpleGraph(range(4))
        # when
        result = list(find_scc(graph))
        # then
        assert_that(result).is_length(4)
        assert_that(result).contains_only({graph.get_vertex(0)}, {graph.get_vertex(1)},
                                          {graph.get_vertex(2)}, {graph.get_vertex(3)})
