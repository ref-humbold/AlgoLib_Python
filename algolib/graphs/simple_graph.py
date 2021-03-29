# -*- coding: utf-8 -*-
"""Structure of simple graph"""
from abc import ABCMeta, abstractmethod

from .graph import Edge, Graph


class _GraphRepresentation:
    def __init__(self, vertices=None):
        self._properties = {}

        if vertices is not None:
            self._graph_dict = {v: set() for v in vertices}
        else:
            self._graph_dict = {}

    @property
    def vertices(self):
        return self._graph_dict.keys()

    @property
    def edges(self):
        result = []

        for edges_set in self._graph_dict.values():
            result += edges_set

        return result

    @property
    def edges_set(self):
        return self._graph_dict.values()

    def __len__(self):
        return len(self._graph_dict)

    def __getitem__(self, item):
        self._validate(item, existing_edge=True)
        return self._properties.get(item, None)

    def __setitem__(self, item, value):
        self._validate(item, existing_edge=True)

        if value is not None:
            self._properties[item] = value
        elif item in self._properties:
            del self._properties[item]

    def get_adjacent_edges(self, vertex):
        self._validate(vertex)
        return self._graph_dict[vertex]

    def add_vertex(self, vertex):
        if vertex in self._graph_dict:
            return False

        self._graph_dict[vertex] = set()
        return True

    def add_edge_to_source(self, edge):
        self._validate(edge, existing_edge=False)
        self._graph_dict[edge.source].add(edge)

    def add_edge_to_destination(self, edge):
        self._validate(edge, existing_edge=False)
        self._graph_dict[edge.destination].add(edge)

    def _validate(self, item, *, existing_edge=None):
        if isinstance(item, Edge):
            if item.source not in self._graph_dict or item.destination not in self._graph_dict:
                raise ValueError(f"Edge {item} does not belong to the graph")

            if existing_edge and item not in self._graph_dict[item.source] \
                    and item not in self._graph_dict[item.destination]:
                raise ValueError(f"Edge {item} does not belong to the graph")

        elif item not in self._graph_dict:
            raise ValueError(f"Vertex {item} does not belong to the graph")


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

    def adjacent_edges(self, vertex):
        return self._representation.get_adjacent_edges(vertex)

    def neighbours(self, vertex):
        return set(edge.get_neighbour(vertex)
                   for edge in self._representation.get_adjacent_edges(vertex))

    def get_edge(self, source, destination):
        try:
            return [edge for edge in self._representation.get_adjacent_edges(source)
                    if edge.get_neighbour(source) == destination][0]
        except IndexError:
            raise KeyError(f"No edge between the vertices {source} and {destination}")

    def add_vertex(self, vertex, vertex_property=None):
        """Adds a new vertex with given property to the graph.

         :param vertex: a new vertex
         :param vertex_property: vertex property
         :return: ``true`` if the vertex was added, otherwise ``false``"""
        was_added = self._representation.add_vertex(vertex)

        if was_added:
            self[vertex] = vertex_property

        return was_added

    def add_edge_between(self, source, destination, edge_property=None):
        """Adds a new edge with given property to the graph.

        :param source: a source vertex
        :param destination: a destination vertex
        :param edge_property: edge property
        :return: the new edge if added, or the existing edge"""
        return self.add_edge(Edge(source, destination), edge_property)

    @abstractmethod
    def add_edge(self, edge, edge_property=None):
        """Adds a new edge with given property to the graph.

        :param edge: a new edge
        :param edge_property: edge property
        :return: the new edge if added, or the existing edge"""
        pass
