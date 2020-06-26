# -*- coding: utf-8 -*-
"""Algorithms for topological sorting"""
import queue

from .searching import dfs_recursive


class DirectedCyclicGraphError(ValueError):
    def __init__(self, *args):
        super().__init__(*args)


def sort_topological1(graph):
    """Topological sorting algorithm using predecessors counting.

    :param graph: a directed graph
    :return: topological order of vertices
    :raise ValueError: if given graph contains a cycle"""
    if graph.edges_count == 0:
        return list(graph.vertices)

    vertex_queue = queue.PriorityQueue()
    input_degrees = {v: graph.get_input_degree(v) for v in graph.vertices}
    order = []

    for vertex in graph.vertices:
        if input_degrees[vertex] == 0:
            vertex_queue.put(vertex)

    while not vertex_queue.empty():
        vertex = vertex_queue.get()
        order.append(vertex)
        del input_degrees[vertex]

        for neighbour in graph.get_neighbours(vertex):
            input_degrees[neighbour] -= 1

            if input_degrees[neighbour] == 0:
                vertex_queue.put(neighbour)

    if len(order) != graph.vertices_count:
        raise DirectedCyclicGraphError("Given graph contains a cycle")

    return iter(order)


def sort_topological2(graph):
    """Topological sorting algorithm using DFS.

    :param graph: a directed graph
    :return: topological order of vertices
    :raise ValueError: if given graph contains a cycle"""
    if graph.edges_count == 0:
        return list(graph.vertices)

    strategy = _TopologicalStrategy()
    dfs_recursive(graph, strategy, graph.vertices)
    return list(reversed(strategy.order))


class _TopologicalStrategy:
    def __init__(self):
        self.order = []

    def for_root(self, root):
        pass

    def on_enter(self, vertex):
        pass

    def on_next_vertex(self, vertex, neighbour):
        pass

    def on_exit(self, vertex):
        self.order.append(vertex)

    def on_edge_to_visited(self, vertex, neighbour):
        raise DirectedCyclicGraphError("The graph contains a cycle")
