# -*- coding: utf-8 -*-
"""GRAPH SEARCHING ALGORITHMS"""
import queue


def bfs(graph, strategy, roots):
    """Algorytm BFS.
    :param graph: graf
    :param strategy: strategia dla wierzchołków
    :param roots: wierzchołki początkowe
    :returns: generator odwiedzonych wierzchołków"""
    reached = [0] * graph.vertices_number
    vertex_queue = queue.Queue()
    iteration = 1

    for root in roots:
        if reached[root] == 0:
            vertex_queue.put(root)
            reached[root] = iteration

            while not vertex_queue.empty():
                vertex = vertex_queue.get()
                strategy.preprocess(vertex)

                for neighbour in graph.get_neighbours(vertex):
                    if reached[neighbour] == 0:
                        strategy.for_neighbour(vertex, neighbour)
                        reached[neighbour] = iteration
                        vertex_queue.put(neighbour)
                    elif reached[neighbour] == iteration:
                        strategy.on_cycle(vertex, neighbour)

                strategy.postprocess(vertex)
                reached[vertex] = -iteration

            iteration += 1

    return map(lambda i: i != 0, reached)


def iter_dfs(graph, strategy, roots):
    """Iteracyjny algorytm DFS.
    :param graph: graf
    :param strategy: strategia dla wierzchołków
    :param roots: wierzchołki początkowe
    :returns: generator odwiedzonych wierzchołków"""
    reached = [0] * graph.vertices_number
    vertex_stack = queue.LifoQueue()
    iteration = 1

    for root in roots:
        if reached[root] == 0:
            vertex_stack.put(root)

            while not vertex_stack.empty():
                vertex = vertex_stack.get()
                strategy.preprocess(vertex)

                if reached[vertex] == 0:
                    reached[vertex] = iteration

                    for neighbour in graph.get_neighbours(vertex):
                        if reached[neighbour] == 0:
                            strategy.for_neighbour(vertex, neighbour)
                            reached[neighbour] = iteration
                            vertex_stack.put(neighbour)
                        elif reached[neighbour] == iteration:
                            strategy.on_cycle(vertex, neighbour)

                    strategy.postprocess(vertex)
                    reached[vertex] = -iteration

            iteration += 1

    return map(lambda i: i != 0, reached)


def rec_dfs(graph, strategy, roots):
    """Rekurencyjny algorytm DFS.
    :param graph: graf
    :param strategy: strategia dla wierzchołków
    :param roots: wierzchołki początkowe
    :returns: generator odwiedzonych wierzchołków"""
    state = _DfsrState(graph.vertices_number)

    for root in roots:
        if state.reached[root] == 0:
            _dfs_step(graph, strategy, root, state)
            state.iteration += 1

    return map(lambda i: i != 0, state.reached)


def _dfs_step(graph, strategy, vertex, state):
    """Krok rekurencyjnego DFS.
    :param graph: graf
    :param vertex: aktualny wierzchołek
    :param strategy: strategia dla wierzchołków
    :param state: aktualny stan rekurencji"""
    state.on_entry(vertex)
    strategy.preprocess(vertex)

    for neighbour in graph.get_neighbours(vertex):
        if state.reached[neighbour] == 0:
            strategy.for_neighbour(vertex, neighbour)
            _dfs_step(graph, strategy, neighbour, state)
        elif state.reached[neighbour] == state.iteration:
            strategy.on_cycle(vertex, neighbour)

    strategy.postprocess(vertex)
    state.on_exit(vertex)


class _DfsrState:
    def __init__(self, vertices_number):
        self.iteration = 1
        self.reached = [0] * vertices_number

    def on_entry(self, vertex):
        self.reached[vertex] = self.iteration

    def on_exit(self, vertex):
        self.reached[vertex] = -self.iteration
