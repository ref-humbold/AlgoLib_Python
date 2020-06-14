# -*- coding: utf-8 -*-
"""Structure of undirected graphs"""
from abc import ABCMeta

from algolib.graphs.directed_graph import DirectedSimpleGraph
from algolib.graphs.graph import Graph
from algolib.graphs.simple_graph import SimpleGraph


class UndirectedGraph(Graph, metaclass=ABCMeta):
    pass


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, vertices=None):
        super().__init__(vertices)

    @property
    def edges_count(self):
        return len(set(self._representation.edges))

    @property
    def edges(self):
        return sorted(set(self._representation.edges))

    def get_output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def get_input_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def add_edge(self, edge, edge_property=None):
        existing_edge = self.get_edge(edge.source, edge.destination)

        if existing_edge is not None:
            return existing_edge

        self._representation.add_edge_to_source(edge)
        self._representation.add_edge_to_destination(edge)
        self._representation[edge] = edge_property
        return edge

    def as_directed(self):
        directed_simple_graph = DirectedSimpleGraph(self.vertices)

        for vertex in self.vertices:
            directed_simple_graph[vertex] = self[vertex]

        for edge in self.edges:
            directed_simple_graph.add_edge(edge, self[edge])
            directed_simple_graph.add_edge(edge.reversed(), self[edge])

        return directed_simple_graph
