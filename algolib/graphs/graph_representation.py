# -*- coding: utf-8 -*-
from graphs.graph import Vertex


class GraphRepresentation:
    def __init__(self, vertices=None):
        if vertices is not None:
            self._graphDict = {v: set() for v in vertices}
        else:
            self._graphDict = {}

    def __len__(self):
        return len(self._graphDict)

    @property
    def vertices(self):
        return self._graphDict.keys()

    @property
    def edges(self):
        result = []

        for edges_set in self._graphDict.values():
            result += edges_set

        return result

    @property
    def edges_set(self):
        return self._graphDict.values()

    def get_adjacent_edges(self, vertex):
        self._validate_vertex(vertex)
        return self._graphDict[vertex]

    def add_vertex(self, vertex_property):
        vertex = Vertex(len(self._graphDict), vertex_property)

        self._graphDict[vertex] = set()
        return vertex

    def add_edge_to_source(self, edge):
        self._validate_edge(edge)
        self._graphDict[edge.source].add(edge)

    def add_edge_to_destination(self, edge):
        self._validate_edge(edge)
        self._graphDict[edge.destination].add(edge)

    def _validate_vertex(self, vertex):
        if all(vertex is not v for v in self._graphDict.keys()):
            raise ValueError("Vertex object does not belong to this graph")

    def _validate_edge(self, edge):
        if all(v is not edge.source for v in self._graphDict.keys()) \
                and all(v is not edge.destination for v in self._graphDict.keys()):
            raise ValueError("Edge source or destination does not belong to this graph")
