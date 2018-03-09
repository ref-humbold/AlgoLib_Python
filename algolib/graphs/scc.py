# -*- coding: utf-8 -*-
"""ALGORYTM WYZNACZANIA SILNIE SPÓLJNYCH SKŁADOWYCH W GRAFIE SKIEROWANYM"""
from .directed_graph import DirectedGraph


def find_scc(digraph):
    """Algorytm wyznaczania silnie spójnych składowych grafu.
    :param digraph: graf skierowany
    :returns: numery silnie spójnych składowych dla wierzchołków"""
    comps = _StrongComponents(digraph).find_scc()
    components = [set() for i in range(max(comps) + 1)]

    for vertex in digraph.get_vertices():
        components[comps[vertex]].add(vertex)

    return components


class _StrongComponents:
    def __init__(self, digraph):
        self.__digraph = digraph
        self.__components = [None for v in digraph.get_vertices()]
        self.__postorder = [None for v in digraph.get_vertices()]

    def find_scc(self):
        """Algorytm wyznaczania silnie spójnych składowych grafu.
        :returns: numery silnie spójnych składowych dla wierzchołków"""
        timer = 0
        component = 0

        for vertex in self.__digraph.get_vertices():
            if self.__postorder[vertex] is None:
                timer = self.__dfs_order(vertex, timer)
                timer += 1

        self.__postorder.sort(reverse=True)
        self.__digraph.reverse()

        for _, vertex in self.__postorder:
            if self.__components[vertex] is None:
                self.__dfs_scc(vertex, component)
                component += 1

        return self.__components

    def __dfs_order(self, vertex, timer):
        """Algorytm DFS z licznikiem czasu wyznaczający porządek post-order wierzchołków.
        :param vertex: aktualny wierzchołek
        :param timer: aktualny czas
        :returns: nowy czas po przetworzeniu wierzchołka"""
        self.__postorder[vertex] = (0, vertex)
        timer += 1

        for neighbour in self.__digraph.get_neighbours(vertex):
            if self.__postorder[neighbour] is None:
                timer = self.__dfs_order(neighbour, timer)

        self.__postorder[vertex] = (timer, vertex)

        return timer + 1

    def __dfs_scc(self, vertex, component):
        """Algorytm DFS wyznaczający silnie spójne składowe.
        :param vertex: aktualny wierzchołek
        :param component: numer składowej"""
        self.__components[vertex] = component

        for neighbour in self.__digraph.get_neighbours(vertex):
            if self.__components[neighbour] is None:
                self.__dfs_scc(neighbour, component)
