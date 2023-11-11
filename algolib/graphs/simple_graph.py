# -*- coding: utf-8 -*-
"""Structure of simple graph"""
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Optional, Union

from .edge import Edge
from .graph import Graph
from .vertex import Vertex


class _GraphRepresentation:
    def __init__(self, vertex_ids=None):
        self._properties = {}

        if vertex_ids is not None:
            self._graph_dict = {Vertex(vertex_id): set() for vertex_id in vertex_ids}
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

    def get_vertex(self, vertex_id):
        try:
            return next(v for v in self._graph_dict.keys() if v.id == vertex_id)
        except StopIteration:
            raise KeyError(f"Vertex not found : {vertex_id}") from None

    def get_edge(self, source_id, destination_id):
        try:
            source, edges = next(
                (v, edges) for v, edges in self._graph_dict.items() if v.id == source_id)
            return next(edge for edge in edges if edge.get_neighbour(source).id == destination_id)
        except StopIteration:
            raise KeyError(f"Edge not found: {source_id}, {destination_id}") from None

    def get_adjacent_edges(self, vertex):
        self._validate(vertex)
        return self._graph_dict[vertex]

    def get_property(self, item):
        self._validate(item, existing_edge=True)
        return self._properties.get(item, None)

    def set_property(self, item, value):
        self._validate(item, existing_edge=True)
        self._properties[item] = value

    def del_property(self, item):
        self._validate(item, existing_edge=True)
        del self._properties[item]

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
    def __init__(self, vertex_ids: Optional[Iterable[Any]]):
        self._representation = _GraphRepresentation(vertex_ids)
        self._properties = self._GraphPropertiesImpl(self)

    @property
    def properties(self):
        return self._properties

    @property
    def vertices_count(self):
        return len(self._representation)

    @property
    def vertices(self):
        return self._representation.vertices

    def get_vertex(self, vertex_id):
        return self._representation.get_vertex(vertex_id)

    def get_edge(self, source, destination):
        return self._representation.get_edge(source.id, destination.id) \
            if isinstance(source, Vertex) and isinstance(destination, Vertex) else \
            self._representation.get_edge(source, destination)

    def adjacent_edges(self, vertex: Vertex):
        return self._representation.get_adjacent_edges(vertex)

    def neighbours(self, vertex: Vertex):
        return set(edge.get_neighbour(vertex)
                   for edge in self._representation.get_adjacent_edges(vertex))

    def add_vertex(self, vertex: Union[Vertex, Any], property_: Any = None) -> Vertex:
        """Adds new vertex with given property to this graph.

        :param vertex: the new vertex or its identifier
        :param property_: the vertex property
        :return: the created vertex
        :raise ValueError: if the vertex already exists"""
        the_vertex = vertex if isinstance(vertex, Vertex) else Vertex(vertex)
        was_added = self._representation.add_vertex(the_vertex)

        if was_added:
            if property_ is not None:
                self._representation.set_property(the_vertex, property_)

            return the_vertex

        raise ValueError(f"Vertex {the_vertex} already exists")

    def add_edge_between(self, source: Vertex, destination: Vertex, property_: Any = None):
        """Adds new edge between given vertices with given property to this graph.

        :param source: the source vertex
        :param destination: the destination vertex
        :param property_: the edge property
        :return: the created edge
        :raise ValueError: if the edge already exists"""
        return self.add_edge(Edge(source, destination), property_)

    @abstractmethod
    def add_edge(self, edge: Edge, property_: Any = None):
        """Adds new edge with given property to this graph.

        :param edge: the new edge
        :param property_: the edge property
        :return: the created edge
        :raise ValueError: if the edge already exists"""

    class _GraphPropertiesImpl(Graph.GraphProperties):
        def __init__(self, graph: "SimpleGraph"):
            self._graph = graph

        def __getitem__(self, item: Union["Vertex", "Edge"]) -> Any:
            return self._graph._representation.get_property(item)

        def __setitem__(self, item: Union["Vertex", "Edge"], property_: Any):
            self._graph._representation.set_property(item, property_)

        def __delitem__(self, item: Union["Vertex", "Edge"]):
            self._graph._representation.del_property(item)
