# -*- coding: utf-8 -*-
"""Tests: Algorithms for graph searching"""
import unittest

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph
from algolib.graphs.algorithms import EmptyStrategy, bfs, dfs_iterative, dfs_recursive


class SearchingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._directed_graph = None
        self._undirected_graph = None

    def setUp(self):
        self._directed_graph = DirectedSimpleGraph(range(10))
        self._directed_graph.add_edge_between(0, 1)
        self._directed_graph.add_edge_between(1, 3)
        self._directed_graph.add_edge_between(1, 7)
        self._directed_graph.add_edge_between(3, 4)
        self._directed_graph.add_edge_between(4, 0)
        self._directed_graph.add_edge_between(5, 4)
        self._directed_graph.add_edge_between(5, 8)
        self._directed_graph.add_edge_between(6, 2)
        self._directed_graph.add_edge_between(6, 9)
        self._directed_graph.add_edge_between(8, 5)

        self._undirected_graph = UndirectedSimpleGraph(range(10))
        self._undirected_graph.add_edge_between(0, 1)
        self._undirected_graph.add_edge_between(0, 4)
        self._undirected_graph.add_edge_between(1, 3)
        self._undirected_graph.add_edge_between(1, 7)
        self._undirected_graph.add_edge_between(2, 6)
        self._undirected_graph.add_edge_between(3, 4)
        self._undirected_graph.add_edge_between(4, 5)
        self._undirected_graph.add_edge_between(5, 8)
        self._undirected_graph.add_edge_between(6, 9)

    def tearDown(self):
        del self._directed_graph
        del self._undirected_graph

    # region bfs

    def test__bfs__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = bfs(self._undirected_graph, EmptyStrategy(), [0])
        # then
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], sorted(result))

    def test__bfs__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = bfs(self._undirected_graph, strategy, [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    def test__bfs__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = bfs(self._undirected_graph, EmptyStrategy(), [])
        # then
        self.assertListEqual([], list(result))

    def test__bfs__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = bfs(self._directed_graph, EmptyStrategy(), [1])
        # then
        self.assertListEqual([0, 1, 3, 4, 7], sorted(result))

    def test__bfs__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = bfs(self._directed_graph, strategy, [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    # endregion
    # region dfs_iterative

    def test__dfs_iterative__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(), [0])
        # then
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], sorted(result))

    def test__dfs_iterative__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_iterative(self._undirected_graph, strategy, [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    def test__dfs_iterative__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(), [])
        # then
        self.assertListEqual([], list(result))

    def test__dfs_iterative__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_iterative(self._directed_graph, EmptyStrategy(), [1])
        # then
        self.assertListEqual([0, 1, 3, 4, 7], sorted(result))

    def test__dfs_iterative__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_iterative(self._directed_graph, strategy, [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    # endregion
    # region dfs_recursive

    def test__dfs_recursive__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(), [0])
        # then
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], sorted(result))

    def test__dfs_recursive__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_recursive(self._undirected_graph, strategy, [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    def test__dfs_recursive__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(), [])
        # then
        self.assertListEqual([], list(result))

    def test__dfs_recursive__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_recursive(self._directed_graph, EmptyStrategy(), [1])
        # then
        self.assertListEqual([0, 1, 3, 4, 7], sorted(result))

    def test__dfs_recursive__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_recursive(self._directed_graph, strategy, [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.entries))
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(strategy.exits))

    # endregion

    class _TestingStrategy:
        def __init__(self):
            self.entries = []
            self.exits = []

        def for_root(self, root):
            pass

        def on_entry(self, vertex):
            self.entries.append(vertex)

        def on_next_vertex(self, vertex, neighbour):
            pass

        def on_exit(self, vertex):
            self.exits.append(vertex)

        def on_edge_to_visited(self, vertex, neighbour):
            pass
