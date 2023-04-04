# -*- coding: utf-8 -*-
"""Algorithms for graph cutting (edge cut and vertex cut)"""
from typing import Iterable

from .searching import dfs_recursive
from .searching_strategy import DFSStrategy
from ..graph import Edge, Vertex
from ..undirected_graph import UndirectedGraph


def find_edge_cut(graph: UndirectedGraph) -> Iterable[Edge]:
    """Finds an edge cut of given graph.

    :param graph: an undirected graph
    :return: generator of edges in the edge cut"""
    strategy = _CuttingStrategy()
    dfs_recursive(graph, strategy, graph.vertices)

    return (graph.get_edge(vertex, strategy.dfs_parents[vertex]) for vertex in graph.vertices
            if strategy.has_bridge(vertex))


def find_vertex_cut(graph: UndirectedGraph) -> Iterable[Vertex]:
    """Finds a vertex cut of given graph.

    param graph: an undirected graph
    :return: generator of vertices in the vertex cut"""
    strategy = _CuttingStrategy()
    dfs_recursive(graph, strategy, graph.vertices)

    return (vertex for vertex in graph.vertices if strategy.is_separator(vertex))


class _CuttingStrategy(DFSStrategy):
    def __init__(self):
        self.depth = 0
        self.dfs_parents = {}
        self.dfs_children = {}
        self.dfs_depths = {}
        self.low_values = {}

    def for_root(self, root):
        pass

    def on_entry(self, vertex):
        self.dfs_depths[vertex] = self.depth
        self.low_values[vertex] = self.depth
        self.dfs_children[vertex] = []
        self.depth += 1

    def on_next_vertex(self, vertex, neighbour):
        self.dfs_parents[neighbour] = vertex
        self.dfs_children[vertex].append(neighbour)

    def on_exit(self, vertex):
        values = [self.low_values[child] for child in self.dfs_children[vertex]]
        values.append(self.low_values[vertex])
        self.low_values[vertex] = min(values)
        self.depth -= 1

    def on_edge_to_visited(self, vertex, neighbour):
        if neighbour != self.dfs_parents[vertex]:
            self.low_values[vertex] = min(self.low_values[vertex], self.dfs_depths[neighbour])

    def has_bridge(self, vertex):
        return not self.is_dfs_root(vertex) and self.low_values[vertex] == self.dfs_depths[vertex]

    def is_separator(self, vertex):
        return len(self.dfs_children[vertex]) > 1 if self.is_dfs_root(vertex) \
            else any(self.low_values[child] >= self.dfs_depths[vertex]
                     for child in self.dfs_children[vertex])

    def is_dfs_root(self, vertex):
        return self.dfs_depths[vertex] == 0
