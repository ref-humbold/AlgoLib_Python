# -*- coding: utf-8 -*-
"""Structure of directed graphs"""
from abc import ABCMeta, abstractmethod

from algolib.graphs.graph import Edge, Graph
from algolib.graphs.graph_representation import GraphRepresentation
from algolib.graphs.simple_graph import SimpleGraph


class DirectedGraph(Graph, metaclass=ABCMeta):
    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def reversed_copy(self):
        pass


class DirectedSimpleGraph(SimpleGraph, DirectedGraph):
    def __init__(self, vertices=None):
        super().__init__(vertices)

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

    def add_edge(self, source, destination, edge_property=None):
        existing_edge = self.get_edge(source, destination)

        if existing_edge is not None:
            return existing_edge

        new_edge = Edge(source, destination)
        self._representation.add_edge_to_source(new_edge)
        self._representation[new_edge] = edge_property
        return new_edge

    def reverse(self):
        new_representation = GraphRepresentation(self.vertices)

        for vertex in self.vertices:
            new_representation[vertex] = self._representation[vertex]

        for edge in self.edges:
            new_edge = edge.reversed()
            new_representation.add_edge_to_source(new_edge)
            new_representation[new_edge] = self._representation[edge]

        self._representation = new_representation

    def reversed_copy(self):
        reversed_graph = DirectedSimpleGraph(self.vertices)

        for vertex in self.vertices:
            reversed_graph[vertex] = self._representation[vertex]

        for edge in self.edges:
            reversed_graph.add_edge(edge.destination, edge.source, self._representation[edge])

        return reversed_graph
