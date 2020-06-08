# -*- coding: utf-8 -*-
"""Structure of simple graphs"""
from abc import ABCMeta, abstractmethod

from .graph import Graph
from .graph_representation import GraphRepresentation


class SimpleGraph(Graph, metaclass=ABCMeta):
    def __init__(self, properties=None, *, graph=None):
        if graph is not None:
            self._representation = GraphRepresentation(vertices=graph.vertices)
        else:
            self._representation = GraphRepresentation()

            if properties is not None:
                for prop in properties:
                    self.add_vertex(prop)

    @property
    def vertices_count(self):
        return len(self._representation)

    @property
    def vertices(self):
        return sorted(self._representation.vertices)

    def get_vertex(self, index):
        try:
            return [v for v in self._representation.vertices if v.index == index][0]
        except IndexError:
            raise IndexError(f"No vertex with index {index} in this graph")

    def get_neighbours(self, vertex):
        return set(edge.get_neighbour(vertex)
                   for edge in self._representation.get_adjacent_edges(vertex))

    def get_adjacent_edges(self, vertex):
        self._representation.get_adjacent_edges(vertex)

    def get_edge(self, source, destination):
        try:
            return [edge for edge in self._representation.get_adjacent_edges(source)
                    if edge.get_neighbour(source) is destination][0]
        except IndexError:
            return None

    def add_vertex(self, vertex_property):
        """Adds a new vertex with given property to this graph.

         :param vertex_property: a vertex property
         :return the new vertex"""
        return self._representation.add_vertex(vertex_property)

    @abstractmethod
    def add_edge(self, source, destination, edge_property):
        """Adds a new edge with given properties to this graph.

        :param source: a source vertex
        :param destination: a destination vertex
        :param edge_property: an edge property
        :return: the new edge"""
        pass
