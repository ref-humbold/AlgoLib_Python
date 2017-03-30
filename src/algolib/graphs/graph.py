# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW"""
from abc import ABCMeta, abstractmethod
import math

class Graph(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def vertices_number(self):
        """Getter dla liczby wierzchołków.
        :returns: liczba wierzchołków"""
        pass

    @property
    @abstractmethod
    def edges_number(self):
        """Getter dla liczby krawędzi.
        :returns: liczba krawędzi"""
        pass

    def get_vertices(self):
        """Wszystkie wierzchołki.
        :returns: generator wierzchołków"""
        return (v for v in range(self.vertices_number))

    @abstractmethod
    def get_edges(self):
        """Wszystkie krawędzie.
        :returns: generator krawędzi"""
        pass

    @abstractmethod
    def get_neighbours(self, v):
        """Sąsiedzi wierzchołka.
        :param v: numer wierzchołka
        :returns: generator sąsiadów wierzchołka"""
        pass

    @abstractmethod
    def get_outdegree(self, v):
        """Stopień wyjściowy wierzchołka.
        :param v: numer wierzchołka
        :returns: wartość stopnia wyjściowego wierzchołka"""
        pass

    @abstractmethod
    def get_indegree(self, v):
        """Stopień wejściowy wierzchołka.
        :param v: numer wierzchołka
        :returns: wartość stopnia wejściowego wierzchołka"""
        pass


class DirectedGraph(Graph, metaclass=ABCmeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UndirectedGraph(Graph, metaclass=ABCmeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SimpleGraph(Graph, metaclass=ABCMeta):
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graphrepr = [[] for i in range(n)]    # Lista sąsiedztwa grafu.

    def verices_number(self):
        """meth: Graph.vertices_number"""
        return len(self._graphrepr)

    def get_neighbours(self, v):
        """:meth: Graph.neighbours"""
        return iter(self._graphrepr[v])

    def get_outdegree(self, v):
        """:meth: Graph.get_outdegree"""
        return self._graphrepr[v]

    def adjacency_list(self):
        """Wyznaczanie listy sąsiedztwa grafu.
        :returns: lista sąsiedztwa"""
        return self._graphrepr

    def get_adjacency_matrix(self):
        """Wyznaczanie macierzy sąsiedztwa grafu.
        :returns: macierz sąsiedztwa"""
        matrix = [[False]*self.vertices_number for _ in self.vertices_number]

        for v in self.get_vertices():
            for u in self.get_neighbours(v):
                matrix[v][u] = True

        return matrix


class WeightedGraph(Graph, metaclass=ABCMeta):
    INF = math.inf

    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graphrepr = [[] for i in range(n)]    # Lista sąsiedztwa grafu.

    def verices_number(self):
        """meth: Graph.vertices_number"""
        return len(self._graphrepr)

    @abstractmethod
    def get_weighted_edges(self):
        """Wszystkie krawędzie wraz z wagami.
        :returns: lista krawędzi z ich wagami"""
        pass

    def get_neighbours(self, v):
        """:meth: Graph.neighbours"""
        return (i[0] for i in self._graphrepr[v])

    def get_weighted_neighbours(self, v):
        """Sąsiedzi wierzchołka wraz z wagami.
        :param v: numer wierzchołka
        :returns: lista sąsiadów wierzchołka wraz z wagami krawędzi"""
        return iter(self._graphrepr[v])

    def get_outdegree(self, v):
        """:meth: Graph.get_outdegree"""
        return self._graphrepr[v]

    def adjacency_list(self):
        """Wyznaczanie listy sąsiedztwa grafu.
        :returns: lista sąsiedztwa"""
        return self._graphrepr

    def get_adjacency_matrix(self):
        """Wyznaczanie macierzy sąsiedztwa grafu.
        :returns: macierz sąsiedztwa"""
        matrix = [[0.0 if v == u else self.INF for v in self.get_vertices()] \
                  for u in self.get_vertices()]

        for v in self.get_vertices():
            for u, wg in self.get_weighted_neighbours(v):
                matrix[v][u] = wg

        return matrix


class DirectedSimpleGraph(SimpleGraph, DirectedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].append(e[1])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_indegree(self, v):
        """:meth: Graph.get_indegree"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v) if u == v)


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].append(e[1])
                self._graphrepr[e[1]].append(e[0])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(0.5 for v in self.get_vertices() for u in self.get_neighbours(v) if u > v)

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u in self.get_neighbours(v) if u > v)

    def get_indegree(self, v):
        """:meth: Graph.get_indegree"""
        return self.get_outdegree(v)


class DirectedWeightedGraph(WeightedGraph, DirectedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].append(e[1:3])

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v))

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u, wg in self.get_neighbours(v))

    def get_weighted_edges(self):
        """:meth: WeightedGraph.weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices() for u, wg in self.get_neighbours(v))

    def get_indegree(self, v):
        """:meth: Graph.get_indegree"""
        return sum(1 for v in self.get_vertices() for u in self.get_neighbours(v) if u == v)


class UndirectedWeightedGraph(WeightedGraph, UndirectedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[e[0]].append(e[1:3])
                self._graphrepr[e[1]].append((e[0], e[3]))

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(0.5 for v in self.get_vertices() for u in self.get_neighbours(v) if u > v)

    def get_edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.get_vertices() for u, wg in self.get_neighbours(v) if u > v)

    def get_weighted_edges(self):
        """:meth: WeightedGraph.weighted_edges"""
        return ((v, u, wg) for v in self.get_vertices() for u, wg in self.get_neighbours(v) \
                if u > v)

    def get_indegree(self, v):
        """:meth: Graph.get_indegree"""
        return self.get_outdegree(v)
