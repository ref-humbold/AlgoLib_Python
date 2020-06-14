# -*- coding: utf-8 -*-
"""Algorithms for minimal spanning tree"""
import queue

from algolib.graphs import UndirectedSimpleGraph
from algolib.structures.disjoint_sets import DisjointSets


def kruskal(graph):
    """Kruskal algorithm.

    :param graph: an undirected graph with weighted edges
    :return: the minimal spanning tree"""
    mst = UndirectedSimpleGraph(graph.vertices)
    edge_queue = queue.PriorityQueue()
    vertex_sets = DisjointSets(graph.vertices)

    for edge in graph.edges:
        edge_queue.put((graph[edge].weight, edge))

    while len(vertex_sets) > 1 and not edge_queue.empty():
        weight, edge = edge_queue.get()

        if not vertex_sets.is_same_set(edge.source, edge.destination):
            mst.add_edge(edge, graph[edge])
            vertex_sets.union_set(edge.source, edge.destination)

    return mst


def prim(graph, source):
    """Prim algorithm.

    :param graph: an undirected graph with weighted edges
    :param source: source vertex
    :return: the minimal spanning tree"""
    mst = UndirectedSimpleGraph(graph.vertices)
    visited = {source}
    edge_queue = queue.PriorityQueue()

    for adjacent_edge in graph.get_adjacent_edges(source):
        neighbour = adjacent_edge.get_neighbour(source)

        if neighbour != source:
            edge_queue.put((graph[adjacent_edge].weight, adjacent_edge, neighbour))

    while not edge_queue.empty():
        _, edge, vertex = edge_queue.get()

        if vertex not in visited:
            visited.add(vertex)
            mst.add_edge(edge, graph[edge])

            for adjacent_edge in graph.get_adjacent_edges(vertex):
                neighbour = adjacent_edge.get_neighbour(vertex)

                if neighbour not in visited:
                    edge_queue.put((graph[adjacent_edge].weight, adjacent_edge, neighbour))

    return mst
