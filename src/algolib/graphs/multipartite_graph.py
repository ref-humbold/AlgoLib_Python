# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW WIELODZIELNYCH"""
from abc import ABCMeta
from .graph import Graph

class GraphgroupitionException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MultigroupiteGraph(Graph, metaclass=ABCMeta):
    def __init__(self, group, graph, *args, edges=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__graph = graph    # Struktura grafu wielodzielnego.
        self.__groups_number = group    # Maksymalna liczba grup wierzchołków.
        self.__groups = []    # Numery grup wierzchołków.

        if edges is not None:
            for e in edges:
                if self.is_same_group(e[0], e[1]):
                    raise GraphgroupitionException()

    @property
    def groups_number(self):
        return self.__groups_number

    @property
    def vertices_number(self):
        return self.__graph.vertices_number

    @property
    def edges_number(self):
        return self.__graph.edges_number

    def get_vertices(self):
        return self.__graph.get_vertices()

    def get_edges(self):
        return self.__graph.get_edges()

    def get_neighbours(self, vertex):
        return self.__graph.get_neighbours(vertex)

    def get_outdegree(self, vertex):
        return self.__graph.get_outdegree(vertex)

    def get_indegree(self, vertex):
        return self.__graph.get_indegree(vertex)

    def get_group(self, group):
        """Wierzchołki zadanej grupy.
        :param group: numer grupy
        :returns: generator wierzchołków z pierwszej grupy"""
        return (v for v in self.get_vertices() if self.__groups[v] == group)

    def is_in_group(self, vertex, group):
        """Sprawdza, czy wierzchołek nalezy do pierwszej grupy.
        :param vertex: wierzchołek
        :param group: numer grupy
        :returns: czy wierzchołek jest w pierwszej grupie"""
        return self.__groups[vertex] == group

    def is_same_group(self, vertex1, vertex2):
        """Sprawdza, czy  wierzchołki są w różnych grupach.
        :param vertex1: pierwszy wierzchołek
        :param vertex2: drugi wierzchołek
        :returns: czy wierzchołki są w różnych grupach"""
        return self.__groups[vertex1] == self.__groups[vertex2]
