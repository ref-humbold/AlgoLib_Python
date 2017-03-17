# -*- coding: utf-8 -*-
"""STRUKTURY GRAFÓW DWUDZIELNYCH"""
from abc import ABCMeta
from .graph import Graph, UndirectedSimpleGraph, UndirectedWeightedGraph

class BipartiteGraph(Graph, metaclass=ABCMeta):
    def __init__(self, n, prt, *args, **kwargs):
        super().__init__(n, *args, **kwargs)
        self.__parts = [v in prt for v in self.get_vertices()]    # Informacja o grupie wierzchołka.

    def first_part(self):
        """Wierzchołki pierwszej grupy.
        :returns: generator wierzchołków z pierwszej grupy"""
        return (v for v in self.get_vertices() if self.__parts[v])

    def second_part(self):
        """Wierzchołki drugiej grupy.
        :returns: generator wierzchołków z drugiej grupy"""
        return (v for v in self.get_vertices() if not self.__parts[v])

    def in_first_part(self, vertex):
        """Sprawdza, czy wierzchołek nalezy do pierwszej grupy.
        :param vertex: wierzchołek
        :returns: czy wierzchołek jest w pierwszej grupie"""
        return self.__parts[vertex]

    def in_second_part(self, vertex):
        """Sprawdza, czy wierzchołek nalezy do drugiej grupy.
        :param vertex: wierzchołek
        :returns: czy wierzchołek jest w drugiej grupie"""
        return not self.__parts[vertex]

    def is_part_different(self, vertex1, vertex2):
        """Sprawdza, czy  wierzchołki są w różnych grupach.
        :param vertex1: pierwszy wierzchołek
        :param vertex2: drugi wierzchołek
        :returns: czy wierzchołki są w różnych grupach"""
        return self.__parts[vertex1] != self.__parts[vertex2]


class BipartiteSimpleGraph(UndirectedSimpleGraph, BipartiteGraph):
    def __init__(self, n, prt, edges=None):
        super().__init__(n, prt, edges=None)

        if edges is not None:
            for e in edges:
                if self.is_part_different(e[0], e[1]):
                    self._graphrepr[ e[0] ].append(e[1])
                    self._graphrepr[ e[1] ].append(e[0])
                else:
                    raise ValueError("Graph is not bipartite")


class BipartiteWeightedGraph(UndirectedWeightedGraph, BipartiteGraph):
    def __init__(self, n, prt, edges=None):
        super().__init__(n, prt, edges=None)

        if edges is not None:
            for e in edges:
                if self.is_part_different(e[0], e[1]):
                    self._graphrepr[ e[0] ].append(e[1:3])
                    self._graphrepr[ e[1] ].append( (e[0], e[3]) )
                else:
                    raise ValueError("Graph is not bipartite")
