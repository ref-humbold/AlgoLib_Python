# -*- coding: utf-8 -*-
"""Structure of tree graph"""
from algolib.graphs.undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class TreeGraph(UndirectedGraph):
    def __init__(self, vertex):
        super().__init__()
        self._graph = UndirectedSimpleGraph([vertex])

    def __getitem__(self, item):
        return self._graph[item]

    def __setitem__(self, item, value):
        self._graph[item] = value

    @property
    def vertices_count(self):
        return self._graph.vertices_count

    @property
    def vertices(self):
        return self._graph.vertices

    @property
    def edges_count(self):
        return self._graph.edges_count

    @property
    def edges(self):
        return self._graph.edges

    def get_edge(self, source, destination):
        return self._graph.get_edge(source, destination)

    def get_adjacent_edges(self, vertex):
        return self._graph.get_adjacent_edges(vertex)

    def get_neighbours(self, vertex):
        return self._graph.get_neighbours(vertex)

    def get_output_degree(self, vertex):
        return self._graph.get_output_degree(vertex)

    def get_input_degree(self, vertex):
        return self._graph.get_input_degree(vertex)

    def add_vertex(self, vertex, neighbour, vertex_property=None, edge_property=None):
        was_added = self._graph.add_vertex(vertex, vertex_property)
        return self._graph.add_edge_between(vertex, neighbour, edge_property) if was_added else None

    def as_directed(self):
        return self._graph.as_directed()
