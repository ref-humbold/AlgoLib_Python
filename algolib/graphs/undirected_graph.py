# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW NIESKIEROWANYCH"""
from abc import ABCMeta, abstractmethod
from .graph import Graph, SimpleGraph, WeightedGraph
from .directed_graph import DirectedSimpleGraph, DirectedWeightedSimpleGraph


class UndirectedGraph(Graph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def as_directed(self):
        """Zamiana krawędzi nieskierowanych na skierowane.
        :returns: graf ze skierowanymi krawędziami"""
        pass


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(self.get_outdegree(v) + 1
                   if v in self.get_neighbours(v)
                   else self.get_outdegree(v)
                   for v in self.get_vertices()) / 2

    def get_edges(self):
        """:meth: Graph.get_edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v) if u >= v)

    def add_edge(self, vertex1, vertex2):
        """:meth: Graph.add_edge"""
        if not 0 <= vertex1 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex2))

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))
        self._graphrepr[vertex2].add((vertex1, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        """:meth: Graph.get_indegree"""
        return self.get_outdegree(vertex)

    def as_directed(self):
        """:meth: UndirectedGraph.as_directed"""
        diedges = list(self.get_edges()) + [(u, v) for v, u in self.get_edges()]

        return DirectedSimpleGraph(self.vertices_number, edges=diedges)


class UndirectedWeightedSimpleGraph(UndirectedSimpleGraph, WeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in map(lambda e: e if len(e) > 2 else (e[0], e[1], self._DEFAULT_WEIGHT), edges):
                self.add_weighted_edge(e[0], e[1], e[2])

    def get_weighted_edges(self):
        """:meth: WeightedGraph.get_weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices() for u, wg in self.get_weighted_neighbours(v)
                if u > v)

    def add_weighted_edge(self, vertex1, vertex2, weight):
        """:meth: WeightedGraph.add_weighted_edge"""
        if not 0 <= vertex1 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex2))

        self._graphrepr[vertex1].add((vertex2, weight))
        self._graphrepr[vertex2].add((vertex1, weight))

    def get_weighted_neighbours(self, vertex):
        """:meth: WeightedGraph.get_weighted_neighbours"""
        return iter(self._graphrepr[vertex])

    def as_directed(self):
        """:meth: UndirectedGraph.as_directed"""
        diwedges = list(self.get_weighted_edges()) \
            + [(u, v, wg) for v, u, wg in self.get_weighted_edges()]

        return DirectedWeightedSimpleGraph(self.vertices_number, edges=diwedges)
