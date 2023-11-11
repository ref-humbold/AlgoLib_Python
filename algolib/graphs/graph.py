# -*- coding: utf-8 -*-
"""Structure of basic graph"""
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Union

from .edge import Edge
from .vertex import Vertex


class Graph(metaclass=ABCMeta):
    @property
    @abstractmethod
    def properties(self) -> "GraphProperties":
        pass

    @property
    @abstractmethod
    def vertices_count(self) -> int:
        """Gets the number of vertices in this graph.

        :return: the number of vertices"""

    @property
    @abstractmethod
    def edges_count(self) -> int:
        """Gets the number of edges in this graph.

        :return: the number of edges"""

    @property
    @abstractmethod
    def vertices(self) -> Iterable[Vertex]:
        """Gets all vertices in this graph.

        :return: all vertices"""

    @property
    @abstractmethod
    def edges(self) -> Iterable[Edge]:
        """Gets all edges in this graph.

        :return: all edges"""

    @abstractmethod
    def get_vertex(self, vertex_id: Any) -> Vertex:
        """Gets the vertex from this graph with given identifier.

        :param vertex_id: the vertex identifier
        :return: the vertex with the identifier
        :raise KeyError: if no such vertex exists"""

    @abstractmethod
    def get_edge(self, source: Union[Vertex, Any], destination: Union[Vertex, Any]) -> Edge:
        """Gets the edge between given vertices or its identifiers.

        :param source: the source vertex or its identifier
        :param destination: the destination vertex or its identifier
        :return: the edge between the vertices
        :raise KeyError: if no such edge exists"""

    @abstractmethod
    def neighbours(self, vertex: Vertex) -> Iterable[Vertex]:
        """Gets the neighbours of given vertex.

        :param vertex: the vertex from this graph
        :return: the neighbouring vertices"""

    @abstractmethod
    def adjacent_edges(self, vertex: Vertex) -> Iterable[Edge]:
        """Gets the adjacent edges of given vertex.

        :param vertex: the vertex from the graph
        :return: the edges adjacent to the vertex"""

    @abstractmethod
    def output_degree(self, vertex: Vertex) -> int:
        """Gets the output degree of given vertex.

        :param vertex: the vertex from the graph
        :return: the output degree of the vertex"""

    @abstractmethod
    def input_degree(self, vertex: Vertex) -> int:
        """Gets the input degree of given vertex.

        :param vertex: the vertex from the graph
        :return: the input degree of the vertex"""

    class GraphProperties(metaclass=ABCMeta):
        @abstractmethod
        def __getitem__(self, item: Union[Vertex, Edge]):
            """Gets the property of given vertex or edge.

            :param item: the vertex or the edge from this graph
            :return: the property of the vertex or the edge, or ``None`` if no property exists"""

        @abstractmethod
        def __setitem__(self, item: Union[Vertex, Edge], property_: Any):
            """Sets the property for given vertex or edge.

            :param item: the vertex or the edge from this graph
            :param property_: the new property"""

        @abstractmethod
        def __delitem__(self, item: Union[Vertex, Edge]):
            """Deletes property for given vertex or edge.
            :param item: the vertex or the edge from this graph"""
