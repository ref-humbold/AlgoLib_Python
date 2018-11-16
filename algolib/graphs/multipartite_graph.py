# -*- coding: utf-8 -*-
"""MULTIPARTITE GRAPHS STRUCTURE"""
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class GraphPartitionException(ValueError):
    pass


class MultipartiteGraph(UndirectedGraph):
    def __init__(self, n, gr):
        super().__init__()
        # Struktura grafu wielodzielnego.
        self.__graph = UndirectedSimpleGraph(n)
        # Maksymalna liczba grup wierzchołków.
        self.__groups_number = gr
        # Numery grup wierzchołków.
        self.__groups = [0] * self.__graph.vertices_number

    @property
    def groups_number(self):
        return self.__groups_number

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    def get_vertices(self, *, group=None):
        """:param group: numer grupy wierzchołków
        :returns: generator wierzchołków z zadanej grupy"""
        if group is None:
            return self.__graph.get_vertices()

        return (v for v in self.__graph.get_vertices() if self.__groups[v] == group)

    def add_vertex(self, *, group=0):
        """Dodawanie nowego wierzchołka do zadanej grupy.
        :param group: numer grupy
        :returns: oznaczenie wierzchołka"""
        self.__groups.append(group)

        return self.__graph.add_vertex()

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_edges(self):
        return self.__graph.get_edges()

    def add_edge(self, vertex1, vertex2):
        if self.is_same_group(vertex1, vertex2):
            raise GraphPartitionException()

        self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex, *, group=None):
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
