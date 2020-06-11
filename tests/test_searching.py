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
        self._directed_graph.add_edge(0, 1)
        self._directed_graph.add_edge(1, 3)
        self._directed_graph.add_edge(1, 7)
        self._directed_graph.add_edge(3, 4)
        self._directed_graph.add_edge(4, 0)
        self._directed_graph.add_edge(5, 4)
        self._directed_graph.add_edge(5, 8)
        self._directed_graph.add_edge(6, 2)
        self._directed_graph.add_edge(6, 9)
        self._directed_graph.add_edge(8, 5)

        self._undirected_graph = UndirectedSimpleGraph(range(10))
        self._undirected_graph.add_edge(0, 1)
        self._undirected_graph.add_edge(0, 4)
        self._undirected_graph.add_edge(1, 3)
        self._undirected_graph.add_edge(1, 7)
        self._undirected_graph.add_edge(2, 6)
        self._undirected_graph.add_edge(3, 4)
        self._undirected_graph.add_edge(4, 5)
        self._undirected_graph.add_edge(5, 8)
        self._undirected_graph.add_edge(6, 9)

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
        # when
        result = bfs(self._undirected_graph, EmptyStrategy(), [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))

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
        # when
        result = bfs(self._directed_graph, EmptyStrategy(), [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))

    # endregion
    # region dfs_iterative

    def test__dfs_iterative__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(), [0])
        # then
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], sorted(result))

    def test__dfs_iterative__when_undirected_graph_and_many_roots__then_all_visited(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(), [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))

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
        # when
        result = dfs_iterative(self._directed_graph, EmptyStrategy(), [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))

    # endregion
    # region dfs_recursive

    def test__dfs_recursive__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(), [0])
        # then
        self.assertListEqual([0, 1, 3, 4, 5, 7, 8], sorted(result))

    def test__dfs_recursive__when_undirected_graph_and_many_roots__then_all_visited(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(), [0, 6])
        # then
        self.assertListEqual(sorted(self._undirected_graph.vertices), sorted(result))

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
        # when
        result = dfs_recursive(self._directed_graph, EmptyStrategy(), [8, 6])
        # then
        self.assertListEqual(sorted(self._directed_graph.vertices), sorted(result))

    # endregion
