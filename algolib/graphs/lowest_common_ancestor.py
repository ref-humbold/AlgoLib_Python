# -*- coding: utf-8 -*-
"""Lowest common ancestor algorithm"""
from math import log


def find_lca(treegraph, vertex1, vertex2, root=0):
    """Wyznaczanie najniższego wspólnego przodka.

    :param treegraph: graf drzewo
    :param vertex1: wierzchołek 1
    :param vertex2: wierzchołek 2
    :param root: korzeń drzewa
    :return: najniższy wspólny przodek"""
    return _LCAFinder(treegraph).search_lca(vertex1, vertex2, root)


class _LCAFinder:
    def __init__(self, treegraph):
        self._graph = treegraph  # Reprezentacja drzewa
        self._paths = \
            [[] for _ in self._graph.get_vertices()]  # Skompresowane ścieżki do korzenia drzewa
        self._pre_post_times = \
            [None] * self._graph.vertices_number  # Czas wejścia i wyjścia dla wierzchołka

    def search_lca(self, vertex1, vertex2, root):
        self._dfs(root, root, 0)

        for i in range(0, int(log(self._graph.vertices_number, 2)) + 3):
            for v in self._graph.get_vertices():
                if len(self._paths[v]) > 0:
                    self._paths[v].append(self._paths[self._paths[v][i]][i])

        return self._search(vertex1, vertex2)

    def _search(self, vertex1, vertex2):
        def is_offspring(vt1, vt2):
            return self._pre_post_times[vt1][0] >= self._pre_post_times[vt2][0] and \
                   self._pre_post_times[vt1][1] <= self._pre_post_times[vt2][1]

        if is_offspring(vertex1, vertex2):
            return vertex2

        if is_offspring(vertex2, vertex1):
            return vertex1

        for candidate in reversed(self._paths[vertex1]):
            if not is_offspring(vertex2, candidate):
                return self._search(candidate, vertex2)

        return self._search(self._paths[vertex1][0], vertex2)

    def _dfs(self, vertex, parent, timer):
        self._pre_post_times[vertex] = ()
        self._paths[vertex].append(parent)
        pre_time = timer
        timer += 1

        for neighbour in self._graph.get_neighbours(vertex):
            if self._pre_post_times[neighbour] is None:
                timer = self._dfs(neighbour, vertex, timer)

        self._pre_post_times[vertex] = (pre_time, timer)
        return timer + 1
