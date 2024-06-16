# -*- coding: utf-8 -*-
"""Tests: Algorithms for graph cutting."""
import unittest

from assertpy import assert_that

from algolib.graphs import UndirectedSimpleGraph
from algolib.graphs.algorithms import find_edge_cut, find_vertex_cut


class CuttingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def test__find_edge_cut__when_present_bridges():
        # given
        graph = UndirectedSimpleGraph(range(12))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(7))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(6))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(8))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(9))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(11))
        graph.add_edge_between(graph.get_vertex(8), graph.get_vertex(9))
        graph.add_edge_between(graph.get_vertex(9), graph.get_vertex(10))
        graph.add_edge_between(graph.get_vertex(9), graph.get_vertex(11))
        graph.add_edge_between(graph.get_vertex(10), graph.get_vertex(11))

        # when
        result = find_edge_cut(graph)

        # then
        assert_that(sorted(result)).is_equal_to([graph.get_edge(0, 7), graph.get_edge(5, 6)])

    @staticmethod
    def test__find_edge_cut__when_no_bridges():
        # given
        graph = UndirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(5))

        # when
        result = find_edge_cut(graph)

        # then
        assert_that(list(result)).is_empty()

    @staticmethod
    def test__find_vertex_cut__when_present_separators():
        # given
        graph = UndirectedSimpleGraph(range(12))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(7))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(6))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(8))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(9))
        graph.add_edge_between(graph.get_vertex(7), graph.get_vertex(11))
        graph.add_edge_between(graph.get_vertex(8), graph.get_vertex(9))
        graph.add_edge_between(graph.get_vertex(9), graph.get_vertex(10))
        graph.add_edge_between(graph.get_vertex(9), graph.get_vertex(11))
        graph.add_edge_between(graph.get_vertex(10), graph.get_vertex(11))

        # when
        result = find_vertex_cut(graph)

        # then
        assert_that(sorted(result)).is_equal_to(
            [graph.get_vertex(0), graph.get_vertex(1), graph.get_vertex(5), graph.get_vertex(7)])

    @staticmethod
    def test__find_vertex_cut__when_no_separators():
        # given
        graph = UndirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(2), graph.get_vertex(3))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(5))
        graph.add_edge_between(graph.get_vertex(4), graph.get_vertex(5))

        # when
        result = find_vertex_cut(graph)

        # then
        assert_that(list(result)).is_empty()
