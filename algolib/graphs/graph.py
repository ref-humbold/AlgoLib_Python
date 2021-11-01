# -*- coding: utf-8 -*-
"""Structure of basic graph"""
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Union


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
    def get_vertex(self, vertex_id: Any) -> "Vertex":
        """:param vertex_id: vertex identifier
        :return: vertex with the identifier
        :raise KeyError: if no such vertex"""

    @abstractmethod
    def get_edge(self, source: Union["Vertex", Any], destination: Union["Vertex", Any]) -> "Edge":
        """:param source: source vertex or its identifier
        :param destination: destination vertex or its identifier
        :return: edge between the vertices
        :raise KeyError: if no such edge"""

    @abstractmethod
    def adjacent_edges(self, vertex: "Vertex") -> Iterable["Edge"]:
        """:param vertex: vertex from this graph
        :return: iterable of edges adjacent to the vertex"""

    @abstractmethod
    def neighbours(self, vertex: "Vertex") -> Iterable["Vertex"]:
        """:param vertex: a vertex from the graph
        :return: iterable of neighbouring vertices"""

    @abstractmethod
    def output_degree(self, vertex: "Vertex") -> int:
        """:param vertex: vertex from this graph
        :return: output degree of the vertex"""

    @abstractmethod
    def input_degree(self, vertex: "Vertex") -> int:
        """:param vertex: vertex from this graph
        :return: input degree of the vertex"""

    class GraphProperties(metaclass=ABCMeta):
        @abstractmethod
        def __getitem__(self, item: Union["Vertex", "Edge"]):
            """Extracts property of given vertex or edge.
            :param item: vertex or edge from this graph
            :return: property of the vertex or the edge, or ``None`` if no property"""

        @abstractmethod
        def __setitem__(self, item: Union["Vertex", "Edge"], property_: Any):
            """Assigns new property for given vertex or edge.
            :param item: vertex or edge from this graph
            :param property_: new property of given vertex or edge"""

        @abstractmethod
        def __delitem__(self, item: Union["Vertex", "Edge"]):
            """Removes property for given vertex or edge.
            :param item: vertex or edge from this graph"""


class Vertex:
    def __init__(self, id_: Any):
        self.id = id_

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Vertex({self.id!r})"

    def __str__(self):
        return f"Vertex({self.id})"

    def __eq__(self, vertex: "Vertex"):
        return self.id == vertex.id

    def __ne__(self, vertex: "Vertex"):
        return self.id != vertex.id

    def __lt__(self, vertex: "Vertex"):
        return self.id < vertex.id

    def __le__(self, vertex: "Vertex"):
        return self.id <= vertex.id

    def __gt__(self, vertex: "Vertex"):
        return self.id > vertex.id

    def __ge__(self, vertex: "Vertex"):
        return self.id >= vertex.id


class Edge:
    def __init__(self, source: Vertex, destination: Vertex):
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

    def get_neighbour(self, vertex: Vertex):
        """:param vertex: vertex adjacent to this edge
        :return: neighbour of the vertex along this edge
        :raise ValueError: if the vertex is not adjacent to this edge"""
        if vertex == self.source:
            return self.destination

        if vertex == self.destination:
            return self.source

        raise ValueError(f"Edge {self} is not adjacent to the vertex {vertex}")

    def reversed(self) -> "Edge":
        """:return: edge with reversed direction"""
        return Edge(self.destination, self.source)
