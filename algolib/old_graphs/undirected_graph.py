# -*- coding: utf-8 -*-
"""Structure of undirected graphs"""
from abc import ABCMeta, abstractmethod

from algolib.old_graphs.directed_graph import DirectedSimpleGraph, DirectedWeightedSimpleGraph
from algolib.old_graphs.graph import Graph, NoSuchVertexError, SimpleGraph, WeightedGraph


class UndirectedGraph(Graph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def to_directed(self):
        """Zamiana krawędzi nieskierowanych na skierowane.

        :return: graf ze skierowanymi krawędziami"""
        pass


class UndirectedWeightedGraph(UndirectedGraph, WeightedGraph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    @property
    def edges_number(self):
        return sum(
                self.get_outdegree(v) + 1 if v in self.get_neighbours(v) else self.get_outdegree(v)
                for v in self.get_vertices()) / 2

    def get_edges(self):
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v) if u >= v)

    def add_edge(self, vertex1, vertex2):
        if not 0 <= vertex1 < self.vertices_number:
            raise NoSuchVertexError(f"No vertex {vertex1}")

        if not 0 <= vertex2 < self.vertices_number:
            raise NoSuchVertexError(f"No vertex {vertex2}")

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))
        self._graphrepr[vertex2].add((vertex1, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        if not 0 <= vertex < self.vertices_number:
            raise NoSuchVertexError(f"No vertex {vertex}")

        return self.get_outdegree(vertex)

    def to_directed(self):
        diedges = list(self.get_edges()) + [(u, v) for v, u in self.get_edges()]
        return DirectedSimpleGraph(self.vertices_number, edges=diedges)


class UndirectedWeightedSimpleGraph(UndirectedSimpleGraph, UndirectedWeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for edge in map(lambda e: e
                            if len(e) > 2 else (e[0], e[1], self._DEFAULT_WEIGHT), edges):
                self.add_weighted_edge(edge[0], edge[1], edge[2])

    def get_weighted_edges(self):
        return ((v, u, wg) for v in self.get_vertices() for u, wg in self.get_weighted_neighbours(v)
                if u > v)

    def add_weighted_edge(self, vertex1, vertex2, weight):
        if not 0 <= vertex1 < self.vertices_number:
            raise NoSuchVertexError(str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise NoSuchVertexError(str(vertex2))

        self._graphrepr[vertex1].add((vertex2, weight))
        self._graphrepr[vertex2].add((vertex1, weight))

    def get_weighted_neighbours(self, vertex):
        if not 0 <= vertex < self.vertices_number:
            raise NoSuchVertexError(str(vertex))

        return iter(self._graphrepr[vertex])

    def to_directed(self):
        diwedges = list(self.get_weighted_edges()) \
                   + [(u, v, wg) for v, u, wg in self.get_weighted_edges()]
        return DirectedWeightedSimpleGraph(self.vertices_number, edges=diwedges)
