# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW"""
from abc import ABCMeta, abstractmethod
import math


class Graph(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @property
    def inf(self):
        return math.inf

    @property
    @abstractmethod
    def vertices_number(self):
        pass

    @property
    @abstractmethod
    def edges_number(self):
        pass

    @abstractmethod
    def get_vertices(self, **kwargs):
        """:returns: generator wierzchołków"""
        pass

    @abstractmethod
    def get_edges(self):
        """:returns: generator krawędzi"""
        pass

    @abstractmethod
    def add_vertex(self, **kwargs):
        """Dodawanie nowego wierzchołka.
        :returns: oznaczenie wierzchołka"""
        pass

    @abstractmethod
    def add_edge(self, vertex1, vertex2):
        """Dodawanie nowej krawędzi.
        :param vertex1: początkowy wierzchołek
        :param vertex2: końcowy wierzchołek"""
        pass

    @abstractmethod
    def get_neighbours(self, vertex, **kwargs):
        """:param vertex: numer wierzchołka
        :returns: generator sąsiadów wierzchołka"""
        pass

    @abstractmethod
    def get_outdegree(self, vertex):
        """:param vertex: numer wierzchołka
        :returns: stopień wyjściowy wierzchołka"""
        pass

    @abstractmethod
    def get_indegree(self, vertex):
        """:param vertex: numer wierzchołka
        :returns: stopień wejściowy wierzchołka"""
        pass


class WeightedGraph(Graph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_weighted_edges(self):
        """:returns: generator krawędzi z wagami"""
        pass

    @abstractmethod
    def add_weighted_edge(self, vertex1, vertex2, weight):
        """Dodawanie nowej krawędzi z jej wagą.
        :param vertex1: początkowy wierzchołek
        :param vertex2: końcowy wierzchołek
        :param weight: waga krawędzi"""
        pass

    @abstractmethod
    def get_weighted_neighbours(self, vertex):
        """:param vertex: numer wierzchołka
        :returns: lista sąsiadów wierzchołka wraz z wagami krawędzi"""
        pass


class SimpleGraph(Graph, metaclass=ABCMeta):
    # Domyślna waga krawędzi.
    _DEFAULT_WEIGHT = 1.0

    def __init__(self, n):
        super().__init__()
        # Lista sąsiedztwa grafu.
        self._graphrepr = [set() for i in range(n)]

    @property
    def vertices_number(self):
        return len(self._graphrepr)

    @property
    @abstractmethod
    def edges_number(self):
        pass

    def get_vertices(self):
        return (v for v in range(self.vertices_number))

    @abstractmethod
    def get_edges(self):
        pass

    def add_vertex(self, **kwargs):
        self._graphrepr.append(set())

        return len(self._graphrepr) - 1

    @abstractmethod
    def add_edge(self, vertex1, vertex2):
        pass

    def get_neighbours(self, vertex):
        return (v for v in map(lambda wv: wv[0], self._graphrepr[vertex]))

    def get_outdegree(self, vertex):
        return len(self._graphrepr[vertex])

    @abstractmethod
    def get_indegree(self, vertex):
        pass
