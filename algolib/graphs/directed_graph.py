# -*- coding: utf-8 -*-
"""Structure of directed graph"""
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Optional

from .graph import Graph
from .simple_graph import SimpleGraph, _GraphRepresentation


class DirectedGraph(Graph, metaclass=ABCMeta):
    @abstractmethod
    def reverse(self):
        """Reverses directions of edges in the graph."""

    @abstractmethod
    def reversed_copy(self) -> "DirectedGraph":
        """:return: copy of this graph with reversed directions of edges"""


class DirectedSimpleGraph(SimpleGraph, DirectedGraph):
    def __init__(self, vertex_ids: Optional[Iterable[Any]] = None):
        super().__init__(vertex_ids)

    @property
    def edges_count(self):
        return len(self._representation.edges)

    @property
    def edges(self):
        return iter(self._representation.edges)

    def output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def input_degree(self, vertex):
        return len([edge for edges in self._representation.edges_set for edge in edges if
                    edge.destination == vertex])

    def add_edge(self, edge, property_=None):
        try:
            existing_edge = self.get_edge(edge.source, edge.destination)
        except KeyError:
            self._representation.add_edge_to_source(edge)

            if property_ is not None:
                self._representation.set_property(edge, property_)

            return edge
        else:
            raise ValueError(f"Edge {existing_edge} already exists")

    def reverse(self):
        new_representation = _GraphRepresentation((v.id for v in self.vertices))

        for vertex in self.vertices:
            new_representation.set_property(vertex, self._representation.get_property(vertex))

        for edge in self.edges:
            new_edge = edge.reversed()
            new_representation.add_edge_to_source(new_edge)
            new_representation.set_property(new_edge, self._representation.get_property(edge))

        self._representation = new_representation

    def reversed_copy(self) -> "DirectedSimpleGraph":
        reversed_graph = DirectedSimpleGraph((v.id for v in self.vertices))

        for vertex in self.vertices:
            reversed_graph.properties[vertex] = self.properties[vertex]

        for edge in self.edges:
            reversed_graph.add_edge(edge.reversed(), self.properties[edge])

        return reversed_graph
