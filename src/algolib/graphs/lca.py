# -*- coding: utf-8 -*-
"""NAJNIŻSZY WSPÓLNY PRZODEK DWÓCH WIERZCHOŁKÓW W DRZEWIE"""
from math import log


class LCATreeGraph:
    def __init__(self, n):
        self.__num_vertex = n    # liczba wierzchołków grafu
        self.__graphrepr = [[] for i in range(n + 1)]    # lista sąsiedztwa grafu
        self.__is_visited = [False] * (n + 1)    # czy wierzchołek odwiedzony

    def find_lca(self, vertex1, vertex2, root=1):
        """
        ZNAJDUJE NAJNIŻSZEGO WSPÓLNEGO PRZODKA
        :param vertex1: wierzchołek 1
        :param vertex2: wierzchołek 2
        :param root: korzeń drzewa
        :returns: najniższy wspólny przodek
        """
        self.__paths = [[] for i in range(self.__num_vertex + 1)]    # ścieżki w drzewie
        # czas wejścia i wyjścia dla wierzchołka
        self.__pre_post_times = [None] * (self.__num_vertex + 1)

        self.__dfs(root, root, 0)

        for i in range(1, log(self.__num_vertex, 2) + 3):
            for w in range(1, self.__num_vertex + 1):
                self.__paths[w].append(self.__paths[self.__paths[w][i - 1]][i - 1])

        return self.__search_lca(vertex1, vertex2)

    def __dfs(self, vertex, parent, timer):
        """
        ALGORYTM DFS Z LICZNIKIEM CZASU WYZNACZAJĄCY KOLEJNE WIERZCHOŁKI NA ŚCIEŻCE DO KORZENIA
        :param vertex: aktualny wierzchołek
        :param parent: ojciec wierzchołka
        :param timer: aktualny czas
        :returns: nowy czas po przetworzeniu wierzchołka
        """
        self.__is_visited[vertex] = True
        self.__paths[vertex][0] = parent
        pre_time = timer
        timer += 1

        for neighbour in self.__graphrepr[vertex]:
            if not self.__is_visited[neighbour]:
                timer = self.__dfs(neighbour, vertex, timer)

        self.__pre_post_times[vertex] = (pre_time, timer)

        return timer + 1

    def __search_lca(self, vertex1, vertex2):
        """
        WYSZUKUJE NAJNIŻSZEGO WSPÓLNEGO PRZODKA
        :param vertex1: wierzchołek 1
        :param vertex2: wierzchołek 2
        :returns: najniższy wspólny przodek
        """
        def is_offspring(
            w, u): return self.__pre_post_times[w][0] >= self.__pre_post_times[u][0] and self.__pre_post_times[w][1] <= self.__pre_post_times[u][1];

        if is_offspring(vertex1, vertex2):
            return vertex2

        if is_offspring(vertex2, vertex1):
            return vertex1

        for i in range(len(self.__paths[vertex1]) - 1, 0, -1):
            candidate = self.__paths[vertex1][i]

            if not is_offspring(vertex2, candidate):
                return self.__search_lca(candidate, vertex2)

        return self.__search_lca(self.__paths[vertex1][0], vertex2)
