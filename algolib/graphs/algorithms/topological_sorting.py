# -*- coding: utf-8 -*-
"""Algorithms for topological sorting of a directed acyclic graph."""
from queue import PriorityQueue
from typing import List

from .searching import dfs_recursive
from .searching_strategy import DFSStrategy
from ..directed_graph import DirectedGraph
from ..vertex import Vertex


class DirectedCyclicGraphError(ValueError):
    pass


def inputs_topological_sort(graph: DirectedGraph) -> List[Vertex]:
    """Topologically sorts the vertices of given directed acyclic graph using predecessors counting.

    :param graph: the directed acyclic graph
    :return: the topological order of vertices
    :raise ValueError: if the graph contains a cycle"""
    if graph.edges_count == 0:
        return list(graph.vertices)

    vertex_queue = PriorityQueue()
    input_degrees = {v: graph.input_degree(v) for v in graph.vertices}
    order = []

    for vertex in graph.vertices:
        if input_degrees[vertex] == 0:
            vertex_queue.put(vertex)

    while not vertex_queue.empty():
        vertex = vertex_queue.get()
        order.append(vertex)
        del input_degrees[vertex]

        for neighbour in graph.neighbours(vertex):
            input_degrees[neighbour] -= 1

            if input_degrees[neighbour] == 0:
                vertex_queue.put(neighbour)

    if len(order) != graph.vertices_count:
        raise DirectedCyclicGraphError("Given graph contains a cycle")

    return order


def dfs_topological_sort(graph: DirectedGraph) -> List[Vertex]:
    """Topologically sorts the vertices of given directed acyclic graph using depth-first search.

    :param graph: the directed acyclic graph
    :return: the topological order of vertices
    :raise ValueError: if the graph contains a cycle"""
    if graph.edges_count == 0:
        return list(graph.vertices)

    strategy = _TopologicalStrategy()
    dfs_recursive(graph, strategy, graph.vertices)
    return list(reversed(strategy.order))


class _TopologicalStrategy(DFSStrategy):
    def __init__(self):
        self.order = []

    def for_root(self, root):
        pass

    def on_entry(self, vertex):
        pass

    def on_next_vertex(self, vertex, neighbour):
        pass

    def on_exit(self, vertex):
        self.order.append(vertex)

    def on_edge_to_visited(self, vertex, neighbour):
        raise DirectedCyclicGraphError("The graph contains a cycle")
