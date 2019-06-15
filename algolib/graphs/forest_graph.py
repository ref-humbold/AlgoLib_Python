# -*- coding: utf-8 -*-
"""TREE GRAPHS STRUCTURE"""
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph
from ..structures import DisjointSets


class CycleException(ValueError):
    pass


class ForestGraph(UndirectedGraph):
    def __init__(self, n, edges=None):
        super().__init__()
        self.__graph = UndirectedSimpleGraph(n)  # Struktura grafu drzew.
        self.__components = DisjointSets(self.__graph.get_vertices())  # Struktura składowych drzew.

        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    @property
    def trees_number(self):
        return len(self.__components)

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    def get_vertices(self):
        return self.__graph.get_vertices()

    def add_vertex(self):
        vertex = self.__graph.add_vertex()
        self.__components += (vertex,)

        return vertex

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_edges(self):
        return self.__graph.get_edges()

    def add_edge(self, vertex1, vertex2):
        if self.is_same_tree(vertex1, vertex2):
            raise CycleException()

        self.__components.union_set(vertex1, vertex2)
        self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex):
        return self.__graph.get_neighbours(vertex)

    def get_outdegree(self, vertex):
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        return self.__graph.get_indegree(vertex)

    def as_directed(self):
        return self.__graph.as_directed()

    def is_same_tree(self, vertex1, vertex2):
        """Sprawdzanie, czy wierzchołki należą do tego samego drzewa.
        :param vertex1: pierwszy wierzchołek
        :param vertex2: drugi wierzchołek
        :returns: czy wierzchołki są w jednym drzewie"""
        return self.__components.is_same_set(vertex1, vertex2)
