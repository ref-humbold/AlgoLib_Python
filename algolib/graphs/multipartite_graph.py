# -*- coding: utf-8 -*-
"""Structure of multipartite graph"""
from .graph import Edge
from .undirected_graph import UndirectedGraph, UndirectedSimpleGraph


class GraphPartitionError(BaseException):
    pass


class MultipartiteGraph(UndirectedGraph):
    def __init__(self, groups_count, vertices=None):
        super().__init__()

        if groups_count < 0:
            raise ValueError("Number of groups cannot be negative")

        self._graph = UndirectedSimpleGraph()
        self._groups_count = groups_count
        self._vertex_group_dict = {}

        if vertices is not None:
            if len(vertices) > groups_count:
                raise GraphPartitionError(f"Cannot add vertices to group {len(vertices)}, "
                                          f"graph contains only {self._groups_count} groups")

            i = 0

            for group_vertices in vertices:
                for vertex in group_vertices:
                    self.add_vertex(i, vertex)

                i += 1

    @property
    def groups_count(self):
        return self._groups_count

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

    def __getitem__(self, item):
        return self._graph[item]

    def __setitem__(self, item, value):
        self._graph[item] = value

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

    def vertices_from_group(self, group_number):
        self._validate_group(group_number)
        return (item[0] for item in self._vertex_group_dict.items() if item[1] == group_number)

    def add_vertex(self, group_number, vertex, vertex_property=None):
        self._validate_group(group_number)

        was_added = self._graph.add_vertex(vertex, vertex_property)

        if was_added:
            self._vertex_group_dict[vertex] = group_number

        return was_added

    def add_edge_between(self, source, destination, edge_property=None):
        return self.add_edge(Edge(source, destination), edge_property)

    def add_edge(self, edge, edge_property=None):
        if self._are_in_same_group(edge.source, edge.destination):
            raise GraphPartitionError("Cannot create an edge between vertices in the same group")

        return self._graph.add_edge(edge, edge_property)

    def _are_in_same_group(self, vertex1, vertex2):
        return self._vertex_group_dict[vertex1] == self._vertex_group_dict[vertex2]

    def _validate_group(self, group_number):
        if group_number < 0 or group_number >= self._groups_count:
            raise IndexError(f"Invalid group number {group_number}, "
                             f"graph contains only {self._groups_count} groups")
