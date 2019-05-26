# -*- coding: utf-8 -*-
"""TREE GRAPHS STRUCTURE"""
from .graph import Graph
from .undirected_graph import UndirectedSimpleGraph
from ..structures.disjoint_sets import DisjointSets


class CycleException(ValueError):
    pass


class NotConnectedException(ValueError):
    pass


class TreeGraph(Graph):
    def __init__(self, n, edges):
        super().__init__()
        self.__graph = UndirectedSimpleGraph(n)  # Struktura grafu drzewa.

        dis = DisjointSets(self.__graph.get_vertices())

        for e in edges:
            if dis.is_same_set(e[0], e[1]):
                raise CycleException(f"Edge from {e[0]} to {e[1]} may create a cycle")

            self.__graph.add_edge(e[0], e[1])
            dis.union_set(e[0], e[1])

        if len(dis) > 1:
            raise NotConnectedException(f"Tree is not a connected graph")

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    def get_vertices(self):
        return self.__graph.get_vertices()

    def add_vertex(self, neighbours=None):
        if neighbours is None or len(neighbours) == 0:
            raise CycleException(f"New vertex won't be connected with the rest of the tree")

        if len(neighbours) > 1:
            raise CycleException(f"More than one edge from new vertex may create a cycle")

        vertex = self.__graph.add_vertex(neighbours)

        return vertex

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_edges(self):
        return self.__graph.get_edges()

    def add_edge(self, vertex1, vertex2):
        raise CycleException(f"New edge from {vertex1} to {vertex2} may create a cycle")

    def get_neighbours(self, vertex):
        return self.__graph.get_neighbours(vertex)

    def get_outdegree(self, vertex):
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        return self.__graph.get_indegree(vertex)
