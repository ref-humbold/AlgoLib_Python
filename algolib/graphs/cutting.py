# -*- coding: utf-8 -*-
"""GRAPH CUTTING ALGORITHMS (EDGE CUT AND VERTEX CUT)"""


def find_edge_cut(ugraph):
    """Wyznaczanie mostów w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista krawędzi będących mostami"""
    return _GraphCutting(ugraph).edge_cut()


def find_vertex_cut(ugraph):
    """Wyznaczanie punktów artykulacji w grafie.
    :param ugraph: graf nieskierowany
    :returns: lista punktów artykulacji"""
    return _GraphCutting(ugraph).vertex_cut()


class _GraphCutting:
    def __init__(self, graph):
        self.__graph = graph  # Reprezentacja grafu nieskierowanego.
        self.__dfs_parents = [None] * graph.vertices_number  # Ojciec w drzewie DFS.
        # Lista synów w drzewie DFS.
        self.__dfs_children = [[] for _ in self.__graph.get_vertices()]
        self.__dfs_depths = [None] * graph.vertices_number  # Głębokość w drzewie DFS.
        self.__low_values = [None] * graph.vertices_number  # Wartości funkcji LOW.

    def edge_cut(self):
        """Znajdowanie mostów.
        :returns: lista krawędzi będących mostami"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is None:
                self.__dfs(v, None, 0)

        return ((min(v, self.__dfs_parents[v]), max(v, self.__dfs_parents[v]))
                for v in self.__graph.get_vertices() if self.__has_bridge(v))

    def vertex_cut(self):
        """Znajdowanie punktów artykulacji.
        :returns: lista punktów artykulacji"""
        for v in self.__graph.get_vertices():
            if self.__dfs_depths[v] is None:
                self.__dfs(v, None, 0)

        return (v for v in self.__graph.get_vertices() if self.__is_separator(v))

    def __has_bridge(self, vertex):
        """Sprawdzanie, czy od wierzchołka wychodzi krawędź będąca mostem.
        :param vertex: wierzchołek
        :returns: czy wierzchołek incydentny z mostem"""
        return self.__low_values[vertex] == self.__dfs_depths[vertex] \
            and not self.__is_dfs_root(vertex)

    def __is_separator(self, vertex):
        """Sprawdzanie, czy wierzchołek jest punktem artykulacji.
        :param vertex: wierzchołek
        :returns: czy wierzchołek to punkt artykulacji"""
        return len(self.__dfs_children[vertex]) > 1 \
            if self.__is_dfs_root(vertex) \
            else any(self.__low_values[ch] >= self.__dfs_depths[vertex]
                     for ch in self.__dfs_children[vertex])

    def __is_dfs_root(self, vertex):
        """Sprawdzanie, czy wierzchołek jest korzeniem drzewa DFS
        :param vertex: wierzchołek
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
            if self.__dfs_depths[neighbour] is None:
                self.__dfs_children[vertex].append(neighbour)
                self.__dfs(neighbour, vertex, depth + 1)
                self.__low_values[vertex] = min(self.__low_values[vertex],
                                                self.__low_values[neighbour])
            elif neighbour != parent:
                self.__low_values[vertex] = min(self.__low_values[vertex],
                                                self.__dfs_depths[neighbour])
