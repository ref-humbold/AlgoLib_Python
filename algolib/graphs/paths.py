# -*- coding: utf-8 -*-
"""ALGORYTMY WYZNACZANIA NAJKRÓTSZYCH ŚCIEŻEK W GRAFIE WAŻONYM"""
import queue


def bellman_ford(diwgraph, source):
    """Algorytm Bellmana-Forda.
    :param diwgraph: skierowany graf ważony
    :param source: wierzchołek początkowy
    :return: lista odległości wierzchołków"""
    distances = [diwgraph.inf] * diwgraph.vertices_number
    distances[source] = 0.0

    for _ in range(diwgraph.vertices_number - 1):
        for v, u, wg in diwgraph.get_weighted_edges():
            distances[u] = min(distances[u], distances[v] + wg)

    for v, u, wg in diwgraph.get_weighted_edges():
        if distances[v] < diwgraph.inf and distances[v] + wg < distances[u]:
            raise Exception("Graph contains a negative cycle.")

    return distances


def dijkstra(wgraph, source):
    """Algorytm Dijkstry.
    :param wgraph: graf ważony z wagami nieujemnymi
    :param source: wierzchołek początkowy"""
    vertex_queue = queue.PriorityQueue()
    vertex_queue.put((0.0, source))
    is_visited = [False] * wgraph.vertices_number
    distances = [wgraph.inf] * wgraph.vertices_number
    distances[source] = 0.0

    while not vertex_queue.empty():
        v = vertex_queue.get()[1]

        if not is_visited[v]:
            is_visited[v] = True

            for nb, wg in wgraph.get_weighted_neighbours(v):
                if distances[v] + wg < distances[nb]:
                    distances[nb] = distances[v] + wg
                    vertex_queue.put((-distances[nb], nb))

    return distances


def floyd_warshall(diwgraph):
    """Algorytm Floyda-Warshalla.
    :param diwgraph: skierowany graf ważony
    :returns: macierz odległości"""
    distances = [[diwgraph.inf for _ in diwgraph.get_vertices()] for _ in diwgraph.get_vertices()]

    for v, u, wg in diwgraph.get_weighted_edges():
        distances[v][u] = wg

    for w in diwgraph.get_vertices():
        for v in diwgraph.get_vertices():
            for u in diwgraph.get_vertices():
                distances[v][u] = min(distances[v][u], distances[v][w] + distances[w][u])

    return distances
