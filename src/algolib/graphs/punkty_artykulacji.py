# WYSZUKIWANIE PUNKTÓW ARTYKULACJI W GRAFIE
# -*- coding: utf-8 -*-
class GraphSep:
    _NO_DEPTH = None    # onaczenie braku głębokości (nieodwiedzenia) w drzewie DFS

    def __init__(self, n):
        """
        KONSTRUKTOR PUSTEGO GRAFU
        :param n: liczba wierzchołków
        """
        self.__num_vertex = n    # lista wierzchołków grafu
        self.__graphrepr = [ [] for i in range(n+1) ]    # lista sąsiedztwa grafu

    def find_vertex_separator(self):
        """
        WYZNACZANIE PUNKTÓW ARTYKULACJI
        :returns: lista punktów artykulacji
        """
        self.__childs_dfs = [ [] for w in self.__graphrepr ]    # lista synów wierzchołka w drzewie DFS
        self.__depths_dfs = [0]+[self._NO_DEPTH]*self.__num_vertex    # głębokość wierzchołka w drzewie DFS
        self.__values_low = [None]*(self.__num_vertex+1)    # wartości funkcji LOW dla wierzchołków

        for w in range(1, self.__num_vertex+1):
            if self.__depths_dfs[w] is self._NO_DEPTH:
                self.__dfs(w, 0)

        is_separator = lambda w: len(self.__childs_dfs[w]) > 1 if self.__depths_dfs[w] == 1 else any(self.__values_low[ch] >= self.__depths_dfs[w] for ch in self.__childs_dfs[w])

        return [w for w in range(1, self.__num_vertex+1) if is_separator(w)]

    def __dfs(self, vertex, parent):
        """
        ALGORYTM DFS WYLICZAJĄCY FUNKCJĘ LOW
        :param vertex: aktualny wierzchołek
        :param parent: ojciec wierzchołka
        """
        self.__depths_dfs[vertex] = self.__depths_dfs[parent]+1
        self.__values_low[vertex] = self.__depths_dfs[vertex]

        for neighbour in self.__graphrepr[vertex]:
            if self.__depths_dfs[neighbour] is self._NO_DEPTH:
                self.__childs_dfs[vertex].append(neighbour)
                self.__dfs(neighbour, vertex)
                self.__values_low[vertex] = min(self.__values_low[vertex], self.__values_low[neighbour])
            elif neighbour != parent:
                self.__values_low[vertex] = min(self.__values_low[vertex], self.__depths_dfs[neighbour])

