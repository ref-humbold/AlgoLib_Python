# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW DRZEW"""
from .graph import Graph
from ..structures import DisjointSets


class CycleCreationException(Exception):
    def __init__(self):
        super().__init__()


class TreeGraph(Graph):
    def __init__(self, ugraph, edges=None):
        super().__init__()
        # Struktura grafu drzewa.
        self.__graph = ugraph
        # Struktura składowych drzewa.
        self.__components = DisjointSets(ugraph.get_vertices())

        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_vertices(self):
        """meth: Graph.get_vertices"""
        return self.__graph.get_vertices()

    def get_edges(self):
        """meth: Graph.get_edges"""
        return self.__graph.get_edges()

    def add_vertex(self):
        """meth: Graph.add_vertex"""
        vertex = self.__graph.add_vertex()
        self.__components.make_set(vertex)

        return vertex

    def add_edge(self, vertex1, vertex2):
        """meth: Graph.get_edge"""
        if self.__components.is_same_set(vertex1, vertex2):
            raise CycleCreationException()

        self.__components.union_set(vertex1, vertex2)
        return self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex):
        """meth: Graph.get_neighbours"""
        return self.__graph.get_neighbours(vertex)

    def get_outdegree(self, vertex):
        """meth: Graph.get_outdegree"""
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        """meth: Graph.get_indegree"""
        return self.__graph.get_indegree(vertex)
