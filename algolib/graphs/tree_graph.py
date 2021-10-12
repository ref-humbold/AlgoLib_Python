# -*- coding: utf-8 -*-
"""Structure of tree graph"""
from typing import Any, Union

from .graph import Edge, Vertex
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class TreeGraph(UndirectedGraph):
    def __init__(self, vertex_id):
        super().__init__()
        self._graph = UndirectedSimpleGraph([vertex_id])

    @property
    def properties(self):
        return self._graph.properties

    @property
    def vertices_count(self):
        return self._graph.vertices_count

    @property
    def edges_count(self):
        return self._graph.edges_count

    @property
    def vertices(self):
        return self._graph.vertices

    @property
    def edges(self):
        return self._graph.edges

    def get_vertex(self, vertex_id):
        return self._graph.get_vertex(vertex_id)

    def get_edge(self, source, destination):
        return self._graph.get_edge(source, destination)

    def adjacent_edges(self, vertex):
        return self._graph.adjacent_edges(vertex)

    def neighbours(self, vertex):
        return self._graph.neighbours(vertex)

    def output_degree(self, vertex):
        return self._graph.output_degree(vertex)

    def input_degree(self, vertex):
        return self._graph.input_degree(vertex)

    def as_directed(self):
        return self._graph.as_directed()

    def add_vertex(self, vertex: Union[Vertex, Any], neighbour: Vertex, vertex_property: Any = None,
                   edge_property: Any = None) -> Edge:
        """Adds new vertex to this graph and creates an edge from the new vertex to
        an existing vertex.

        :param vertex: new vertex ot its identifier
        :param neighbour: existing vertex from the graph
        :param vertex_property: vertex property
        :param edge_property: edge property
        :return: new edge between the new vertex and the existing vertex
        :raise ValueError: if the vertex exists"""
        new_vertex = self._graph.add_vertex(vertex, vertex_property)
        return self._graph.add_edge_between(new_vertex, neighbour, edge_property)
