# -*- coding: utf-8 -*-
"""STRONGLY CONNECTED COMPONENTS ALGORITHM"""


def find_scc(digraph):
    """Algorytm wyznaczania silnie spójnych składowych grafu
    :param digraph: graf skierowany
    :return: numery silnie spójnych składowych dla wierzchołków"""
    comps = _GraphComponents(digraph).find_scc()
    components = [set() for i in range(max(comps) + 1)]

    for v in digraph.get_vertices():
        components[comps[v]].add(v)

    return components


class _GraphComponents:
    def __init__(self, digraph):
        self.__digraph = digraph
        self.__components = [None] * digraph.vertices_number
        self.__postorder = [None] * digraph.vertices_number

    def find_scc(self):
        """Algorytm wyznaczania silnie spójnych składowych grafu
        :return: numery silnie spójnych składowych dla wierzchołków"""
        timer = 0
        component = 0

        for v in self.__digraph.get_vertices():
            if self.__postorder[v] is None:
                timer = self.__dfs_order(v, timer)
                timer += 1

        self.__postorder.sort(reverse=True)
        self.__digraph.reverse()

        for _, v in self.__postorder:
            if self.__components[v] is None:
                self.__dfs_scc(v, component)
                component += 1

        return self.__components

    def __dfs_order(self, vertex, timer):
        """Algorytm DFS z licznikiem czasu wyznaczający porządek post-order wierzchołków
        :param vertex: aktualny wierzchołek
        :param timer: aktualny czas
        :return: nowy czas po przetworzeniu wierzchołka"""
        self.__postorder[vertex] = (0, vertex)
        timer += 1

        for neighbour in self.__digraph.get_neighbours(vertex):
            if self.__postorder[neighbour] is None:
                timer = self.__dfs_order(neighbour, timer)

        self.__postorder[vertex] = (timer, vertex)
        return timer + 1

    def __dfs_scc(self, vertex, component):
        """Algorytm DFS wyznaczający silnie spójne składowe
        :param vertex: aktualny wierzchołek
        :param component: numer składowej"""
        self.__components[vertex] = component

        for neighbour in self.__digraph.get_neighbours(vertex):
            if self.__components[neighbour] is None:
                self.__dfs_scc(neighbour, component)
