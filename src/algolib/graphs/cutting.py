# -*- coding: utf-8 -*-
"""WYSZUKIWANIE MOSTÓW I PUNKTÓW ARTYKULACJI W GRAFIE"""

def find_bridges(ugraph):
    """Znajdowanie mostów w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista krawędzi będących mostami"""
    return GraphCutting(ugraph).bridges()


def find_vertex_separator(ugraph):
    """Znajdowanie punktów artykulacji w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista punktów artykulacji"""
    return GraphCutting(ugraph).separators()


class GraphCutting:
    _NO_DEPTH = None    # oznaczenie braku głębokości (nieodwiedzenia) w drzewie DFS

    def __init__(self, graph):
        self.__graph = graph    # reprezentacja grafu nieskierowanego
        self.__dfs_parents = [None] * graph.get_vertices_number()    # ojciec w drzewie DFS
        self.__dfs_children = [[] for _ in self.__graph.get_vertices_number()]    # lista synów w drzewie DFS
        self.__dfs_depths = [self._NO_DEPTH] * graph.get_vertices_number()    # głębokość w drzewie DFS
        self.__low_values = [None] * graph.get_vertices_number()    # wartości funkcji LOW

    def bridges(self):
        """Znajdowanie mostów.
        :returns: lista krawędzi będących mostami"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is self._NO_DEPTH:
                self.__dfs(v, None, 0)

        has_bridge = lambda v: self.__low_values[v] == self.__dfs_depths[v] \
                               and not self.__is_dfs_root(v)

        return [(v, self.__dfs_parents[v]) for v in self.__graph.get_vertices() if has_bridge(v)]

    def separators(self):
        """Znajdowanie punktów artykulacji.
        :returns: lista punktów artykulacji"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is self._NO_DEPTH:
                self.__dfs(v, None, 0)

        is_separator = lambda v: len(self.__dfs_children[v]) > 1 \
                                 if self.__is_dfs_root(v) \
                                 else any(self.__low_values[c] >= self.__dfs_depths[v] \
                                          for c in self.__dfs_children[v])

        return [v for v in self.__graph.get_vertices() if is_separator(v)]

    def __is_dfs_root(self, vertex):
        """Sprawdzanie, czy wierzchołek jest korzeniem drzewa DFS
        :returns: czy wierzchołek to korzeń"""
        return self.__dfs_depths[vertex] == 0

    def __dfs(self, vertex, parent, depth):
        """Algorytm DFS wyliczający funkcję LOW.
        :param vertex: aktualny wierzchołek
        :param parent: ojciec wierzchołka
        :param depth: głębokość"""
        self.__dfs_parents[vertex] = parent
        self.__dfs_depths[vertex] = depth
        self.__low_values[vertex] = depth

        for neighbour in self.__graph.get_neighbours(vertex):
            if self.__dfs_depths[neighbour] is self._NO_DEPTH:
                self.__dfs_children[vertex].append(neighbour)
                self.__dfs(neighbour, vertex, depth + 1)
                self.__low_values[vertex] = min(self.__low_values[vertex], \
                                                self.__low_values[neighbour])
            elif neighbour != parent:
                self.__low_values[vertex] = min(self.__low_values[vertex], \
                                                self.__dfs_depths[neighbour])
