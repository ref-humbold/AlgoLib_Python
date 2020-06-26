# -*- coding: utf-8 -*-
"""Algorithms for graph searching"""
import queue


def bfs(graph, strategy, roots):
    """Breadth-first-search algorithm.

    :param graph: a graph
    :param strategy: a searching strategy
    :param roots: starting vertices
    :return: iterable object of visited vertices"""
    reached = set()
    vertex_queue = queue.Queue()

    for root in roots:
        if root not in reached:
            strategy.for_root(root)
            vertex_queue.put(root)
            reached.add(root)

            while not vertex_queue.empty():
                vertex = vertex_queue.get()
                strategy.on_enter(vertex)

                for neighbour in graph.get_neighbours(vertex):
                    if neighbour not in reached:
                        strategy.on_next_vertex(vertex, neighbour)
                        reached.add(neighbour)
                        vertex_queue.put(neighbour)

                strategy.on_exit(vertex)

    return reached


def dfs_iterative(graph, strategy, roots):
    """Iterative depth-first-search algorithm.

    :param graph: a graph
    :param strategy: a searching strategy
    :param roots: starting vertices
    :return: iterable object of visited vertices"""
    reached = {}
    vertex_stack = queue.LifoQueue()
    iteration = 1

    for root in roots:
        if root not in reached:
            strategy.for_root(root)
            vertex_stack.put(root)

            while not vertex_stack.empty():
                vertex = vertex_stack.get()

                if vertex not in reached:
                    reached[vertex] = iteration
                    strategy.on_enter(vertex)

                    for neighbour in graph.get_neighbours(vertex):
                        if neighbour not in reached:
                            strategy.on_next_vertex(vertex, neighbour)
                            vertex_stack.put(neighbour)
                        elif reached[neighbour] == iteration:
                            strategy.on_edge_to_visited(vertex, neighbour)

                    strategy.on_exit(vertex)
                    reached[vertex] = -iteration

            iteration += 1

    return reached.keys()


def dfs_recursive(graph, strategy, roots):
    """Recursive depth-first-search algorithm.

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
    # Single step of recursive DFS
    vertex = state.vertex
    state.on_enter(vertex)
    strategy.on_enter(vertex)

    for neighbour in graph.get_neighbours(vertex):
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

    def on_enter(self, vertex):
        self.reached[vertex] = self.iteration

    def on_exit(self, vertex):
        self.reached[vertex] = -self.iteration
