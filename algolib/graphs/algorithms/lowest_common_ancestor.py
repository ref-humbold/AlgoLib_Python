# -*- coding: utf-8 -*-
"""Lowest common ancestor algorithm"""
import math

from .searching import dfs_recursive
from .searching_strategy import DFSStrategy
from ..graph import Vertex
from ..tree_graph import TreeGraph


class LowestCommonAncestor:
    def __init__(self, graph: TreeGraph, root: Vertex):
        self.graph = graph
        self.root = root
        self._empty = True
        self._paths = {}
        self._strategy = self._LCAStrategy()

    def find(self, vertex1: Vertex, vertex2: Vertex) -> Vertex:
        """Finds a lowest common ancestor of two vertices in a rooted tree.

        :param vertex1: first vertex
        :param vertex2: second vertex
        :return: lowest common ancestor of given vertices"""
        if self._empty:
            self._initialize()

        return self._do_find(vertex1, vertex2)

    def _do_find(self, vertex1, vertex2):
        if self._is_offspring(vertex1, vertex2):
            return vertex2

        if self._is_offspring(vertex2, vertex1):
            return vertex1

        for candidate in reversed(self._paths[vertex1]):
            if not self._is_offspring(vertex2, candidate):
                return self._do_find(candidate, vertex2)

        return self._do_find(self._paths[vertex1][0], vertex2)

    def _initialize(self):
        dfs_recursive(self.graph, self._strategy, [self.root])

        for vertex in self.graph.vertices:
            self._paths[vertex] = [self._strategy.parents[vertex]]

        for i in range(int(math.log(self.graph.vertices_count, 2)) + 3):
            for vertex in self.graph.vertices:
                self._paths[vertex].append(self._paths[self._paths[vertex][i]][i])

        self._empty = False

    def _is_offspring(self, vertex1, vertex2):
        return self._strategy.pre_times[vertex1] >= self._strategy.pre_times[vertex2] \
               and self._strategy.post_times[vertex1] <= self._strategy.post_times[vertex2]

    class _LCAStrategy(DFSStrategy):
        def __init__(self):
            self.parents = {}
            self.pre_times = {}
            self.post_times = {}
            self._timer = 0

        def for_root(self, root):
            self.parents[root] = root

        def on_entry(self, vertex):
            self.pre_times[vertex] = self._timer
            self._timer += 1

        def on_next_vertex(self, vertex, neighbour):
            self.parents[neighbour] = vertex

        def on_exit(self, vertex):
            self.post_times[vertex] = self._timer
            self._timer += 1

        def on_edge_to_visited(self, vertex, neighbour):
            pass
