# -*- coding: utf-8 -*-
"""WYSZUKIWANIE MOSTÓW I PUNKTÓW ARTYKULACJI W GRAFIE"""


def find_bridges(ugraph):
    """Znajdowanie mostów w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista krawędzi będących mostami"""
    return _GraphCutting(ugraph).bridges()


def find_vertex_separators(ugraph):
    """Znajdowanie punktów artykulacji w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista punktów artykulacji"""
    return _GraphCutting(ugraph).separators()


class _GraphCutting:
    # Oznaczenie braku głębokości (nieodwiedzenia) w drzewie DFS.
    _NO_DEPTH = None

    def __init__(self, graph):
        # Reprezentacja grafu nieskierowanego.
        self.__graph = graph
        # Ojciec w drzewie DFS.
        self.__dfs_parents = [None] * graph.vertices_number
        # Lista synów w drzewie DFS.
        self.__dfs_children = [[] for _ in self.__graph.get_vertices()]
        # Głębokość w drzewie DFS.
        self.__dfs_depths = [self._NO_DEPTH] * graph.vertices_number
        # Wartości funkcji LOW.
        self.__low_values = [None] * graph.vertices_number

    def bridges(self):
        """Znajdowanie mostów.
        :returns: lista krawędzi będących mostami"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is self._NO_DEPTH:
                self.__dfs(v, None, 0)

        return {(min(v, self.__dfs_parents[v]), max(v, self.__dfs_parents[v]))
                for v in self.__graph.get_vertices() if self.__has_bridge(v)}

    def separators(self):
        """Znajdowanie punktów artykulacji.
        :returns: lista punktów artykulacji"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is self._NO_DEPTH:
                self.__dfs(v, None, 0)

        return {v for v in self.__graph.get_vertices() if self.__is_separator(v)}

    def __has_bridge(self, vertex):
        """Sparwdzanie, czy od wierzchołka wychodzi krawędź będąca mostem.
        :param vertex: wierzchołek
        :returns: czy wierzchołek incydentny z mostem"""
        return self.__low_values[vertex] == self.__dfs_depths[vertex] \
            and not self.__is_dfs_root(vertex)

    def __is_separator(self, vertex):
        """Sparwdzanie, czy wierzchołek jest punktem artykulacji.
        :param vertex: wierzchołek
        :returns: czy wierzchołek to punkt artykulacji"""
        return len(self.__dfs_children[vertex]) > 1 \
            if self.__is_dfs_root(vertex) \
            else any(self.__low_values[c] >= self.__dfs_depths[vertex]
                     for c in self.__dfs_children[vertex])

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
                self.__low_values[vertex] = min(self.__low_values[vertex],
                                                self.__low_values[neighbour])
            elif neighbour != parent:
                self.__low_values[vertex] = min(self.__low_values[vertex],
                                                self.__dfs_depths[neighbour])
