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

    def vertices(self):
        """Wszystkie wierzchołki.
        :returns: generator wierzchołków"""
        return ( v for v in range(self._vertices_number) )


    @abstractmethod
    def edges(self):
        """Wszystkie krawędzie.
        :returns: generator krawędzi"""
        pass

    @abstractmethod
    def neighbours(self, v):
        """Sąsiedzi wierzchołka.
        :param v: numer wierzchołka
        :returns: generator sąsiadów wierzchołka"""
        pass


class SimpleGraph(Graph, metaclass=ABCMeta):
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graphrepr = [ [] for i in range(n) ]    # Lista sąsiedztwa grafu.

    def verices_number(self):
        """meth: Graph.vertices_number"""
        return len(self._graphrepr)

    def neighbours(self, v):
        """:meth: Graph.neighbours"""
        return iter( self._graphrepr[v] )

    def adjacency_list(self):
        """Wyznaczanie listy sąsiedztwa grafu.
        :returns: lista sąsiedztwa"""
        return self._graphrepr

    def adjacency_matrix(self):
        """Wyznaczanie macierzy sąsiedztwa grafu.
        :returns: macierz sąsiedztwa"""
        matrix = [ [False]*self._vertices_number for _ in self._vertices_number ]

        for v in self.vertices():
            for u in self.neighbours(v):
                matrix[v][u] = True

        return matrix


class DirectedSimpleGraph(SimpleGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[ e[0] ].append( e[1] )

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum( 1 for v in self.vertices() for u in self.neighbours(v) )

    def edges(self):
        """:meth: Graph.edges"""
        return ( (v, u) for v in self.vertices() for u in self.neighbours(v) )


class UndirectedSimpleGraph(SimpleGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[ e[0] ].append( e[1] )
                self._graphrepr[ e[1] ].append( e[0] )

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.vertices() for u in self.neighbours(v) if u > v)

    def edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.vertices() for u in self.neighbours(v) if u > v)


class WeightedGraph(Graph, metaclass=ABCMeta):
    _INF = math.inf

    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._graphrepr = [ [] for i in range(n) ]    # Lista sąsiedztwa grafu.

    def verices_number(self):
        """meth: Graph.vertices_number"""
        return len(self._graphrepr)

    @abstractmethod
    def weighted_edges(self):
        """Wszystkie krawędzie wraz z wagami.
        :returns: lista krawędzi z ich wagami"""
        pass

    def neighbours(self, v):
        """:meth: Graph.neighbours"""
        return ( i[0] for i in self._graphrepr[v] )

    def weighted_neighbours(self, v):
        """Sąsiedzi wierzchołka wraz z wagami.
        :param v: numer wierzchołka
        :returns: lista sąsiadów wierzchołka wraz z wagami krawędzi"""
        return iter( self._graphrepr[v] )

    def adjacency_list(self):
        """Wyznaczanie listy sąsiedztwa grafu.
        :returns: lista sąsiedztwa"""
        return self._graphrepr

    def adjacency_matrix(self):
        """Wyznaczanie macierzy sąsiedztwa grafu.
        :returns: macierz sąsiedztwa"""
        matrix = [ [0.0 if v == u else _INF for v in self.vertices()] for u in self.vertices()]

        for v in self.vertices():
            for u, wg in self.weighted_neighbours(v):
                matrix[v][u] = wg

        return matrix


class DirectedWeightedGraph(WeightedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[ e[0] ].append( e[1:3] )

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum( 1 for v in self.vertices() for u in self.neighbours(v) )

    def edges(self):
        """:meth: Graph.edges"""
        return ( (v, u) for v in self.vertices() for u, wg in self.neighbours(v) )

    def weighted_edges(self):
        """:meth: WeightedGraph.weighted_edges"""
        return ( (v, u, wg) for v in self.vertices() for u, wg in self.neighbours(v) )



class UndirectedWeightedGraph(WeightedGraph):
    def __init__(self, n, *args, edges=None, **kwargs):
        super().__init__(n, *args, **kwargs)

        if edges is not None:
            for e in edges:
                self._graphrepr[ e[0] ].append( e[1:3] )
                self._graphrepr[ e[1] ].append( (e[0], e[3]) )

    @property
    def edges_number(self):
        """:meth: Graph.edges_number"""
        return sum(1 for v in self.vertices() for u in self.neighbours(v) if u > v)

    def edges(self):
        """:meth: Graph.edges"""
        return ((v, u) for v in self.vertices() for u, wg in self.neighbours(v) if u > v)

    def weighted_edges(self):
        """:meth: WeightedGraph.weighted_edges"""
        return ((v, u, wg) for v in self.vertices() for u, wg in self.neighbours(v) if u > v)
