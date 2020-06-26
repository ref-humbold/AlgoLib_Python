# -*- coding: utf-8 -*-
from .graph import Edge


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
