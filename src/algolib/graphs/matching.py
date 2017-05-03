# -*- coding: utf-8 -*-
"""ALGORYTM HOPCROFTA-KARPA WYZNACZANIA SKOJARZEŃ W GRAFIE DWUDZIELNYM"""
import queue
import math

NO_MATCH = None    # Oznaczenie braku skojarzenia.
INF = math.inf    # Oznaczenie nieskończoności.

def match(partgraph):
    """Wyznaczanie maksymalnego skojarzenia.
    :param partgraph: graf wielodzielny
    :returns: pary skojarzonych wierzchołków"""
    augmenter = MatchAugmenter(partgraph)

    while augmenter.augment_match():
        pass

    matching = augmenter.matching

    return [(v, matching[v]) for v in partgraph.get_group(1) if matching[v] is not NO_MATCH]


class MatchAugmenter:
    def __init__(self, partgraph, matching=None):
        if partgraph.groups_number != 2:
            raise ValueError("Graph is not bipartite.")

        self.__partgraph = partgraph    # Graf dwudzielny.
        self.__matching = matching    # Skojarzenia wierzchołków.
        self.__distances = None    # Odległości wierzchołków.
        self.__is_visited = None    # Lista odwiedzonych wierzchołków.

        if matching is None:
            self.__matching = [NO_MATCH]*partgraph.vertices_number

    @property
    def matching(self):
        """Getter dla aktualnego skojarzenia.
        :returns: skojarzenia wierzchołków"""
        return self.__matching

    def augment_match(self):
        """Powiększanie skojarzenia przy pomocy scieżek powiększających.
        :returns: czy powiększono skojarzenie"""
        self.__distances = [INF]*self.__partgraph.vertices_number
        self.__is_visited = [False]*self.__partgraph.vertices_number
        self.__bfs()

        return any([self.__dfs(v) for v in self.__partgraph.get_group(1)])

    def __bfs(self):
        """Algorytm BFS wyliczający odległości wierzchołków."""
        vertex_queue = queue.Queue()

        for v in self.__partgraph.get_group(1):
            self.__distances[v] = 0
            vertex_queue.put(v)

        while not vertex_queue.empty():
            v = vertex_queue.get()

            for nb in self.__partgraph.get_neighbours(v):
                if self.__matching[nb] is not NO_MATCH \
                   and self.__distances[self.__matching[nb]] == INF:
                    self.__distances[self.__matching[nb]] = self.__distances[v] + 1
                    vertex_queue.put(self.__matching[nb])

    def __dfs(self, vertex):
        """Algorytm DFS powiększający skojarzenie za pomocą ścieżek powiekszających.
        :returns: czy powiększono skojarzenie"""
        self.__is_visited[vertex] = True

        for neighbour in self.__partgraph.get_neighbours(vertex):
            if self.__matching[neighbour] is NO_MATCH:
                self.__matching[vertex] = neighbour
                self.__matching[neighbour] = vertex

                return True
            else:
                mtc = self.__matching[neighbour]

                if self.__distances[mtc] == self.__distances[vertex] + 1 \
                   and not self.__is_visited[mtc] and self.__dfs(mtc):
                    self.__matching[vertex] = neighbour
                    self.__matching[neighbour] = vertex

                    return True

        return False
