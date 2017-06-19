# -*- coding: utf-8 -*-
"""NAJNIŻSZY WSPÓLNY PRZODEK DWÓCH WIERZCHOŁKÓW W DRZEWIE"""
from math import log


def find_lca(treegraph, vertex1, vertex2, root=0):
    """Znajduje najniższego wspólnego przodka.
    :param treegraph: graf drzewo
    :param vertex1: wierzchołek 1
    :param vertex2: wierzchołek 2
    :param root: korzeń drzewa
    :returns: najniższy wspólny przodek"""
    if not treegraph.is_same_tree(vertex1, vertex2):
        raise ValueError("Vertices are not in the same tree.")

    if not treegraph.is_same_tree(vertex1, root) \
       or not treegraph.is_same_tree(vertex2, root):
        raise ValueError("Root vertex does not belong to the tree.")

    lca_finder = _LCAFinder(treegraph)

    return lca_finder.search_lca(vertex1, vertex2, root)


class _LCAFinder:
    def __init__(self, fgraph):
        # reprezentacja drzewa
        self.__graph = fgraph
        # ścieżki w drzewie
        self.__paths = None
        # czas wejścia i wyjścia dla wierzchołka
        self.__pre_post_times = None

    def search_lca(self, vertex1, vertex2, root):
        """Wyszukuje najniższego wpólnego przodka.
        :param vertex1: wierzchołek 1
        :param vertex2: wierzchołek 2
        :param root: korzeń drzewa
        :returns: najniższy wspólny przodek"""
        self.__paths = [[] for _ in range(self.__graph.vertices_number + 1)]
        self.__pre_post_times = [None] * (self.__graph.vertices_number + 1)
        self.__dfs(root, root, 0)

        for i in range(1, log(self.__graph.vertices_number, 2) + 3):
            for v in self.__graph.get_vertices():
                self.__paths[v].append(self.__paths[self.__paths[v][i - 1]][i - 1])

        return self.__search(vertex1, vertex2)

    def __search(self, vertex1, vertex2):
        """Wyszukuje najniższego wpólnego przodka.
        :param vertex1: wierzchołek 1
        :param vertex2: wierzchołek 2
        :returns: najniższy wspólny przodek"""
        def is_offspring(vt1, vt2):
            return self.__pre_post_times[vt1][0] >= self.__pre_post_times[vt2][0] \
                and self.__pre_post_times[vt1][1] <= self.__pre_post_times[vt2][1]

        if is_offspring(vertex1, vertex2):
            return vertex2

        if is_offspring(vertex2, vertex1):
            return vertex1

        for candidate in reversed(self.__paths[vertex1]):
            if not is_offspring(vertex2, candidate):
                return self.__search(candidate, vertex2)

        return self.__search(self.__paths[vertex1][0], vertex2)

    def __dfs(self, vertex, parent, timer):
        """Algorytm DFS z licznikiem czasu wyznaczający kolejne wierzchołki na ścieżce do korzenia.
        :param vertex: aktualny wierzchołek
        :param parent: ojciec wierzchołka
        :param timer: aktualny czas
        :returns: nowy czas po przetworzeniu wierzchołka"""
        self.__pre_post_times[vertex] = ()
        self.__paths[vertex][0] = parent
        pre_time = timer
        timer += 1

        for neighbour in self.__graph.get_neighbours(vertex):
            if self.__pre_post_times[neighbour] is not None:
                timer = self.__dfs(neighbour, vertex, timer)

        self.__pre_post_times[vertex] = (pre_time, timer)

        return timer + 1
