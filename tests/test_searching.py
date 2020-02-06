# -*- coding: utf-8 -*-
"""Tests: Graph searching algorithms"""
import unittest

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph, bfs, iter_dfs, rec_dfs


class SearchingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._strategy = None
        self._digraph = None
        self._ugraph = None

    def setUp(self):
        self._strategy = _SearchingTestStrategy()
        self._digraph = DirectedSimpleGraph(10, [(0, 1), (1, 4), (1, 7), (2, 4), (2, 6), (3, 0),
                                                 (3, 7), (4, 5), (4, 3), (5, 6), (5, 8), (6, 5),
                                                 (7, 5), (7, 8), (8, 9), (9, 6)])
        self._ugraph = UndirectedSimpleGraph(10, [(0, 1), (1, 4), (1, 7), (2, 6), (3, 0), (3, 7),
                                                  (4, 5), (4, 3), (5, 8), (7, 5), (7, 8), (9, 6)])

    def tearDown(self):
        self._digraph = None
        self._ugraph = None

    def test__bfs__when_undirected_graph_and_single_root__then_not_all_visited(self):
        result = list(bfs(self._ugraph, self._strategy, 0))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, False, True, True, False],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], visited)

    def test__bfs__when_undirected_graph_and_many_roots__then_all_visited(self):
        result = list(bfs(self._ugraph, self._strategy, 0, 6))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__bfs__when_directed_graph_and_single_root__then_not_all_visited(self):
        result = list(bfs(self._digraph, self._strategy, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__bfs__when_directed_graph_and_many_roots__then_all_visited(self):
        result = list(bfs(self._digraph, self._strategy, 2, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__iter_dfs__when_undirected_graph_and_single_root__then_not_all_visited(self):
        result = list(iter_dfs(self._ugraph, self._strategy, 0))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, False, True, True, False],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], visited)

    def test__iter_dfs__when_undirected_graph_and_many_roots__then_all_visited(self):
        result = list(iter_dfs(self._ugraph, self._strategy, 0, 6))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__iter_dfs__when_directed_graph_and_single_root__then_not_all_visited(self):
        result = list(iter_dfs(self._digraph, self._strategy, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__iter_dfs__when_directed_graph_and_many_roots__then_all_visited(self):
        result = list(iter_dfs(self._digraph, self._strategy, 2, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__rec_dfs__when_undirected_graph_and_single_root__then_not_all_visited(self):
        result = list(rec_dfs(self._ugraph, self._strategy, 0))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, False, True, True, False],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], visited)

    def test__rec_dfs__when_undirected_graph_and_many_roots__then_all_visited(self):
        result = list(rec_dfs(self._ugraph, self._strategy, 0, 6))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__rec_dfs__when_directed_graph_and_single_root__then_not_all_visited(self):
        result = list(rec_dfs(self._digraph, self._strategy, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, False, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 3, 4, 5, 6, 7, 8, 9], visited)

    def test__rec_dfs__when_directed_graph_and_many_roots__then_all_visited(self):
        result = list(rec_dfs(self._digraph, self._strategy, 2, 1))
        visited = sorted(self._strategy.visited)

        self.assertListEqual([True, True, True, True, True, True, True, True, True, True],
                             result)
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], visited)


class _SearchingTestStrategy:
    def __init__(self):
        self.visited = []

    def preprocess(self, vertex):
        self.visited.append(vertex)

    def for_neighbour(self, vertex, neighbour):
        pass

    def postprocess(self, vertex):
        pass

    def on_cycle(self, vertex, neighbour):
        pass
