# -*- coding: utf-8 -*-
"""Structure of basic graphs"""
from abc import ABCMeta, abstractmethod


class Graph(metaclass=ABCMeta):
    @property
    @abstractmethod
    def vertices_count(self):
        """:return: number of vertices"""
        pass

    @property
    @abstractmethod
    def vertices(self):
        """:return: sorted list of vertices"""
        pass

    @property
    @abstractmethod
    def edges_count(self):
        """:return: number of edges"""
        pass

    @property
    @abstractmethod
    def edges(self):
        """:return: sorted list of edges"""
        pass

    @abstractmethod
    def get_vertex(self, index):
        """:param index: vertex index
        :return: vertex with the index
        :raise IndexError: if no vertex found"""
        pass

    @abstractmethod
    def get_edge(self, source, destination):
        """:param source: source vertex
        :param destination: destination vertex
        :return: edge between the vertices, or ``None`` of no edge"""
        pass

    @abstractmethod
    def get_neighbours(self, vertex):
        """:param vertex: a vertex from this graph
        :return: generator of neighbouring vertices"""
        pass

    @abstractmethod
    def get_adjacent_edges(self, vertex):
        """:param vertex: a vertex from this graph
        :return: generator of edges adjacent to this vertex"""
        pass

    @abstractmethod
    def get_output_degree(self, vertex):
        """:param vertex: a vertex from this graph
        :return: the output degree of this vertex"""
        pass

    @abstractmethod
    def get_input_degree(self, vertex):
        """:param vertex: a vertex from this graph
        :return: the input degree of this vertex"""
        pass


class Vertex:
    def __init__(self, index, vertex_property):
        self._index = index
        self.property = vertex_property

    @property
    def index(self):
        return self._index

    def __hash__(self):
        return hash(self._index)

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __lt__(self, other):
        return self.index < other.index

    def __le__(self, other):
        return self.index <= other.index

    def __gt__(self, other):
        return self.index > other.index

    def __ge__(self, other):
        return self.index > other.index

    def __str__(self):
        return f"Vertex{{{self._index} ({self.property})}}"


class Edge:
    def __init__(self, source, destination, edge_property):
        self._source = source
        self._destination = destination
        self.property = edge_property

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

        raise ValueError(f"Edge {self} is not adjacent to given vertex {vertex}")

    def reversed(self):
        return Edge(self._destination, self._source, self.property)

    def __hash__(self):
        return hash((self.source, self._destination))

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
        return f"Edge{{{self._source} -> {self._destination} ({self.property})}}"
