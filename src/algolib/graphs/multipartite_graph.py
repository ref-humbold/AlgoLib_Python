# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW WIELODZIELNYCH"""
from .graph import Graph


class GraphPartitionException(Exception):
    def __init__(self):
        super().__init__()


class MultipartiteGraph(Graph):
    def __init__(self, group, ugraph, edges=None):
        super().__init__()
        # Struktura grafu wielodzielnego.
        self.__graph = ugraph
        # Maksymalna liczba grup wierzchołków.
        self.__groups_number = group
        # Numery grup wierzchołków.
        self.__groups = []

        if edges is not None:
            for e in edges:
                if self.is_same_group(e[0], e[1]):
                    raise GraphPartitionException()

    @property
    def groups_number(self):
        return self.__groups_number

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_vertices(self, group=None, **kwargs):
        """meth: Graph.get_vertices
        :param group: numer grupy wierzchołków"""
        if group is None:
            return self.__graph.get_vertices()

        return (v for v in self.__graph.get_vertices() if self.__groups[v] == group)

    def get_edges(self):
        """meth: Graph.get_edges"""
        return self.__graph.get_edges()

    def add_vertex(self, group=1, **kwargs):
        """meth: Graph.add_vertex
        :param group: numer grupy wierzchołka"""
        self.__groups.append(group)
        self.__graph.add_vertex()

    def add_edge(self, vertex1, vertex2):
        """meth: Graph.add_edge"""
        if self.is_same_group(vertex1, vertex2):
            raise GraphPartitionException()

        self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex, group=None, **kwargs):
        """meth: Graph.get_neighbours
        :param group: numer grupy sąsiadów"""
        if group is None:
            return self.__graph.get_neighbours(vertex)

        return (v for v in self.__graph.get_neighbours(vertex) if self.__groups[v] == group)

    def get_outdegree(self, vertex):
        """meth: Graph.get_outdegree"""
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        """meth: Graph.get_indegree"""
        return self.__graph.get_indegree(vertex)

    def is_in_group(self, vertex, group):
        """Sprawdzanie, czy wierzchołek nalezy do zadanej grupy.
        :param vertex: wierzchołek
        :param group: numer grupy
        :returns: czy wierzchołek jest w grupie"""
        return self.__groups[vertex] == group

    def is_same_group(self, vertex1, vertex2):
        """Sprawdzanie, czy wierzchołki należą do tej samej grupy.
        :param vertex1: pierwszy wierzchołek
        :param vertex2: drugi wierzchołek
        :returns: czy wierzchołki są w jednej grupie"""
        return self.__groups[vertex1] == self.__groups[vertex2]
