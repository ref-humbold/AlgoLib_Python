# -*- coding: utf-8 -*-
# WYSZUKIWANIE MOSTÓW W GRAFIE
class GraphMosty:
    _NO_DEPTH = None    # oznaczenie braku głębokości (nieodwiedzenia) w drzewie DFS

    def __init__(self, n):
        """
        KONSTRUKTOR PUSTEGO GRAFU
        :param n: liczba wierzchołków
        """
        self.__num_vertex = n    # liczba wierzchołków grafu
        self.__graphrepr = [ [] for i in range(n+1) ]    # lista sąsiedztwa grafu

    def find_bridges(self):
        """
        WYZNACZA MOSTY W GRAFIE
        :returns: lista kraw�dzi b�d�cych mostami
        """
        self.__parents_DFS = [None]*(self.__num_vertex+1)    # ojciec wierzchołka w drzewie DFS
        self.__depths_DFS = [0]+[self._NO_DEPTH]*self.__num_vertex    # głębokość wierzchołka w drzewie DFS
        self.__values_LOW = [None]*(self.__num_vertex+1)    # wartości funkcji LOW dla wierzchołków

        for w in range(1, self.__num_vertex+1):
            if self.__depths_DFS[w] is self._NO_DEPTH:
                self.__parents_DFS[w] = 0
                self.__dfs(w)

        has_bridge = lambda w : self.__values_LOW[w] == self.__depths_DFS[w] and self.__parents_DFS[w] > 0

        return [(w, self.__parents_DFS[w]) for w in range(1, self.__num_vertex+1) if has_bridge(w)]

    def __dfs(self, vertex):
        """
        ALGORYTM DFS WYLICZAJ�CY FUNKCJ� LOW
        :param vertex: wierzchołek
        """
        self.__depths_DFS[vertex] = self.__depths_DFS[ self.__parents_DFS[vertex] ]+1
        self.__values_LOW[vertex] = self.__depths_DFS[vertex]

        for neghbour in self.__graphrepr[vertex]:
            if self.__depths_DFS[neghbour] is self._NO_DEPTH:
                self.__parents_DFS[neghbour] = vertex
                self.__dfs(neghbour)
                self.__values_LOW[vertex] = min(self.__values_LOW[vertex], self.__values_LOW[neghbour])
            elif neghbour != self.__parents_DFS[vertex]:
                self.__values_LOW[vertex] = min(self.__values_LOW[vertex], self.__depths_DFS[neghbour])

