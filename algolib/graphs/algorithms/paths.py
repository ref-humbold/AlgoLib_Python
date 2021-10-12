# -*- coding: utf-8 -*-
"""Algorithms for shortest paths"""
from collections import deque
import math
from typing import Dict, Tuple

from ..directed_graph import DirectedGraph
from ..graph import Graph, Vertex


class Paths:
    INFINITY = math.inf


def bellman_ford(graph: DirectedGraph, source: Vertex) -> Dict[Vertex, float]:
    """Bellman-Ford algorithm.

    :param graph: a directed graph with weighted edges
    :param source: source vertex
    :return: dictionary of vertices' distances"""
    distances = {v: Paths.INFINITY for v in graph.vertices}
    distances[source] = 0.0

    for _ in range(graph.vertices_count - 1):
        for edge in graph.edges:
            distances[edge.destination] = \
                min(distances[edge.destination],
                    distances[edge.source] + graph.properties[edge].weight)

    for edge in graph.edges:
        if distances[edge.source] < Paths.INFINITY \
                and distances[edge.source] + graph.properties[edge].weight \
                < distances[edge.destination]:
            raise ValueError("Graph contains a negative cycle")

    return distances


def dijkstra(graph: Graph, source: Vertex) -> Dict[Vertex, float]:
    """Dijkstra algorithm.

    :param graph: a graph with weighted edges (weights are not negative)
    :param source: source vertex
    :return: dictionary of vertices' distances"""
    if any(graph.properties[edge].weight < 0.0 for edge in graph.edges):
        raise ValueError("Graph contains an edge with negative weight")

    vertex_queue = deque()
    vertex_queue.append((0.0, source))
    visited = set()
    distances = {v: Paths.INFINITY for v in graph.vertices}
    distances[source] = 0.0

    while len(vertex_queue) > 0:
        vertex = vertex_queue.popleft()[1]

        if vertex not in visited:
            visited.add(vertex)

            for edge in graph.adjacent_edges(vertex):
                neighbour = edge.get_neighbour(vertex)

                if distances[vertex] + graph.properties[edge].weight < distances[neighbour]:
                    distances[neighbour] = distances[vertex] + graph.properties[edge].weight
                    vertex_queue.append((distances[neighbour], neighbour))

    return distances


def floyd_warshall(graph: DirectedGraph) -> Dict[Tuple[Vertex, Vertex], float]:
    """Floyd-Warshall algorithm.

    :param graph: a directed graph with weighted edges
    :return: dictionary of distances between all pairs of vertices"""
    distances = {(v, u): 0.0 if v == u else Paths.INFINITY for v in graph.vertices
                 for u in graph.vertices}

    for edge in graph.edges:
        distances[(edge.source, edge.destination)] = graph.properties[edge].weight

    for vertex0 in graph.vertices:
        for vertex1 in graph.vertices:
            for vertex2 in graph.vertices:
                distances[(vertex1, vertex2)] = \
                    min(distances[(vertex1, vertex2)],
                        distances[(vertex1, vertex0)] + distances[(vertex0, vertex2)])

    return distances
