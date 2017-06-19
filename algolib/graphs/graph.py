# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW"""
from abc import ABCMeta, abstractmethod
import math


class Graph(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

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
        """Wszystkie wierzchołki.
        :returns: generator wierzchołków"""
        pass

    @abstractmethod
    def get_edges(self):
        """Wszystkie krawędzie.
        :returns: generator krawędzi"""
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
        """Sąsiedzi wierzchołka.
        :param vertex: numer wierzchołka
        :returns: generator sąsiadów wierzchołka"""
        pass

    @abstractmethod
    def get_outdegree(self, vertex):
        """Stopień wyjściowy wierzchołka.
        :param vertex: numer wierzchołka
        :returns: wartość stopnia wyjściowego wierzchołka"""
        pass

    @abstractmethod
    def get_indegree(self, vertex):
        """Stopień wejściowy wierzchołka.
        :param vertex: numer wierzchołka
        :returns: wartość stopnia wejściowego wierzchołka"""
        pass


class WeightedGraph(Graph, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_weighted_edges(self):
        """Wszystkie krawędzie wraz z ich wagami.
        :returns: generator krawędzi z wagami"""
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
        """Sąsiedzi wierzchołka wraz z wagami.
        :param vertex: numer wierzchołka
        :returns: lista sąsiadów wierzchołka wraz z wagami krawędzi"""
        pass


class SimpleGraph(Graph, metaclass=ABCMeta):
    # Oznaczenie nieskończoności.
    INF = math.inf
    # Domyślna waga krawędzi.
    _DEFAULT_WEIGHT = 1.0

    def __init__(self, n):
        super().__init__()
        # Lista sąsiedztwa grafu.
        self._graphrepr = [set() for i in range(n)]

    @property
    def vertices_number(self):
        return len(self._graphrepr)

    def get_vertices(self):
        """meth: Graph.get_vertices"""
        return (v for v in range(self.vertices_number))

    def add_vertex(self, **kwargs):
        """meth: Graph.add_vertex"""
        self._graphrepr.append(set())

        return len(self._graphrepr) - 1

    def get_neighbours(self, vertex):
        """:meth: Graph.get_neighbours"""
        return map(lambda wv: wv[0], self._graphrepr[vertex])

    def get_outdegree(self, vertex):
        """:meth: Graph.get_outdegree"""
        return self._graphrepr[vertex]


class DirectedGraph(SimpleGraph):
    def __init__(self, n, edges=None):
        super().__init__(n, edges=edges)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add(e[1])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v))

    def add_edge(self, vertex1, vertex2):
        """:meth: Graph.add_edge"""
        if not (0 < vertex1 < self.vertices_number and 0 < vertex2 < self.vertices_number):
            raise IndexError("No such vertex.")

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        """:meth: Graph.get_indegree"""
        return sum(1 for _, v in self.get_edges() if v == vertex)

    def reverse(self):
        """Odwracanie skierowania grafu"""
        revgraph = [set() for _ in self.vertices_number()]

        for v, u in self.get_edges():
            revgraph[u].add((v, self._DEFAULT_WEIGHT))

        self._graphrepr = revgraph


class DirectedWeightedGraph(DirectedGraph, WeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add(e[1:3])

    def get_weighted_edges(self):
        """:meth: WeightedGraph.get_weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices()
                for u, wg in self.get_weighted_neighbours(v))

    def add_weighted_edge(self, vertex1, vertex2, weight):
        """:meth: WeightedGraph.add_weighted_edge"""
        if not (0 < vertex1 < self.vertices_number and 0 < vertex2 < self.vertices_number):
            raise IndexError("No such vertex.")

        self._graphrepr[vertex1].add((vertex2, weight))

    def get_weighted_neighbours(self, vertex):
        """:meth: WeightedGraph.get_weighted_neighbours"""
        return iter(self._graphrepr[vertex])

    def reverse(self):
        """:meth: DirectedGraph.reverse"""
        revgraph = [set() for _ in self.vertices_number()]

        for v, u, wg in self.get_weighted_edges():
            revgraph[u].add((v, wg))

        self._graphrepr = revgraph


class UndirectedGraph(SimpleGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add(e[1])
                self._graphrepr[e[1]].add(e[0])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(self.get_outdegree(v) + 1
                   if v in self.get_neighbours(v)
                   else self.get_outdegree(v)
                   for v in self.get_vertices()) / 2

    def get_edges(self):
        """:meth: Graph.get_edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v) if u > v)

    def add_edge(self, vertex1, vertex2):
        """:meth: Graph.add_edge"""
        if not (0 < vertex1 < self.vertices_number and 0 < vertex2 < self.vertices_number):
            raise IndexError("No such vertex.")

        self._graphrepr[vertex1].add((vertex2, self._DEFAULT_WEIGHT))
        self._graphrepr[vertex2].add((vertex1, self._DEFAULT_WEIGHT))

    def get_indegree(self, vertex):
        """:meth: Graph.get_indegree"""
        return self.get_outdegree(vertex)

    def as_directed(self):
        """Zamiana krawędzi nieskierowanych na skierowane.
        :returns: graf ze skierowanymi krawędziami"""
        diedges = list(self.get_edges()) + [(u, v) for v, u in self.get_edges()]

        return DirectedGraph(self.vertices_number, edges=diedges)


class UndirectedWeightedGraph(UndirectedGraph, WeightedGraph):
    def __init__(self, n, edges=None):
        super().__init__(n)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].add((e[1], e[2]))
                self._graphrepr[e[1]].add((e[0], e[2]))

    def get_weighted_edges(self):
        """:meth: WeightedGraph.get_weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices() for u, wg in self.get_weighted_neighbours(v)
                if u > v)

    def add_weighted_edge(self, vertex1, vertex2, weight):
        """:meth: WeightedGraph.add_weighted_edge"""
        if not (0 < vertex1 < self.vertices_number and 0 < vertex2 < self.vertices_number):
            raise IndexError("No such vertex.")

        self._graphrepr[vertex1].add((vertex2, weight))
        self._graphrepr[vertex2].add((vertex1, weight))

    def get_weighted_neighbours(self, vertex):
        """:meth: WeightedGraph.get_weighted_neighbours"""
        return iter(self._graphrepr[vertex])

    def as_directed(self):
        """Zamiana krawędzi nieskierowanych na skierowane z zachowaniem wag.
        :returns: graf ze skierowanymi krawędziami ważonymi"""
        diwedges = list(self.get_weighted_edges()) \
            + [(u, v, wg) for v, u, wg in self.get_weighted_edges()]

        return DirectedWeightedGraph(self.vertices_number, edges=diwedges)
