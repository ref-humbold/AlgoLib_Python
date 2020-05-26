# -*- coding: utf-8 -*-
"""Algorithms for minimal spanning tree"""
import queue

from algolib.structures.disjoint_sets import DisjointSets


def kruskal(uwgraph):
    """Algorytm Kruskala wyliczający długość MST.

    :param uwgraph: graf nieskierowany ważony
    :return: długość minimalnego drzewa spinającego"""
    size_mst = 0.0
    components = uwgraph.vertices_number
    edge_queue = queue.PriorityQueue()
    vertex_sets = DisjointSets(uwgraph.get_vertices())

    for v, u, wg in uwgraph.get_weighted_edges():
        edge_queue.put((wg, v, u))

    while components > 1 and not edge_queue.empty():
        edge_weight, edge_first, edge_second = edge_queue.get()

        if not vertex_sets.is_same_set(edge_first, edge_second):
            size_mst += edge_weight
            vertex_sets.union_set(edge_first, edge_second)
            components -= 1

    return size_mst


def prim(uwgraph, source):
    """Algorytm Prima wyliczający długość MST.

    :param uwgraph: graf nieskierowany ważony
    :param source: początkowy wierzchołek
    :return: długość minimalnego drzewa spinającego"""
    size_mst = 0.0
    is_visited = [False] * (uwgraph.vertices_number + 1)
    vertex_queue = queue.PriorityQueue()
    vertex_queue.put((0.0, source))

    while not vertex_queue.empty():
        edge_weight, v = vertex_queue.get()

        if not is_visited[v]:
            is_visited[v] = True
            size_mst += edge_weight

            for s, wg in uwgraph.get_weighted_neighbours(v):
                if not is_visited[s]:
                    vertex_queue.put((wg, s))

    return size_mst
