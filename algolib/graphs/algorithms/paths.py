# -*- coding: utf-8 -*-
"""Algorithms for shortest paths"""
import math
import queue


class Paths:
    INFINITY = math.inf


def bellman_ford(graph, source):
    """Bellman-Ford algorithm.

    :param graph: a directed graph with weighted edges
    :param source: source vertex
    :return: dictionary of vertices' distances"""
    distances = {v: Paths.INFINITY for v in graph.vertices}
    distances[source] = 0.0

    for _ in range(graph.vertices_count - 1):
        for edge in graph.edges:
            distances[edge.destination] = min(distances[edge.destination],
                                              distances[edge.source] + graph[edge].weight)

    for edge in graph.edges:
        if distances[edge.source] < Paths.INFINITY \
                and distances[edge.source] + graph[edge].weight < distances[edge.destination]:
            raise ValueError("Graph contains a negative cycle")

    return distances


def dijkstra(graph, source):
    """Dijkstra algorithm.

    :param graph: a graph with weighted edges (weights are not negative)
    :param source: source vertex
    :return: dictionary of vertices' distances"""
    if any(graph[e].weight < 0.0 for e in graph.edges):
        raise ValueError("Graph contains an edge with negative weight")

    vertex_queue = queue.PriorityQueue()
    vertex_queue.put((0.0, source))
    visited = set()
    distances = {v: Paths.INFINITY for v in graph.vertices}
    distances[source] = 0.0

    while not vertex_queue.empty():
        vertex = vertex_queue.get()[1]

        if vertex not in visited:
            visited.add(vertex)

            for edge in graph.adjacent_edges(vertex):
                neighbour = edge.get_neighbour(vertex)

                if distances[vertex] + graph[edge].weight < distances[neighbour]:
                    distances[neighbour] = distances[vertex] + graph[edge].weight
                    vertex_queue.put((distances[neighbour], neighbour))

    return distances


def floyd_warshall(graph):
    """Floyd-Warshall algorithm.

    :param graph: a directed graph with weighted edges
    :return: map of distances between all pairs of vertices"""
    distances = {(v, u): 0.0 if v == u else Paths.INFINITY for v in graph.vertices
                 for u in graph.vertices}

    for edge in graph.edges:
        distances[(edge.source, edge.destination)] = graph[edge].weight

    for vertex0 in graph.vertices:
        for vertex1 in graph.vertices:
            for vertex2 in graph.vertices:
                distances[(vertex1, vertex2)] = \
                    min(distances[(vertex1, vertex2)],
                        distances[(vertex1, vertex0)] + distances[(vertex0, vertex2)])

    return distances
