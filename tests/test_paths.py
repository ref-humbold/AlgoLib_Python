# -*- coding: utf-8 -*-
"""TEST : Shortest paths algorithms."""
import unittest

from refhumbold.algolib.graphs import DirectedWeightedSimpleGraph, UndirectedWeightedSimpleGraph, \
    bellman_ford, dijkstra, floyd_warshall


class PathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__diwgraph = None
        self.__uwgraph = None

    def setUp(self):
        self.__diwgraph = DirectedWeightedSimpleGraph(
            10, [(0, 1, 4), (1, 4, 7), (1, 7, 12), (2, 4, 6), (2, 6, 8), (3, 0, 3), (3, 7, 5),
                 (4, 5, 1), (4, 3, 10), (5, 6, 4), (5, 8, 2), (6, 5, 7), (7, 5, 2), (7, 8, 6),
                 (8, 9, 10), (9, 6, 3)])
        self.__uwgraph = UndirectedWeightedSimpleGraph(
            10, [(0, 1, 4), (1, 4, 7), (1, 7, 12), (2, 6, 8), (3, 0, 3), (3, 7, 5), (4, 5, 1),
                 (4, 3, 10), (5, 8, 2), (7, 5, 2), (7, 8, 6), (9, 6, 3)])

    def tearDown(self):
        self.__diwgraph = None
        self.__uwgraph = None

    def test_bellman_ford_when_directed_graph(self):
        source = 1
        self.__diwgraph.add_weighted_edge(2, 1, -2)

        result = bellman_ford(self.__diwgraph, source)

        self.assertListEqual([20, 0, self.__diwgraph.inf, 17, 7, 8, 12, 12, 10, 20], result)

    def test_bellman_ford_when_undirected_graph(self):
        source = 1

        result = bellman_ford(self.__uwgraph.as_directed(), source)
        i = self.__diwgraph.inf

        self.assertListEqual([4, 0, i, 7, 7, 8, i, 10, 10, i], result)

    def test_bellman_ford_when_negative_cycle(self):
        source = 1
        self.__diwgraph.add_weighted_edge(8, 3, -20.0)

        with self.assertRaises(ValueError):
            bellman_ford(self.__diwgraph, source)

    def test_dijkstra_when_directed_graph(self):
        source = 1

        result = dijkstra(self.__diwgraph, source)

        self.assertListEqual([20, 0, self.__diwgraph.inf, 17, 7, 8, 12, 12, 10, 20], result)

    def test_dijkstra_when_undirected_graph(self):
        source = 1

        result = dijkstra(self.__uwgraph, source)
        i = self.__diwgraph.inf

        self.assertListEqual([4, 0, i, 7, 7, 8, i, 10, 10, i], result)

    def test_dijkstra_when_negative_edge(self):
        source = 1
        self.__diwgraph.add_weighted_edge(2, 1, -2)

        with self.assertRaises(ValueError):
            dijkstra(self.__diwgraph, source)

    def test_floyd_warshall_when_directed_graph(self):
        self.__diwgraph.add_weighted_edge(2, 1, -2)

        result = floyd_warshall(self.__diwgraph)
        i = self.__diwgraph.inf

        self.assertListEqual([[0, 4, i, 21, 11, 12, 16, 16, 14, 24],
                              [20, 0, i, 17, 7, 8, 12, 12, 10, 20],
                              [18, -2, 0, 15, 5, 6, 8, 10, 8, 18],
                              [3, 7, i, 0, 14, 7, 11, 5, 9, 19],
                              [13, 17, i, 10, 0, 1, 5, 15, 3, 13],
                              [i, i, i, i, i, 0, 4, i, 2, 12],
                              [i, i, i, i, i, 7, 0, i, 9, 19],
                              [i, i, i, i, i, 2, 6, 0, 4, 14],
                              [i, i, i, i, i, 20, 13, i, 0, 10],
                              [i, i, i, i, i, 10, 3, i, 12, 0]], result)

    def test_floyd_warshall_when_undirected_graph(self):
        result = floyd_warshall(self.__uwgraph.as_directed())
        i = self.__diwgraph.inf

        self.assertListEqual([[0, 4, i, 3, 11, 10, i, 8, 12, i],
                              [4, 0, i, 7, 7, 8, i, 10, 10, i],
                              [i, i, 0, i, i, i, 8, i, i, 11],
                              [3, 7, i, 0, 8, 7, i, 5, 9, i],
                              [11, 7, i, 8, 0, 1, i, 3, 3, i],
                              [10, 8, i, 7, 1, 0, i, 2, 2, i],
                              [i, i, 8, i, i, i, 0, i, i, 3],
                              [8, 10, i, 5, 3, 2, i, 0, 4, i],
                              [12, 10, i, 9, 3, 2, i, 4, 0, i],
                              [i, i, 11, i, i, i, 3, i, i, 0]], result)
