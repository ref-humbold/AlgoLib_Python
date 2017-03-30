# -*- coding: utf-8 -*-
"""ALGORYTMY SORTOWANIA TOPOLOGICZNEGO"""
import queue

def sort_topological1(digraph):
    """Sortowanie topologiczne przez liczenie poprzedników.
    :param digraph: graf skierowany
    :returns: porządek topologiczny wierzchołków"""
    vertex_queue = queue.Queue()
    indegs = [0]*(digraph.num_vertex)
    order = []

    for v, s in digraph.get_edges():
        indegs[s] += 1

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

    if len(order) != digraph.num_vertex+1:
        raise Exception("Digraph contains a cycle, so it cannot be sorted topologically.")

    return order


def sort_topological2(digraph):
    """Sortowanie topologiczne z użyciem DFS.
    :param digraph: graf skierowany
    :returns: porządek topologiczny wierzchołków"""
    is_visited = [False]*(digraph.num_vertex)
    order = []

    for v in digraph.get_vertices():
        if not is_visited[v]:
            dfs(v, digraph, order, is_visited)

    order.reverse()

    if len(order) != digraph.num_vertex+1:
        raise Exception("Digraph contains a cycle, so it cannot be sorted topologically.")

    return order


def dfs(vertex, digraph, order, is_visited):
    """Algorytm DFS wyznaczający kolejność wierzchołków.
    :param vertex: aktualny wierzchołek
    :param digraph: graf skierowany
    :param order: aktualny porządek topologiczny
    :param is_visited: czy wierzchołek odwiedzony"""
    is_visited[vertex] = True

    for neighbour in digraph.get_neighbours(vertex):
        if not is_visited[neighbour]:
            dfs(neighbour, digraph, order, is_visited)

    order.append(vertex)
