# -*- coding: utf-8 -*-
"""MULTIPARTITE GRAPHS STRUCTURE"""
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class GraphPartitionException(ValueError):
    pass


class MultipartiteGraph(UndirectedGraph):
    def __init__(self, g, n, groups):
        super().__init__()
        if len(groups) != n:
            raise ValueError("Groups mapping is not consistent with vertices number")

        if not all(0 <= grp < g for grp in groups):
            raise ValueError("Groups mapping is not consistent with maximal groups number")

        self.__graph = UndirectedSimpleGraph(n)  # Struktura grafu wielodzielnego.
        self.__groups_number = g  # Maksymalna liczba grup wierzchołków.
        self.__groups = list(groups)  # Numery grup wierzchołków.

    @property
    def groups_number(self):
        return self.__groups_number

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    def get_vertices(self, group=None):
        """:param group: numer grupy wierzchołków
        :returns: generator wierzchołków z zadanej grupy"""
        if group is None:
            return self.__graph.get_vertices()

        return (v for v in self.__graph.get_vertices() if self.__groups[v] == group)

    def add_vertex(self, neighbours=None, group=0):
        """Dodawanie nowego wierzchołka do zadanej grupy.
        :param group: numer grupy
        :returns: oznaczenie wierzchołka"""
        v = self.__graph.add_vertex(neighbours)
        self.__groups.append(group)

        return v

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_edges(self):
        return self.__graph.get_edges()

    def add_edge(self, vertex1, vertex2):
        if self.is_same_group(vertex1, vertex2):
            raise GraphPartitionException()

        self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex, group=None):
        """:param vertex: numer wierzchołka
        :param group: numer grupy sąsiadów
        :returns: generator sąsiadów wierzchołka z zadanej grupy"""
        if group is None:
            return self.__graph.get_neighbours(vertex)

        return (v for v in self.__graph.get_neighbours(vertex) if self.__groups[v] == group)

    def get_outdegree(self, vertex):
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        return self.__graph.get_indegree(vertex)

    def to_directed(self):
        return self.__graph.to_directed()

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
