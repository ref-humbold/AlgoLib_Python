# -*- coding: utf-8 -*-
"""Structure of tree graph"""
from typing import Any, Union

from .edge import Edge
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph
from .vertex import Vertex


class TreeGraph(UndirectedGraph):
    def __init__(self, vertex_id: Any):
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

    def add_vertex(self,
                   vertex: Union[Vertex, Any],
                   neighbour: Vertex,
                   vertex_property: Any = None,
                   edge_property: Any = None) -> Edge:
        """Adds new vertex to this graph and creates an edge to given existing vertex.

        :param vertex: the new vertex ot its identifier
        :param neighbour: the existing vertex
        :param vertex_property: the vertex property
        :param edge_property: the edge property
        :return: the created edge between the vertices
        :raise ValueError: if the vertex already exists"""
        new_vertex = self._graph.add_vertex(vertex, vertex_property)
        return self._graph.add_edge_between(new_vertex, neighbour, edge_property)
