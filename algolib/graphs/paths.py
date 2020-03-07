# -*- coding: utf-8 -*-
"""SHORTEST PATHS ALGORITHMS"""
import queue


def bellman_ford(diwgraph, source):
    """Algorytm Bellmana-Forda
    :param diwgraph: skierowany graf ważony
    :param source: wierzchołek początkowy
    :return: lista odległości wierzchołków"""
    distances = [diwgraph.INF] * diwgraph.vertices_number
    distances[source] = 0.0

    for _ in range(diwgraph.vertices_number - 1):
        for v, u, wg in diwgraph.get_weighted_edges():
            distances[u] = min(distances[u], distances[v] + wg)

    for v, u, wg in diwgraph.get_weighted_edges():
        if distances[v] < diwgraph.INF and distances[v] + wg < distances[u]:
            raise ValueError("Graph contains a negative cycle.")

    return distances


def dijkstra(wgraph, source):
    """Algorytm Dijkstry
    :param wgraph: graf ważony z wagami nieujemnymi
    :param source: wierzchołek początkowy
    :return: lista odległości wierzchołków"""
    if any(wg < 0.0 for _, _, wg in wgraph.get_weighted_edges()):
        raise ValueError("Graph contains an edge with negative weight.")

    vertex_queue = queue.PriorityQueue()
    vertex_queue.put((0.0, source))
    is_visited = [False] * wgraph.vertices_number
    distances = [wgraph.INF] * wgraph.vertices_number
    distances[source] = 0.0

    while not vertex_queue.empty():
        v = vertex_queue.get()[1]

        if not is_visited[v]:
            is_visited[v] = True

            for nb, wg in wgraph.get_weighted_neighbours(v):
                if distances[v] + wg < distances[nb]:
                    distances[nb] = distances[v] + wg
                    vertex_queue.put((distances[nb], nb))

    return distances


def floyd_warshall(diwgraph):
    """Algorytm Floyda-Warshalla
    :param diwgraph: skierowany graf ważony
    :return: macierz odległości wierzchołków"""
    distances = [[0.0 if v == u else diwgraph.INF for u in diwgraph.get_vertices()]
                 for v in diwgraph.get_vertices()]

    for v, u, wg in diwgraph.get_weighted_edges():
        distances[v][u] = wg

    for w in diwgraph.get_vertices():
        for v in diwgraph.get_vertices():
            for u in diwgraph.get_vertices():
                distances[v][u] = min(distances[v][u], distances[v][w] + distances[w][u])

    return distances
