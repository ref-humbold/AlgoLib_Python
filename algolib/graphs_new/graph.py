# -*- coding: utf-8 -*-
"""Structure of basic graph"""
from abc import ABCMeta, abstractmethod
from typing import Iterable, Union


class Graph(metaclass=ABCMeta):
    @property
    @abstractmethod
    def properties(self) -> "GraphProperties":
        pass

    @property
    @abstractmethod
    def vertices_count(self) -> int:
        """:return: number of vertices"""

    @property
    @abstractmethod
    def edges_count(self) -> int:
        """:return: number of edges"""

    @property
    @abstractmethod
    def vertices(self) -> Iterable["Vertex"]:
        """:return: iterable of vertices"""

    @property
    @abstractmethod
    def edges(self) -> Iterable["Edge"]:
        """:return: iterable of edges"""

    @abstractmethod
    def get_vertex(self, vertex_id) -> "Vertex":
        pass

    @abstractmethod
    def get_edge(self, source, destination) -> "Edge":
        pass

    @abstractmethod
    def adjacent_edges(self, vertex: "Vertex") -> Iterable["Edge"]:
        """:param vertex: vertex from the graph
        :return: iterable of edges adjacent to the vertex"""

    @abstractmethod
    def neighbours(self, vertex: "Vertex") -> Iterable["Vertex"]:
        """:param vertex: a vertex from the graph
        :return: iterable of neighbouring vertices"""

    @abstractmethod
    def output_degree(self, vertex: "Vertex") -> int:
        """:param vertex: vertex from the graph
        :return: output degree of the vertex"""

    @abstractmethod
    def input_degree(self, vertex: "Vertex") -> int:
        """:param vertex: vertex from the graph
        :return: input degree of the vertex"""

    class GraphProperties(metaclass=ABCMeta):
        @abstractmethod
        def __getitem__(self, item: Union["Vertex", "Edge"]):
            pass

        @abstractmethod
        def __setitem__(self, item: Union["Vertex", "Edge"], value):
            pass

        @abstractmethod
        def __delitem__(self, item: Union["Vertex", "Edge"]):
            pass


class Vertex:
    def __init__(self, identifier):
        self.identifier = identifier

    def __hash__(self):
        return hash(self.identifier)

    def __repr__(self):
        return f"Vertex({self.identifier!r})"

    def __str__(self):
        return f"Vertex({self.identifier})"

    def __eq__(self, vertex: "Vertex"):
        return self.identifier == vertex.identifier

    def __ne__(self, vertex: "Vertex"):
        return self.identifier != vertex.identifier

    def __lt__(self, vertex: "Vertex"):
        return self.identifier < vertex.identifier

    def __le__(self, vertex: "Vertex"):
        return self.identifier <= vertex.identifier

    def __gt__(self, vertex: "Vertex"):
        return self.identifier > vertex.identifier

    def __ge__(self, vertex: "Vertex"):
        return self.identifier >= vertex.identifier


class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __hash__(self):
        return hash((self.source, self.destination))

    def __repr__(self):
        return f"Edge({self.source!r}, {self.destination!r})"

    def __str__(self):
        return f"Edge{{{self.source} -- {self.destination}}}"

    def __eq__(self, edge: "Edge"):
        return (self.source, self.destination) == (edge.source, edge.destination)

    def __ne__(self, edge: "Edge"):
        return (self.source, self.destination) != (edge.source, edge.destination)

    def __lt__(self, edge: "Edge"):
        return (self.source, self.destination) < (edge.source, edge.destination)

    def __le__(self, edge: "Edge"):
        return (self.source, self.destination) <= (edge.source, edge.destination)

    def __gt__(self, edge: "Edge"):
        return (self.source, self.destination) > (edge.source, edge.destination)

    def __ge__(self, edge: "Edge"):
        return (self.source, self.destination) >= (edge.source, edge.destination)

    def get_neighbour(self, vertex):
        if vertex is self.source:
            return self.destination

        if vertex is self.destination:
            return self.source

        raise ValueError(f"Edge {self} is not adjacent to the vertex {vertex}")

    def reversed(self) -> "Edge":
        return Edge(self.destination, self.source)
