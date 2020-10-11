# -*- coding: utf-8 -*-
"""Algorithms for graph searching"""
from collections import deque


def bfs(graph, strategy, roots):
    """Breadth-first search algorithm.

    :param graph: a graph
    :param strategy: a searching strategy
    :param roots: starting vertices
    :return: iterable object of visited vertices"""
    reached = set()
    vertex_queue = deque()

    for root in roots:
        if root not in reached:
            strategy.for_root(root)
            vertex_queue.append(root)
            reached.add(root)

            while len(vertex_queue) > 0:
                vertex = vertex_queue.popleft()
                strategy.on_entry(vertex)

                for neighbour in graph.neighbours(vertex):
                    if neighbour not in reached:
                        strategy.on_next_vertex(vertex, neighbour)
                        reached.add(neighbour)
                        vertex_queue.append(neighbour)

                strategy.on_exit(vertex)

    return reached


def dfs_iterative(graph, strategy, roots):
    """Iterative depth-first search algorithm.

    :param graph: a graph
    :param strategy: a searching strategy
    :param roots: starting vertices
    :return: iterable object of visited vertices"""
    reached = {}
    vertex_stack = deque()
    iteration = 1

    for root in roots:
        if root not in reached:
            strategy.for_root(root)
            vertex_stack.append(root)

            while len(vertex_stack) > 0:
                vertex = vertex_stack.pop()

                if vertex not in reached:
                    reached[vertex] = iteration
                    strategy.on_entry(vertex)

                    for neighbour in graph.neighbours(vertex):
                        if neighbour not in reached:
                            strategy.on_next_vertex(vertex, neighbour)
                            vertex_stack.append(neighbour)
                        elif reached[neighbour] == iteration:
                            strategy.on_edge_to_visited(vertex, neighbour)

                    strategy.on_exit(vertex)
                    reached[vertex] = -iteration

            iteration += 1

    return reached.keys()


def dfs_recursive(graph, strategy, roots):
    """Recursive depth-first search algorithm.

    :param graph: a graph
    :param strategy: a searching strategy
    :param roots: starting vertices
    :return: iterable object of visited vertices"""
    state = _DfsRecursiveState()

    for root in roots:
        if root not in state.reached:
            strategy.for_root(root)
            state.vertex = root
            _dfs_recursive_step(graph, strategy, state)
            state.iteration += 1

    return state.reached.keys()


def _dfs_recursive_step(graph, strategy, state):
    # Single step of recursive DFS.
    vertex = state.vertex
    state.on_entry(vertex)
    strategy.on_entry(vertex)

    for neighbour in graph.neighbours(vertex):
        if neighbour not in state.reached:
            strategy.on_next_vertex(vertex, neighbour)
            state.vertex = neighbour
            _dfs_recursive_step(graph, strategy, state)
        elif state.reached[neighbour] == state.iteration:
            strategy.on_edge_to_visited(vertex, neighbour)

    strategy.on_exit(vertex)
    state.on_exit(vertex)


class _DfsRecursiveState:
    def __init__(self):
        self.vertex = None
        self.iteration = 1
        self.reached = {}

    def on_entry(self, vertex_):
        self.reached[vertex_] = self.iteration

    def on_exit(self, vertex_):
        self.reached[vertex_] = -self.iteration
