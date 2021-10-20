# -*- coding: utf-8 -*-
"""Tests: Algorithms for shortest paths"""
import unittest

from assertpy import assert_that

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph
from algolib.graphs.algorithms import Paths, bellman_ford, dijkstra, floyd_warshall


def _from_list(graph, distances):
    return {graph.get_vertex(i): d for i, d in enumerate(distances)}


def _from_matrix(graph, distances):
    return {(graph.get_vertex(i), graph.get_vertex(j)): d for i, ds in enumerate(distances)
            for j, d in enumerate(ds)}


class PathsTest(unittest.TestCase):
    INF = Paths.INFINITY

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._directed_graph = None
        self._undirected_graph = None

    def setUp(self):
        self._directed_graph = DirectedSimpleGraph(range(10))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(0),
                                              self._directed_graph.get_vertex(1), self._Weight(4))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(1),
                                              self._directed_graph.get_vertex(4), self._Weight(7))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(1),
                                              self._directed_graph.get_vertex(7), self._Weight(12))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(2),
                                              self._directed_graph.get_vertex(4), self._Weight(6))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(2),
                                              self._directed_graph.get_vertex(6), self._Weight(8))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(3),
                                              self._directed_graph.get_vertex(0), self._Weight(3))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(3),
                                              self._directed_graph.get_vertex(7), self._Weight(5))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(4),
                                              self._directed_graph.get_vertex(5), self._Weight(1))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(4),
                                              self._directed_graph.get_vertex(3), self._Weight(10))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(5),
                                              self._directed_graph.get_vertex(6), self._Weight(4))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(5),
                                              self._directed_graph.get_vertex(8), self._Weight(2))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(6),
                                              self._directed_graph.get_vertex(5), self._Weight(7))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(7),
                                              self._directed_graph.get_vertex(5), self._Weight(2))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(7),
                                              self._directed_graph.get_vertex(8), self._Weight(6))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(8),
                                              self._directed_graph.get_vertex(9), self._Weight(10))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(9),
                                              self._directed_graph.get_vertex(6), self._Weight(3))

        self._undirected_graph = UndirectedSimpleGraph(range(10))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(0),
                                                self._undirected_graph.get_vertex(1),
                                                self._Weight(4))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(1),
                                                self._undirected_graph.get_vertex(4),
                                                self._Weight(7))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(1),
                                                self._undirected_graph.get_vertex(7),
                                                self._Weight(12))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(2),
                                                self._undirected_graph.get_vertex(6),
                                                self._Weight(8))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(3),
                                                self._undirected_graph.get_vertex(0),
                                                self._Weight(3))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(3),
                                                self._undirected_graph.get_vertex(7),
                                                self._Weight(5))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(4),
                                                self._undirected_graph.get_vertex(5),
                                                self._Weight(1))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(4),
                                                self._undirected_graph.get_vertex(3),
                                                self._Weight(10))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(5),
                                                self._undirected_graph.get_vertex(8),
                                                self._Weight(2))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(7),
                                                self._undirected_graph.get_vertex(5),
                                                self._Weight(2))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(7),
                                                self._undirected_graph.get_vertex(8),
                                                self._Weight(6))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(9),
                                                self._undirected_graph.get_vertex(6),
                                                self._Weight(3))

    def test__bellman_ford__when_directed_graph(self):
        # given
        distances = [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20]
        expected = _from_list(self._directed_graph, distances)
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(2),
                                              self._directed_graph.get_vertex(1), self._Weight(-2))
        # when
        result = bellman_ford(self._directed_graph, self._directed_graph.get_vertex(1))
        # then
        assert_that(result).is_equal_to(expected)

    def test__bellman_ford__when_undirected_graph(self):
        # given
        distances = [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF]
        expected = _from_list(self._undirected_graph, distances)
        # when
        result = bellman_ford(self._undirected_graph.as_directed(),
                              self._undirected_graph.get_vertex(1))
        # then
        assert_that(result).is_equal_to(expected)

    def test__bellman_ford__when_negative_cycle__then_value_error(self):
        # given
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(8),
                                              self._directed_graph.get_vertex(3),
                                              self._Weight(-20.0))

        # when
        def function(graph):
            return bellman_ford(graph, graph.get_vertex(1))

        # then
        assert_that(function).raises(ValueError).when_called_with(self._directed_graph)

    def test__dijkstra__when_directed_graph(self):
        # given
        distances = [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20]
        expected = _from_list(self._directed_graph, distances)
        # when
        result = dijkstra(self._directed_graph, self._directed_graph.get_vertex(1))
        # then
        assert_that(result).is_equal_to(expected)

    def test__dijkstra__when_undirected_graph(self):
        # given
        distances = [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF]
        expected = _from_list(self._undirected_graph, distances)
        # when
        result = dijkstra(self._undirected_graph, self._undirected_graph.get_vertex(1))
        # then
        assert_that(result).is_equal_to(expected)

    def test__dijkstra__when_negative_edge__then_value_error(self):
        # given
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(2),
                                              self._directed_graph.get_vertex(1), self._Weight(-2))

        # when
        def function(graph):
            dijkstra(graph, graph.get_vertex(1))

        # then
        assert_that(function).raises(ValueError).when_called_with(self._directed_graph)

    def test__floyd_warshall__when_directed_graph(self):
        # given
        distances = [[0, 4, self.INF, 21, 11, 12, 16, 16, 14, 24],
                     [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20],
                     [18, -2, 0, 15, 5, 6, 8, 10, 8, 18],
                     [3, 7, self.INF, 0, 14, 7, 11, 5, 9, 19],
                     [13, 17, self.INF, 10, 0, 1, 5, 15, 3, 13],
                     [self.INF, self.INF, self.INF, self.INF, self.INF, 0, 4, self.INF, 2, 12],
                     [self.INF, self.INF, self.INF, self.INF, self.INF, 7, 0, self.INF, 9, 19],
                     [self.INF, self.INF, self.INF, self.INF, self.INF, 2, 6, 0, 4, 14],
                     [self.INF, self.INF, self.INF, self.INF, self.INF, 20, 13, self.INF, 0, 10],
                     [self.INF, self.INF, self.INF, self.INF, self.INF, 10, 3, self.INF, 12, 0]]
        expected = _from_matrix(self._directed_graph, distances)
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(2),
                                              self._directed_graph.get_vertex(1), self._Weight(-2))
        # when
        result = floyd_warshall(self._directed_graph)
        # then
        assert_that(result).is_equal_to(expected)

    def test__floyd_warshall__when_undirected_graph(self):
        # given
        distances = \
            [[0, 4, self.INF, 3, 11, 10, self.INF, 8, 12, self.INF],
             [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF],
             [self.INF, self.INF, 0, self.INF, self.INF, self.INF, 8, self.INF, self.INF, 11],
             [3, 7, self.INF, 0, 8, 7, self.INF, 5, 9, self.INF],
             [11, 7, self.INF, 8, 0, 1, self.INF, 3, 3, self.INF],
             [10, 8, self.INF, 7, 1, 0, self.INF, 2, 2, self.INF],
             [self.INF, self.INF, 8, self.INF, self.INF, self.INF, 0, self.INF, self.INF, 3],
             [8, 10, self.INF, 5, 3, 2, self.INF, 0, 4, self.INF],
             [12, 10, self.INF, 9, 3, 2, self.INF, 4, 0, self.INF],
             [self.INF, self.INF, 11, self.INF, self.INF, self.INF, 3, self.INF, self.INF, 0]]
        expected = _from_matrix(self._undirected_graph, distances)
        # when
        result = floyd_warshall(self._undirected_graph.as_directed())
        # then
        assert_that(result).is_equal_to(expected)

    class _Weight:
        def __init__(self, weight):
            self.weight = weight
