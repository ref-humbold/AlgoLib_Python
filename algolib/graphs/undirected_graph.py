# -*- coding: utf-8 -*-
"""Structure of undirected graph"""
from abc import ABCMeta

from .directed_graph import DirectedSimpleGraph
from .graph import Graph
from .simple_graph import SimpleGraph


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

    def output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def input_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def add_edge(self, edge, edge_property=None):
        try:
            existing_edge = self.get_edge(edge.source, edge.destination)
        except KeyError:
            self._representation.add_edge_to_source(edge)
            self._representation.add_edge_to_destination(edge)
            self._representation[edge] = edge_property
            return edge
        else:
            return existing_edge

    def as_directed(self):
        graph = DirectedSimpleGraph(self.vertices)

        for vertex in self.vertices:
            graph[vertex] = self[vertex]

        for edge in self.edges:
            graph.add_edge(edge, self[edge])
            graph.add_edge(edge.reversed(), self[edge])

        return graph
