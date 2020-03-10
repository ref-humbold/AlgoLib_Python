# -*- coding: utf-8 -*-
"""Graph cutting algorithms (edge cut and vertex cut)"""


def find_edge_cut(ugraph):
    """Wyznaczanie mostów w grafie.

    :param ugraph: graf nieskierowany
    :return: lista krawędzi będących mostami"""
    return _GraphCutting(ugraph).edge_cut()


def find_vertex_cut(ugraph):
    """Wyznaczanie punktów artykulacji w grafie.

    :param ugraph: graf nieskierowany
    :return: lista punktów artykulacji"""
    return _GraphCutting(ugraph).vertex_cut()


class _GraphCutting:
    def __init__(self, graph):
        self._graph = graph  # Reprezentacja grafu nieskierowanego
        self._dfs_parents = [None] * graph.vertices_number  # Ojciec w drzewie DFS
        self._dfs_children = [[] for _ in self._graph.get_vertices()]  # Lista synów w drzewie DFS
        self._dfs_depths = [None] * graph.vertices_number  # Głębokość w drzewie DFS
        self._low_values = [None] * graph.vertices_number  # Wartości funkcji LOW

    def edge_cut(self):
        for v in self._graph.get_vertices():
            if self._dfs_depths[v] is None:
                self._dfs(v, None, 0)

        return ((min(v, self._dfs_parents[v]), max(v, self._dfs_parents[v]))
                for v in self._graph.get_vertices() if self._has_bridge(v))

    def vertex_cut(self):
        for v in self._graph.get_vertices():
            if self._dfs_depths[v] is None:
                self._dfs(v, None, 0)

        return (v for v in self._graph.get_vertices() if self._is_separator(v))

    def _has_bridge(self, vertex):
        return self._low_values[vertex] == self._dfs_depths[vertex] \
               and not self._is_dfs_root(vertex)

    def _is_separator(self, vertex):
        return len(self._dfs_children[vertex]) > 1 \
            if self._is_dfs_root(vertex) \
            else any(self._low_values[ch] >= self._dfs_depths[vertex]
                     for ch in self._dfs_children[vertex])

    def _is_dfs_root(self, vertex):
        return self._dfs_depths[vertex] == 0

    def _dfs(self, vertex, parent, depth):
        self._dfs_parents[vertex] = parent
        self._dfs_depths[vertex] = depth
        self._low_values[vertex] = depth

        for neighbour in self._graph.get_neighbours(vertex):
            if self._dfs_depths[neighbour] is None:
                self._dfs_children[vertex].append(neighbour)
                self._dfs(neighbour, vertex, depth + 1)
                self._low_values[vertex] = min(self._low_values[vertex],
                                               self._low_values[neighbour])
            elif neighbour != parent:
                self._low_values[vertex] = min(self._low_values[vertex],
                                               self._dfs_depths[neighbour])
