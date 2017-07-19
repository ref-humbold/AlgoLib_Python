# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW SKIEROWANYCH"""
from abc import ABCMeta, abstractmethod
from .graph import Graph, SimpleGraph, WeightedGraph, NoSuchVertexException


class DirectedGraph(Graph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def reverse(self):
        """Odwracanie skierowania grafu."""
        pass


class DirectedWeightedGraph(DirectedGraph, WeightedGraph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()


class DirectedSimpleGraph(SimpleGraph, DirectedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    @property
    def edges_number(self):
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_edges(self):
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v))

    def add_edge(self, vertex1, vertex2):
        if not 0 <= vertex1 < self.vertices_number:
            raise NoSuchVertexException(str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise NoSuchVertexException(str(vertex2))

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        if not 0 <= vertex < self.vertices_number:
            raise NoSuchVertexException(str(vertex))

        return sum(1 for _, v in self.get_edges() if v == vertex)

    def reverse(self):
        revgraphrepr = [set() for _ in self.get_vertices()]

        for v, u in self.get_edges():
            revgraphrepr[u].add((v, self._DEFAULT_WEIGHT))

        self._graphrepr = revgraphrepr


class DirectedWeightedSimpleGraph(DirectedSimpleGraph, DirectedWeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in map(lambda e: e if len(e) > 2 else (e[0], e[1], self._DEFAULT_WEIGHT), edges):
                self.add_weighted_edge(e[0], e[1], e[2])

    def get_weighted_edges(self):
        return ((v, u, wg) for v in self.get_vertices()
                for u, wg in self.get_weighted_neighbours(v))

    def add_weighted_edge(self, vertex1, vertex2, weight):
        if not 0 <= vertex1 < self.vertices_number:
            raise NoSuchVertexException(str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise NoSuchVertexException(str(vertex2))

        self._graphrepr[vertex1].add((vertex2, weight))

    def get_weighted_neighbours(self, vertex):
        if not 0 <= vertex < self.vertices_number:
            raise NoSuchVertexException(str(vertex))

        return iter(self._graphrepr[vertex])

    def reverse(self):
        revgraphrepr = [set() for _ in self.get_vertices()]

        for v, u, wg in self.get_weighted_edges():
            revgraphrepr[u].add((v, wg))

        self._graphrepr = revgraphrepr
