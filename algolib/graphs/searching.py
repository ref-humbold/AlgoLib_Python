# -*- coding: utf-8 -*-
"""ALGORYTMY PRZESZUKIWANIA GRAFU"""
import queue


def bfs(graph, root):
    """Algorytm BFS.
    :param graph: graf
    :param root: wierzchołek początkowy
    :returns: lista odwiedzonych wierzchołków"""
    is_visited = [False] * graph.vertices_number
    vertex_queue = queue.Queue()
    vertex_queue.put(root)

    is_visited[root] = True

    while not vertex_queue.empty():
        v = vertex_queue.get()

        for nb in graph.get_neighbours(v):
            if not is_visited[nb]:
                is_visited[nb] = True
                vertex_queue.put(nb)

    return is_visited


def iter_dfs(graph, root):
    """Iteracyjny algorytm DFS.
    :param graph: graf
    :param root: wierzchołek początkowy
    :returns: lista odwiedzonych wierzchołków"""
    is_visited = [False] * graph.vertices_number
    vertex_stack = queue.LifoQueue()
    vertex_stack.put(root)

    is_visited[root] = True

    while not vertex_stack.empty():
        v = vertex_stack.get()

        if not is_visited[v]:
            is_visited[v] = True

            for nb in graph.get_neighbours(v):
                if not is_visited[nb]:
                    vertex_stack.put(nb)

    return is_visited


def rec_dfs(graph, root):
    """Rekurencyjny algorytm DFS.
    :param graph: graf
    :param root: wierzchołek początkowy
    :returns: lista odwiedzonych wierzchołków"""
    is_visited = [False] * graph.vertices_number
    _dfs_step(root, graph, is_visited)

    return is_visited


def _dfs_step(vertex, graph, is_visited):
    """Krok rekurencyjnego DFS.
    :param vertex: aktualny wierzchołek
    :param graph: graf
    :param is_visited: lista odwiedzonych wierzchołków"""
    is_visited[vertex] = True

    for neighbour in graph.get_neighbours(vertex):
        if not is_visited[neighbour]:
            _dfs_step(neighbour, graph, is_visited)
