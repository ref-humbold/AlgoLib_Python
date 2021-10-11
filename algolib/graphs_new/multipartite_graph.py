# -*- coding: utf-8 -*-
"""Structure of multipartite graph"""
from typing import Any, Iterable, Union

from .graph import Edge, Vertex
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class GraphPartitionError(BaseException):
    pass


class MultipartiteGraph(UndirectedGraph):
    def __init__(self, groups_count, vertex_ids=None):
        super().__init__()

        if groups_count < 0:
            raise ValueError("Number of groups cannot be negative")

        self._graph = UndirectedSimpleGraph()
        self._vertex_group_dict = {}
        self.groups_count = groups_count

        if vertex_ids is not None:
            if len(vertex_ids) > groups_count:
                raise GraphPartitionError(f"Cannot add vertices to group {len(vertex_ids)}, "
                                          f"graph contains only {self.groups_count} groups")

            for i, group_vertices in enumerate(vertex_ids):
                for vertex_id in group_vertices:
                    self.add_vertex(i, vertex_id)

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

    def vertices_from_group(self, group_number: int) -> Iterable[Vertex]:
        self._validate_group(group_number)
        return (vertex for vertex, group in self._vertex_group_dict.items()
                if group == group_number)

    def add_vertex(self, group_number: int, vertex: Union[Vertex, Any], property_: Any = None):
        self._validate_group(group_number)
        the_vertex = self._graph.add_vertex(vertex, property_)
        self._vertex_group_dict[the_vertex] = group_number
        return the_vertex

    def add_edge_between(self, source: Vertex, destination: Vertex, property_: Any = None):
        return self.add_edge(Edge(source, destination), property_)

    def add_edge(self, edge: Edge, property_: Any = None):
        if self._are_in_same_group(edge.source, edge.destination):
            raise GraphPartitionError("Cannot create an edge between vertices in the same group")

        return self._graph.add_edge(edge, property_)

    def _are_in_same_group(self, vertex1, vertex2):
        return self._vertex_group_dict[vertex1] == self._vertex_group_dict[vertex2]

    def _validate_group(self, group_number):
        if group_number < 0 or group_number >= self.groups_count:
            raise IndexError(f"Invalid group number {group_number}, "
                             f"graph contains only {self.groups_count} groups")
