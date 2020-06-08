# -*- coding: utf-8 -*-
"""Structure of directed graphs"""
from abc import ABCMeta, abstractmethod

from .graph import Edge, Graph
from .graph_representation import GraphRepresentation
from .simple_graph import SimpleGraph


class DirectedGraph(Graph, metaclass=ABCMeta):
    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def reversed_copy(self):
        pass


class DirectedSimpleGraph(SimpleGraph, DirectedGraph):
    def __init__(self, properties=None, *, graph=None):
        super().__init__(properties=properties, graph=graph)

    @property
    def edges_count(self):
        return len(self._representation.edges)

    @property
    def edges(self):
        return sorted(self._representation.edges)

    def get_output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def get_input_degree(self, vertex):
        return len([edge for edges in self._representation.edges_set for edge in edges if
                    edge.destination is vertex])

    def add_edge(self, source, destination, edge_property):
        edge = Edge(source, destination, edge_property)

        self._representation.add_edge_to_source(edge)
        return edge

    def reverse(self):
        edges = self.edges
        self._representation = GraphRepresentation(vertices=self.vertices)

        for edge in edges:
            self._representation.add_edge_to_source(edge.reversed())

    def reversed_copy(self):
        reversed_graph = DirectedSimpleGraph(graph=self)

        for edge in self.edges:
            reversed_graph.add_edge(edge.destination, edge.source, edge.property)

        return reversed_graph
