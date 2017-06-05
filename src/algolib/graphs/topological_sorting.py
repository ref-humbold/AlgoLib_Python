# -*- coding: utf-8 -*-
"""ALGORYTMY SORTOWANIA TOPOLOGICZNEGO"""
import queue


class DirectedCyclicGraphException(Exception):
    def __init__(self):
        super().__init__()


def sort_topological1(digraph):
    """Sortowanie topologiczne przez liczenie poprzedników.
    :param digraph: graf skierowany
    :returns: porządek topologiczny wierzchołków"""
    vertex_queue = queue.Queue()
    indegs = [digraph.get_indegree(v) for v in digraph.get_vertices()]
    order = []

    for v in digraph.get_vertices():
        if indegs[v] == 0:
            vertex_queue.put(v)

    while not vertex_queue.empty():
        v = vertex_queue.get()
        order.append(v)
        indegs[v] = None

        for s in digraph.get_neighbours(v):
            indegs[s] -= 1

            if indegs[s] == 0:
                vertex_queue.put(s)

    if len(order) != digraph.vertices_number + 1:
        raise DirectedCyclicGraphException()

    return order


def sort_topological2(digraph):
    """Sortowanie topologiczne z użyciem DFS.
    :param digraph: graf skierowany
    :returns: porządek topologiczny wierzchołków"""
    is_visited = [False] * (digraph.vertices_number)
    order = []

    for v in digraph.get_vertices():
        if not is_visited[v]:
            _dfs(v, digraph, order, is_visited)

    order.reverse()

    if len(order) != digraph.vertices_number + 1:
        raise DirectedCyclicGraphException()

    return order


def _dfs(vertex, digraph, order, is_visited):
    """Algorytm DFS wyznaczający kolejność wierzchołków.
    :param vertex: aktualny wierzchołek
    :param digraph: graf skierowany
    :param order: aktualny porządek topologiczny
    :param is_visited: czy wierzchołek odwiedzony"""
    is_visited[vertex] = True

    for neighbour in digraph.get_neighbours(vertex):
        if not is_visited[neighbour]:
            _dfs(neighbour, digraph, order, is_visited)

    order.append(vertex)
