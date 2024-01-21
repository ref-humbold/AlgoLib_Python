# -*- coding: utf-8 -*-
"""Structure of undirected graph."""
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Optional

from .directed_graph import DirectedGraph, DirectedSimpleGraph
from .graph import Graph
from .simple_graph import SimpleGraph


class UndirectedGraph(Graph, metaclass=ABCMeta):
    @abstractmethod
    def as_directed(self) -> DirectedGraph:
        """Converts this graph to the directed graph with the same vertices.

        :return: the directed copy of this graph"""


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, vertex_ids: Optional[Iterable[Any]] = None):
        super().__init__(vertex_ids)

    @property
    def edges_count(self):
        return len(set(self._representation.edges))

    @property
    def edges(self):
        return iter(set(self._representation.edges))

    def output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def input_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def add_edge(self, edge, property_=None):
        try:
            existing_edge = self.get_edge(edge.source, edge.destination)
        except KeyError:
            self._representation.add_edge_to_source(edge)
            self._representation.add_edge_to_destination(edge)

            if property_ is not None:
                self._representation.set_property(edge, property_)

            return edge
        else:
            raise ValueError(f"Edge {existing_edge} already exists")

    def as_directed(self) -> DirectedSimpleGraph:
        graph = DirectedSimpleGraph((v.id for v in self.vertices))

        for vertex in self.vertices:
            graph.properties[vertex] = self.properties[vertex]

        for edge in self.edges:
            graph.add_edge(edge, self.properties[edge])

            if edge.source != edge.destination:
                graph.add_edge(edge.reversed(), self.properties[edge])

        return graph
