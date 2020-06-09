# -*- coding: utf-8 -*-
"""Structure of undirected graphs"""
from abc import ABCMeta

from .graph import Edge, Graph
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

    def get_output_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def get_input_degree(self, vertex):
        return len(self._representation.get_adjacent_edges(vertex))

    def add_edge(self, source, destination, edge_property=None):
        existing_edge = self.get_edge(source, destination)

        if existing_edge is not None:
            return existing_edge

        new_edge = Edge(source, destination)
        self._representation.add_edge_to_source(new_edge)
        self._representation.add_edge_to_destination(new_edge)
        self._representation[new_edge] = edge_property
        return new_edge
