# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW SKIEROWANYCH"""
from .graph import SimpleGraph, WeightedGraph


class DirectedGraph(SimpleGraph):
    def __init__(self, n, edges=None):
        super().__init__(n, edges=edges)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add(e[1])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v))

    def add_edge(self, vertex1, vertex2):
        """:meth: Graph.add_edge"""
        if not 0 <= vertex1 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex2))

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        """:meth: Graph.get_indegree"""
        return sum(1 for _, v in self.get_edges() if v == vertex)

    def reverse(self):
        """Odwracanie skierowania grafu"""
        revgraph = [set() for _ in self.vertices_number()]

        for v, u in self.get_edges():
            revgraph[u].add((v, self._DEFAULT_WEIGHT))

        self._graphrepr = revgraph


class DirectedWeightedGraph(DirectedGraph, WeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add(e[1:3])

    def get_weighted_edges(self):
        """:meth: WeightedGraph.get_weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices()
                for u, wg in self.get_weighted_neighbours(v))

    def add_weighted_edge(self, vertex1, vertex2, weight):
        """:meth: WeightedGraph.add_weighted_edge"""
        if not 0 <= vertex1 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex1))

        if not 0 <= vertex2 < self.vertices_number:
            raise IndexError("No such vertex: " + str(vertex2))

        self._graphrepr[vertex1].add((vertex2, weight))

    def get_weighted_neighbours(self, vertex):
        """:meth: WeightedGraph.get_weighted_neighbours"""
        return iter(self._graphrepr[vertex])

    def reverse(self):
        """:meth: DirectedGraph.reverse"""
        revgraph = [set() for _ in self.vertices_number()]

        for v, u, wg in self.get_weighted_edges():
            revgraph[u].add((v, wg))

        self._graphrepr = revgraph
