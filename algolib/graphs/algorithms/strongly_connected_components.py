# -*- coding: utf-8 -*-
"""Strongly connected components algorithm"""


def find_scc(digraph):
    """Algorytm wyznaczania silnie spójnych składowych grafu.

    :param digraph: graf skierowany
    :return: numery silnie spójnych składowych dla wierzchołków"""
    comps = _GraphComponents(digraph).find_scc()
    components = [set() for i in range(max(comps) + 1)]

    for v in digraph.get_vertices():
        components[comps[v]].add(v)

    return components


class _GraphComponents:
    def __init__(self, digraph):
        self._digraph = digraph
        self._components = [None] * digraph.vertices_number
        self._postorder = [None] * digraph.vertices_number

    def find_scc(self):
        timer = 0
        component = 0

        for v in self._digraph.get_vertices():
            if self._postorder[v] is None:
                timer = self._dfs_order(v, timer)
                timer += 1

        self._postorder.sort(reverse=True)
        self._digraph.reverse()

        for _, v in self._postorder:
            if self._components[v] is None:
                self._dfs_scc(v, component)
                component += 1

        return self._components

    def _dfs_order(self, vertex, timer):
        self._postorder[vertex] = (0, vertex)
        timer += 1

        for neighbour in self._digraph.get_neighbours(vertex):
            if self._postorder[neighbour] is None:
                timer = self._dfs_order(neighbour, timer)

        self._postorder[vertex] = (timer, vertex)
        return timer + 1

    def _dfs_scc(self, vertex, component):
        self._components[vertex] = component

        for neighbour in self._digraph.get_neighbours(vertex):
            if self._components[neighbour] is None:
                self._dfs_scc(neighbour, component)
