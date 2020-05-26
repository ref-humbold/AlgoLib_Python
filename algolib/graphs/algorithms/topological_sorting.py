# -*- coding: utf-8 -*-
"""Algorithms for topological sorting"""
import queue


class DirectedCyclicGraphError(ValueError):
    pass


def sort_topological1(digraph):
    """Sortowanie topologiczne przez liczenie poprzedników.
    
    :param digraph: graf skierowany
    :return: porządek topologiczny wierzchołków"""
    vertex_queue = queue.PriorityQueue()
    indegs = [digraph.get_indegree(v) for v in digraph.get_vertices()]
    order = []

    for v in digraph.get_vertices():
        if indegs[v] == 0:
            vertex_queue.put(v)

    while not vertex_queue.empty():
        v = vertex_queue.get()
        order.append(v)
        indegs[v] = None

        for nb in digraph.get_neighbours(v):
            indegs[nb] -= 1

            if indegs[nb] == 0:
                vertex_queue.put(nb)

    if len(order) != digraph.vertices_number:
        raise DirectedCyclicGraphError()

    return iter(order)


def sort_topological2(digraph):
    """Sortowanie topologiczne z użyciem DFS.
    
    :param digraph: graf skierowany
    :return: porządek topologiczny wierzchołków"""
    indices = [None] * digraph.vertices_number
    order = []

    for v in reversed(sorted(digraph.get_vertices())):
        if indices[v] is None:
            _dfs(v, v, digraph, order, indices)

    return (v for v in reversed(order))


def _dfs(vertex, index, digraph, order, indices):
    indices[vertex] = (index, True)

    for neighbour in digraph.get_neighbours(vertex):
        if indices[neighbour] is None:
            _dfs(neighbour, index, digraph, order, indices)
        elif indices[neighbour] == (index, True):
            raise DirectedCyclicGraphError()

    order.append(vertex)
    indices[vertex] = (index, False)
