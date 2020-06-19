# -*- coding: utf-8 -*-
"""Structure of simple graph"""
from abc import ABCMeta, abstractmethod

from algolib.graphs.graph import Edge, Graph
from algolib.graphs.graph_representation import _GraphRepresentation


class SimpleGraph(Graph, metaclass=ABCMeta):
    def __init__(self, vertices=None):
        self._representation = _GraphRepresentation(vertices)

    @property
    def vertices_count(self):
        return len(self._representation)

    @property
    def vertices(self):
        return sorted(self._representation.vertices)

    def __getitem__(self, item):
        return self._representation[item]

    def __setitem__(self, item, value):
        self._representation[item] = value

    def get_adjacent_edges(self, vertex):
        return self._representation.get_adjacent_edges(vertex)

    def get_neighbours(self, vertex):
        return set(edge.get_neighbour(vertex)
                   for edge in self._representation.get_adjacent_edges(vertex))

    def get_edge(self, source, destination):
        try:
            return [edge for edge in self._representation.get_adjacent_edges(source)
                    if edge.get_neighbour(source) == destination][0]
        except IndexError:
            raise KeyError(f"No edge between the vertices {source} and {destination}")

    def add_vertex(self, vertex, vertex_property=None):
        """Adds a new vertex with given property to this graph.

         :param vertex: a new vertex
         :param vertex_property: vertex property
         :return: ``true`` if the vertex was added, otherwise ``false``"""
        was_added = self._representation.add_vertex(vertex)

        if was_added:
            self[vertex] = vertex_property

        return was_added

    def add_edge_between(self, source, destination, edge_property=None):
        """Adds a new edge with given property to this graph.

        :param source: a source vertex
        :param destination: a destination vertex
        :param edge_property: edge property
        :return: the new edge if added, or the existing edge"""
        return self.add_edge(Edge(source, destination), edge_property)

    @abstractmethod
    def add_edge(self, edge, edge_property=None):
        """Adds a new edge with given property to this graph.

        :param edge: a new edge
        :param edge_property: edge property
        :return: the new edge if added, or the existing edge"""
        pass
