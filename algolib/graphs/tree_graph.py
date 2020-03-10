# -*- coding: utf-8 -*-
"""TREE GRAPHS STRUCTURE"""
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph
from ..structures.disjoint_sets import DisjointSets


class CycleError(ValueError):
    pass


class NotConnectedError(ValueError):
    pass


class TreeGraph(UndirectedGraph):
    def __init__(self, n, edges):
        super().__init__()
        self._graph = UndirectedSimpleGraph(n)  # Struktura grafu drzewa

        components = DisjointSets(self._graph.get_vertices())

        for e in edges:
            if components.is_same_set(e[0], e[1]):
                raise CycleError(f"Edge from vertex {e[0]} to vertex {e[1]} may create a cycle")

            self._graph.add_edge(e[0], e[1])
            components.union_set(e[0], e[1])

        if len(components) > 1:
            raise NotConnectedError("Tree is not a connected graph")

    @property
    def vertices_number(self):
        return self._graph.vertices_number

    def get_vertices(self):
        return self._graph.get_vertices()

    def add_vertex(self, neighbours=None):
        if neighbours is None or len(neighbours) == 0:
            raise NotConnectedError("New vertex won't be connected with the rest of the tree")

        if len(neighbours) > 1:
            raise CycleError("More than one edge from new vertex may create a cycle")

        return self._graph.add_vertex(neighbours)

    @property
    def edges_number(self):
        return self._graph.edges_number

    def get_edges(self):
        return self._graph.get_edges()

    def add_edge(self, vertex1, vertex2):
        raise CycleError(f"Edge from vertex {vertex1} to vertex {vertex2} may create a cycle")

    def get_neighbours(self, vertex):
        return self._graph.get_neighbours(vertex)

    def get_outdegree(self, vertex):
        return self._graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        return self._graph.get_indegree(vertex)

    def to_directed(self):
        return self._graph.to_directed()
