# -*- coding: utf-8 -*-
"""Algorithms for minimal spanning tree."""
from queue import PriorityQueue

from algolib.structures.disjoint_sets import DisjointSets
from ..undirected_graph import UndirectedGraph, UndirectedSimpleGraph
from ..vertex import Vertex


def kruskal(graph: UndirectedGraph) -> UndirectedGraph:
    """Computes minimal spanning tree of given undirected graph using Kruskal algorithm.

    :param graph: the undirected weighted graph
    :return: the minimal spanning tree"""
    mst = UndirectedSimpleGraph([v.id for v in graph.vertices])
    edge_queue = PriorityQueue()
    vertex_sets = DisjointSets(graph.vertices)

    for edge in graph.edges:
        edge_queue.put((graph.properties[edge].weight, edge))

    while len(vertex_sets) > 1 and not edge_queue.empty():
        _, edge = edge_queue.get()

        if not vertex_sets.is_same_set(edge.source, edge.destination):
            mst.add_edge(edge, graph.properties[edge])
            vertex_sets.union_set(edge.source, edge.destination)

    return mst


def prim(graph: UndirectedGraph, source: Vertex) -> UndirectedGraph:
    """Computes minimal spanning tree of given undirected graph using Prim algorithm.

    :param graph: the undirected weighted graph.
    :param source: the starting vertex
    :return: the minimal spanning tree"""
    mst = UndirectedSimpleGraph([v.id for v in graph.vertices])
    visited = {source}
    edge_queue = PriorityQueue()

    for adjacent_edge in graph.adjacent_edges(source):
        neighbour = adjacent_edge.get_neighbour(source)

        if neighbour != source:
            edge_queue.put((graph.properties[adjacent_edge].weight, adjacent_edge, neighbour))

    while not edge_queue.empty():
        _, edge, vertex = edge_queue.get()

        if vertex not in visited:
            visited.add(vertex)
            mst.add_edge(edge, graph.properties[edge])

            for adjacent_edge in graph.adjacent_edges(vertex):
                neighbour = adjacent_edge.get_neighbour(vertex)

                if neighbour not in visited:
                    edge_queue.put(
                        (graph.properties[adjacent_edge].weight, adjacent_edge, neighbour))

    return mst
