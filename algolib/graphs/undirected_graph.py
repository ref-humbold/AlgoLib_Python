# -*- coding: utf-8 -*-
from abc import ABCMeta

from .graph import Edge, Graph
from .simple_graph import SimpleGraph


class UndirectedGraph(Graph, metaclass=ABCMeta):
    pass


class UndirectedSimpleGraph(SimpleGraph, UndirectedGraph):
    def __init__(self, properties=None, *, graph=None):
        super().__init__(properties=properties, graph=graph)

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

    def add_edge(self, source, destination, edge_property):
        new_source = min(source, destination)
        new_destination = max(source, destination)
        edge = Edge(new_source, new_destination, edge_property)

        self._representation.add_edge_to_source(edge)
        self._representation.add_edge_to_destination(edge)
        return edge
