# -*- coding: utf-8 -*-
"""Structure of graph edge."""
from .vertex import Vertex


class Edge:
    def __init__(self, source: Vertex, destination: Vertex):
        self.source = source
        self.destination = destination

    def __hash__(self):
        return hash((self.source, self.destination))

    def __repr__(self):
        return f"Edge({self.source!r}, {self.destination!r})"

    def __str__(self):
        return f"Edge{{{self.source} -- {self.destination}}}"

    def __eq__(self, edge: "Edge"):
        return (self.source, self.destination) == (edge.source, edge.destination)

    def __ne__(self, edge: "Edge"):
        return (self.source, self.destination) != (edge.source, edge.destination)

    def __lt__(self, edge: "Edge"):
        return (self.source, self.destination) < (edge.source, edge.destination)

    def __le__(self, edge: "Edge"):
        return (self.source, self.destination) <= (edge.source, edge.destination)

    def __gt__(self, edge: "Edge"):
        return (self.source, self.destination) > (edge.source, edge.destination)

    def __ge__(self, edge: "Edge"):
        return (self.source, self.destination) >= (edge.source, edge.destination)

    def get_neighbour(self, vertex: Vertex):
        """Gets the neighbour of given adjacent vertex.

        :param vertex: the vertex adjacent to this edge
        :return: the neighbour of the vertex along this edge
        :raise ValueError: if the vertex is not adjacent to this edge"""
        if vertex == self.source:
            return self.destination

        if vertex == self.destination:
            return self.source

        raise ValueError(f"Edge {self} is not adjacent to the vertex {vertex}")

    def reversed(self) -> "Edge":
        """Gets the reversed copy of this edge.

        :return: the edge with reversed direction"""
        return Edge(self.destination, self.source)
