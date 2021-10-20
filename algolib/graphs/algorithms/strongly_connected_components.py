# -*- coding: utf-8 -*-
"""Algorithm for strongly connected components"""
from typing import Iterable, Set

from .searching import dfs_recursive
from .searching_strategy import DFSStrategy
from ..directed_graph import DirectedGraph
from ..graph import Vertex


def find_scc(graph: DirectedGraph) -> Iterable[Set[Vertex]]:
    """Finds strongly connected components in given directed graph.

    :param graph: a directed graph
    :return: list of vertices in strongly connected components"""
    post_order_strategy = _PostOrderStrategy()
    dfs_recursive(graph, post_order_strategy, graph.vertices)
    vertices = [vertex for vertex, _ in sorted(post_order_strategy.post_times.items(),
                                               key=lambda item: item[1], reverse=True)]
    reversed_graph = graph.reversed_copy()
    scc_strategy = _SCCStrategy()
    dfs_recursive(reversed_graph, scc_strategy, vertices)
    return iter(scc_strategy.components)


class _PostOrderStrategy(DFSStrategy):
    def __init__(self):
        self.post_times = {}
        self._timer = 0

    def for_root(self, root):
        pass

    def on_entry(self, vertex):
        pass

    def on_next_vertex(self, vertex, neighbour):
        pass

    def on_exit(self, vertex):
        self.post_times[vertex] = self._timer
        self._timer += 1

    def on_edge_to_visited(self, vertex, neighbour):
        pass


class _SCCStrategy(DFSStrategy):
    def __init__(self):
        self.components = []

    def for_root(self, root):
        self.components.append(set())

    def on_entry(self, vertex):
        self.components[-1].add(vertex)

    def on_next_vertex(self, vertex, neighbour):
        pass

    def on_exit(self, vertex):
        pass

    def on_edge_to_visited(self, vertex, neighbour):
        pass
