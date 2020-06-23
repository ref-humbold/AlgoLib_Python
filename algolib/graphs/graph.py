# -*- coding: utf-8 -*-
"""Structure of basic graph"""
from abc import ABCMeta, abstractmethod


class Graph(metaclass=ABCMeta):
    @property
    @abstractmethod
    def vertices_count(self):
        """:return: number of vertices"""

    @property
    @abstractmethod
    def edges_count(self):
        """:return: number of edges"""

    @property
    @abstractmethod
    def vertices(self):
        """:return: sorted list of vertices"""

    @property
    @abstractmethod
    def edges(self):
        """:return: sorted list of edges"""

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def __setitem__(self, item, value):
        pass

    @abstractmethod
    def get_edge(self, source, destination):
        """:param source: source vertex
        :param destination: destination vertex
        :return: edge between the vertices
        :raise KeyError: if no edge"""

    @abstractmethod
    def get_adjacent_edges(self, vertex):
        """:param vertex: a vertex from this graph
        :return: generator of edges adjacent to this vertex"""

    @abstractmethod
    def get_neighbours(self, vertex):
        """:param vertex: a vertex from this graph
        :return: generator of neighbouring vertices"""

    @abstractmethod
    def get_output_degree(self, vertex):
        """:param vertex: a vertex from this graph
        :return: the output degree of this vertex"""

    @abstractmethod
    def get_input_degree(self, vertex):
        """:param vertex: a vertex from this graph
        :return: the input degree of this vertex"""


class Edge:
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination

    @property
    def source(self):
        return self._source

    @property
    def destination(self):
        return self._destination

    def get_neighbour(self, vertex):
        if vertex is self._source:
            return self._destination

        if vertex is self._destination:
            return self._source

        raise ValueError(f"Edge {self} is not adjacent to the vertex {vertex}")

    def reversed(self):
        return Edge(self._destination, self._source)

    def __hash__(self):
        return hash((self._source, self._destination))

    def __eq__(self, other):
        return (self.source, self._destination) == (other.source, other.destination)

    def __ne__(self, other):
        return (self.source, self._destination) != (other.source, other.destination)

    def __lt__(self, other):
        return (self.source, self._destination) < (other.source, other.destination)

    def __le__(self, other):
        return (self.source, self._destination) <= (other.source, other.destination)

    def __gt__(self, other):
        return (self.source, self._destination) > (other.source, other.destination)

    def __ge__(self, other):
        return (self.source, self._destination) >= (other.source, other.destination)

    def __str__(self):
        return f"Edge{{{self._source} -> {self._destination}}}"
