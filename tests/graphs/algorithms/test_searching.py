# -*- coding: utf-8 -*-
"""Tests: Algorithms for graph searching"""
import unittest

from assertpy import assert_that

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph
from algolib.graphs.algorithms import DFSStrategy, EmptyStrategy, bfs, dfs_iterative, dfs_recursive


class SearchingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._directed_graph = None
        self._undirected_graph = None

    def setUp(self):
        self._directed_graph = DirectedSimpleGraph(range(10))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(0),
                                              self._directed_graph.get_vertex(1))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(1),
                                              self._directed_graph.get_vertex(3))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(1),
                                              self._directed_graph.get_vertex(7))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(3),
                                              self._directed_graph.get_vertex(4))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(4),
                                              self._directed_graph.get_vertex(0))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(5),
                                              self._directed_graph.get_vertex(4))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(5),
                                              self._directed_graph.get_vertex(8))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(6),
                                              self._directed_graph.get_vertex(2))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(6),
                                              self._directed_graph.get_vertex(9))
        self._directed_graph.add_edge_between(self._directed_graph.get_vertex(8),
                                              self._directed_graph.get_vertex(5))

        self._undirected_graph = UndirectedSimpleGraph(range(10))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(0),
                                                self._undirected_graph.get_vertex(1))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(0),
                                                self._undirected_graph.get_vertex(4))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(1),
                                                self._undirected_graph.get_vertex(3))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(1),
                                                self._undirected_graph.get_vertex(7))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(2),
                                                self._undirected_graph.get_vertex(6))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(3),
                                                self._undirected_graph.get_vertex(4))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(4),
                                                self._undirected_graph.get_vertex(5))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(5),
                                                self._undirected_graph.get_vertex(8))
        self._undirected_graph.add_edge_between(self._undirected_graph.get_vertex(6),
                                                self._undirected_graph.get_vertex(9))

    # region bfs

    def test__bfs__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = bfs(self._undirected_graph, EmptyStrategy(),
                     [self._undirected_graph.get_vertex(0)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._undirected_graph.get_vertex(0), self._undirected_graph.get_vertex(1),
             self._undirected_graph.get_vertex(3), self._undirected_graph.get_vertex(4),
             self._undirected_graph.get_vertex(5), self._undirected_graph.get_vertex(7),
             self._undirected_graph.get_vertex(8)])

    def test__bfs__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = bfs(self._undirected_graph, strategy,
                     [self._undirected_graph.get_vertex(0),
                      self._undirected_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    def test__bfs__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = bfs(self._undirected_graph, EmptyStrategy(), [])
        # then
        assert_that(list(result)).is_empty()

    def test__bfs__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = bfs(self._directed_graph, EmptyStrategy(), [self._directed_graph.get_vertex(1)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._directed_graph.get_vertex(0), self._directed_graph.get_vertex(1),
             self._directed_graph.get_vertex(3), self._directed_graph.get_vertex(4),
             self._directed_graph.get_vertex(7)])

    def test__bfs__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = bfs(self._directed_graph, strategy,
                     [self._directed_graph.get_vertex(8),
                      self._directed_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._directed_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    # endregion
    # region dfs_iterative

    def test__dfs_iterative__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(),
                               [self._undirected_graph.get_vertex(0)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._undirected_graph.get_vertex(0), self._undirected_graph.get_vertex(1),
             self._undirected_graph.get_vertex(3), self._undirected_graph.get_vertex(4),
             self._undirected_graph.get_vertex(5), self._undirected_graph.get_vertex(7),
             self._undirected_graph.get_vertex(8)])

    def test__dfs_iterative__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_iterative(self._undirected_graph, strategy, [
                self._undirected_graph.get_vertex(0),
                self._undirected_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    def test__dfs_iterative__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = dfs_iterative(self._undirected_graph, EmptyStrategy(), [])
        # then
        assert_that(list(result)).is_empty()

    def test__dfs_iterative__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_iterative(self._directed_graph, EmptyStrategy(),
                               [self._directed_graph.get_vertex(1)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._directed_graph.get_vertex(0), self._directed_graph.get_vertex(1),
             self._directed_graph.get_vertex(3), self._directed_graph.get_vertex(4),
             self._directed_graph.get_vertex(7)])

    def test__dfs_iterative__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_iterative(self._directed_graph, strategy, [
                self._directed_graph.get_vertex(8),
                self._directed_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._directed_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    # endregion
    # region dfs_recursive

    def test__dfs_recursive__when_undirected_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(),
                               [self._undirected_graph.get_vertex(0)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._undirected_graph.get_vertex(0), self._undirected_graph.get_vertex(1),
             self._undirected_graph.get_vertex(3), self._undirected_graph.get_vertex(4),
             self._undirected_graph.get_vertex(5), self._undirected_graph.get_vertex(7),
             self._undirected_graph.get_vertex(8)])

    def test__dfs_recursive__when_undirected_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_recursive(self._undirected_graph, strategy, [
                self._undirected_graph.get_vertex(0),
                self._undirected_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    def test__dfs_recursive__when_undirected_graph_and_no_roots__then_empty(self):
        # when
        result = dfs_recursive(self._undirected_graph, EmptyStrategy(), [])
        # then
        assert_that(list(result)).is_empty()

    def test__dfs_recursive__when_directed_graph_and_single_root__then_visited_visited(self):
        # when
        result = dfs_recursive(self._directed_graph, EmptyStrategy(),
                               [self._directed_graph.get_vertex(1)])
        # then
        assert_that(sorted(result)).is_equal_to(
            [self._directed_graph.get_vertex(0), self._directed_graph.get_vertex(1),
             self._directed_graph.get_vertex(3), self._directed_graph.get_vertex(4),
             self._directed_graph.get_vertex(7)])

    def test__dfs_recursive__when_directed_graph_and_many_roots__then_all_visited(self):
        # given
        strategy = self._TestingStrategy()
        # when
        result = dfs_recursive(self._directed_graph, strategy, [
                self._directed_graph.get_vertex(8),
                self._directed_graph.get_vertex(6)])
        # then
        assert_that(sorted(result)).is_equal_to(sorted(self._directed_graph.vertices))
        assert_that(sorted(strategy.entries)).is_equal_to(sorted(self._undirected_graph.vertices))
        assert_that(sorted(strategy.exits)).is_equal_to(sorted(self._undirected_graph.vertices))

    # endregion

    class _TestingStrategy(DFSStrategy):
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
