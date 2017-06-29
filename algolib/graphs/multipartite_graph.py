# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW WIELODZIELNYCH"""
from .undirected_graph import UndirectedGraph


class GraphPartitionException(Exception):
    def __init__(self):
        super().__init__()


class MultipartiteGraph(UndirectedGraph):
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
        """:param group: numer grupy wierzchołków
        :returns: generator wierzchołków z zadanej grupy"""
        if group is None:
            return self.__graph.get_vertices()

        return (v for v in self.__graph.get_vertices() if self.__groups[v] == group)

    def get_edges(self):
        return self.__graph.get_edges()

    def add_vertex(self, group=1, **kwargs):
        """Dodawanie nowego wierzchołka do zadanej grupy.
        :param group: numer grupy
        :returns: oznaczenie wierzchołka"""
        self.__groups.append(group)
        self.__graph.add_vertex()

    def add_edge(self, vertex1, vertex2):
        if self.is_same_group(vertex1, vertex2):
            raise GraphPartitionException()

        self.__graph.add_edge(vertex1, vertex2)

    def get_neighbours(self, vertex, group=None, **kwargs):
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

    def as_directed(self):
        return self.__graph.as_directed

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
