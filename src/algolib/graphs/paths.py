# -*- coding: utf-8 -*-
"""ALGORYTMY WYZNACZANIA NAJKRÓTSZYCH ŚCIEŻEK W GRAFIE WAŻONYM"""
import queue
import math

_INF = math.inf    # Oznaczenie nieskończoności.

def bellman_ford(wgraph, source):
    """Algorytm Bellmana-Forda.
    :param wgraph: graf ważony
    :param source: wierzchołek początkowy
    :return: lista odległości wierzchołków"""
    distances = [_INF]*(wgraph.num_vertex+1)
    distances[source] = 0.0

    for _ in range(wgraph.num_vertex-1):
        for v in wgraph.vertices():
            for nb, wg in wgraph.neighbours(v):
                distances[nb] = min(distances[nb], distances[v]+wg)

    for v in wgraph.vertices():
        for nb, wg in wgraph.neighbours(v):
            if distances[v] < _INF and distances[v]+wg < distances[nb]:
                raise Exception("Graph contains a negative cycle.")

    return distances


def dijkstra(wgraph, source):
    """Algorytm Dijkstry.
    :param wgraph: graf ważony z wagami nieujemnymi
    :param source: wierzchołek początkowy"""
    vertex_queue = queue.PriorityQueue()
    vertex_queue.put( (0.0, source) )
    is_visited = [False]*wgraph.num_vertex
    distances = [_INF]*wgraph.num_vertex
    distances[source] = 0.0

    while not vertex_queue.empty():
        v = vertex_queue.get()[1]

        if not is_visited[v]:
            is_visited[v] = True

            for nb, wg in wgraph.neighbours(v):
                if distances[v]+wg < distances[nb]:
                    distances[nb] = distances[v]+wg
                    vertex_queue.put( (-distances[nb], nb) )

    return distances


def floyd_warshall(wgraph):
    """Algorytm Floyda-Warshalla.
    :param wgraph: graf ważony
    :returns: macierz odległości"""
    distances = wgraph.adjacency_matrix()

    for w in wgraph.vertices():
        for v in wgraph.vertices():
            for u in wgraph.vertices():
                distances[v][u] = min(distances[v][u], distances[v][w]+distances[w][u])

    return distances
