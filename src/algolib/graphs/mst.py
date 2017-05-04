# -*- coding: utf-8 -*-
"""ALGORYTMY WYZNACZAJĄCE MINIMALNE DRZEWO SPINAJĄCE"""
import queue
from ..structures.disjoint_sets import DisjointSets

def kruskal(wgraph):
    """Algorytm Kruskala wyliczjący długość MST.
    :param wgraph: graf ważony
    :returns: długość minimalnego drzewa spinającego"""
    size_mst = 0.0
    components = wgraph.vertices_number
    edge_queue = queue.PriorityQueue()
    vertex_sets = DisjointSets(wgraph.get_vertices())

    for v, u, wg in wgraph.get_weighted_edges():
        edge_queue.put((-wg, v, u))

    while components > 1 and not edge_queue.empty():
        edge_weight, edge_first, edge_second = edge_queue.get()

        if vertex_sets.is_set_different(edge_first, edge_second):
            size_mst += abs(edge_weight)
            components -= 1
            vertex_sets.union_set(edge_first, edge_second)

        return size_mst


def prim(wgraph, source):
    """Algorytm Prima wyliczjący długość MST.
    :param wgraph: graf ważony
    :param source: początkowy wierzchołek
    :returns: długość minimalnego drzewa spinającego"""
    size_mst = 0.0
    is_visited = [False] * (wgraph.vertices_number + 1)
    vertex_queue = queue.PriorityQueue()
    vertex_queue.put((0.0, source))

    while not vertex_queue.empty():
        edge_weight, v = vertex_queue.get()

        if not is_visited[v]:
            is_visited[v] = True
            size_mst += abs(edge_weight)

            for s, wg in wgraph.get_weighted_neighbours(v):
                if not is_visited[s]:
                    vertex_queue.put((-wg, s))

    return size_mst
