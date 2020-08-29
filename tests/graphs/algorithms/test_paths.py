# -*- coding: utf-8 -*-
"""Tests: Algorithms for shortest paths"""
import unittest

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph
from algolib.graphs.algorithms import Paths, bellman_ford, dijkstra, floyd_warshall


def _from_list(distances):
    return dict(enumerate(distances))


def _from_matrix(distances):
    return {(i, j): d for i, ds in enumerate(distances) for j, d in enumerate(ds)}


class PathsTest(unittest.TestCase):
    INF = Paths.INFINITY

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._directed_graph = None
        self._undirected_graph = None

    def setUp(self):
        self._directed_graph = DirectedSimpleGraph(range(10))
        self._directed_graph.add_edge_between(0, 1, self._Weight(4))
        self._directed_graph.add_edge_between(1, 4, self._Weight(7))
        self._directed_graph.add_edge_between(1, 7, self._Weight(12))
        self._directed_graph.add_edge_between(2, 4, self._Weight(6))
        self._directed_graph.add_edge_between(2, 6, self._Weight(8))
        self._directed_graph.add_edge_between(3, 0, self._Weight(3))
        self._directed_graph.add_edge_between(3, 7, self._Weight(5))
        self._directed_graph.add_edge_between(4, 5, self._Weight(1))
        self._directed_graph.add_edge_between(4, 3, self._Weight(10))
        self._directed_graph.add_edge_between(5, 6, self._Weight(4))
        self._directed_graph.add_edge_between(5, 8, self._Weight(2))
        self._directed_graph.add_edge_between(6, 5, self._Weight(7))
        self._directed_graph.add_edge_between(7, 5, self._Weight(2))
        self._directed_graph.add_edge_between(7, 8, self._Weight(6))
        self._directed_graph.add_edge_between(8, 9, self._Weight(10))
        self._directed_graph.add_edge_between(9, 6, self._Weight(3))

        self._undirected_graph = UndirectedSimpleGraph(range(10))
        self._undirected_graph.add_edge_between(0, 1, self._Weight(4))
        self._undirected_graph.add_edge_between(1, 4, self._Weight(7))
        self._undirected_graph.add_edge_between(1, 7, self._Weight(12))
        self._undirected_graph.add_edge_between(2, 6, self._Weight(8))
        self._undirected_graph.add_edge_between(3, 0, self._Weight(3))
        self._undirected_graph.add_edge_between(3, 7, self._Weight(5))
        self._undirected_graph.add_edge_between(4, 5, self._Weight(1))
        self._undirected_graph.add_edge_between(4, 3, self._Weight(10))
        self._undirected_graph.add_edge_between(5, 8, self._Weight(2))
        self._undirected_graph.add_edge_between(7, 5, self._Weight(2))
        self._undirected_graph.add_edge_between(7, 8, self._Weight(6))
        self._undirected_graph.add_edge_between(9, 6, self._Weight(3))

    def tearDown(self):
        del self._directed_graph
        del self._undirected_graph

    def test__bellman_ford__when_directed_graph(self):
        # given
        distances = [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20]
        expected = _from_list(distances)
        self._directed_graph.add_edge_between(2, 1, self._Weight(-2))
        # when
        result = bellman_ford(self._directed_graph, 1)
        # then
        self.assertDictEqual(expected, result)

    def test__bellman_ford__when_undirected_graph(self):
        # given
        distances = [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF]
        expected = _from_list(distances)
        # when
        result = bellman_ford(self._undirected_graph.as_directed(), 1)
        # then
        self.assertDictEqual(expected, result)

    def test__bellman_ford__when_negative_cycle__then_value_error(self):
        # given
        self._directed_graph.add_edge_between(8, 3, self._Weight(-20.0))
        # then
        with self.assertRaises(ValueError):
            # when
            bellman_ford(self._directed_graph, 1)

    def test__dijkstra__when_directed_graph(self):
        # given
        distances = [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20]
        expected = _from_list(distances)
        # when
        result = dijkstra(self._directed_graph, 1)
        # then
        self.assertDictEqual(expected, result)

    def test__dijkstra__when_undirected_graph(self):
        # given
        distances = [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF]
        expected = _from_list(distances)
        # when
        result = dijkstra(self._undirected_graph, 1)
        # then
        self.assertDictEqual(expected, result)

    def test__dijkstra__when_negative_edge__then_value_error(self):
        # given
        self._directed_graph.add_edge_between(2, 1, self._Weight(-2))
        # then
        with self.assertRaises(ValueError):
            # when
            dijkstra(self._directed_graph, 1)

    def test__floyd_warshall__when_directed_graph(self):
        # given
        distances = [
                [0, 4, self.INF, 21, 11, 12, 16, 16, 14, 24],
                [20, 0, self.INF, 17, 7, 8, 12, 12, 10, 20],
                [18, -2, 0, 15, 5, 6, 8, 10, 8, 18],
                [3, 7, self.INF, 0, 14, 7, 11, 5, 9, 19],
                [13, 17, self.INF, 10, 0, 1, 5, 15, 3, 13],
                [self.INF, self.INF, self.INF, self.INF, self.INF, 0, 4, self.INF, 2, 12],
                [self.INF, self.INF, self.INF, self.INF, self.INF, 7, 0, self.INF, 9, 19],
                [self.INF, self.INF, self.INF, self.INF, self.INF, 2, 6, 0, 4, 14],
                [self.INF, self.INF, self.INF, self.INF, self.INF, 20, 13, self.INF, 0, 10],
                [self.INF, self.INF, self.INF, self.INF, self.INF, 10, 3, self.INF, 12, 0], ]
        expected = _from_matrix(distances)
        self._directed_graph.add_edge_between(2, 1, self._Weight(-2))
        # when
        result = floyd_warshall(self._directed_graph)
        # then
        self.assertDictEqual(expected, result)

    def test__floyd_warshall__when_undirected_graph(self):
        # given
        distances = [
                [0, 4, self.INF, 3, 11, 10, self.INF, 8, 12, self.INF],
                [4, 0, self.INF, 7, 7, 8, self.INF, 10, 10, self.INF],
                [self.INF, self.INF, 0, self.INF, self.INF, self.INF, 8, self.INF, self.INF, 11],
                [3, 7, self.INF, 0, 8, 7, self.INF, 5, 9, self.INF],
                [11, 7, self.INF, 8, 0, 1, self.INF, 3, 3, self.INF],
                [10, 8, self.INF, 7, 1, 0, self.INF, 2, 2, self.INF],
                [self.INF, self.INF, 8, self.INF, self.INF, self.INF, 0, self.INF, self.INF, 3],
                [8, 10, self.INF, 5, 3, 2, self.INF, 0, 4, self.INF],
                [12, 10, self.INF, 9, 3, 2, self.INF, 4, 0, self.INF],
                [self.INF, self.INF, 11, self.INF, self.INF, self.INF, 3, self.INF, self.INF, 0], ]
        expected = _from_matrix(distances)
        # when
        result = floyd_warshall(self._undirected_graph.as_directed())
        # then
        self.assertDictEqual(expected, result)

    class _Weight:
        def __init__(self, weight):
            self.weight = weight
