# -*- coding: utf-8 -*-
"""ALGORYTM HOPCROFTA-KARPA WYZNACZANIA SKOJARZEŃ W GRAFIE DWUDZIELNYM"""
import queue
import math

_NO_MATCH = None    # Oznaczenie braku skojarzenia.
_INF = math.inf    # Oznaczenie nieskończoności.

def match(bigraph):
    """Wyznaczanie maksymalnego skojarzenia.
    :param bigraph: graf dwudzielny
    :returns: pary skojarzonych wierzchołków"""
    augmenter = _MatchAugmenter(bigraph, [_NO_MATCH]*bigraph.vertex_number)

    match_added = True

    while match_added:
        match_added = augmenter.augment_match()

    matching = augmenter.matching

    return [(v, matching[v]) for v in bigraph.first_set() if matching[v] is not _NO_MATCH]


class _MatchAugmenter:
    def __init__(self, bigraph, matching):
        self.__bigraph = bigraph    # Graf dwudzielny.
        self.__matching = matching    # Skojarzenia wierzchołków.
        self.__distances = None    # Odległości wierzchołków.
        self.__is_visited = None    # Lista odwiedzonych wierzchołków.

    @property
    def matching(self):
        """Getter dla aktualnego skojarzenia.
        :returns: skojarzenia wierzchołków"""
        return self.__matching

    def augment_match(self):
        """Powiększanie skojarzenia przy pomocy scieżek powiększających.
        :returns: czy powiększono skojarzenie"""
        self.__distances = [_INF]*self.__bigraph.vertices_number
        self.__is_visited = [False]*self.__bigraph.vertices_number
        self.__bfs()

        return any([self.__dfs(v) for v in self.__bigraph.first_part()])

    def __bfs(self):
        """Algorytm BFS wyliczający odległości wierzchołków."""
        vertex_queue = queue.Queue()

        for v in self.__bigraph.first_part():
            self.__distances[v] = 0
            vertex_queue.put(v)

        while not vertex_queue.empty():
            v = vertex_queue.get()

            for nb in self.__bigraph.neighbours(v):
                if self.__matching[nb] is not _NO_MATCH \
                   and self.__distances[ self.__matching[nb] ] == _INF:
                    self.__distances[ self.__matching[nb] ] = self.__distances[v]+1
                    vertex_queue.put(self.__matching[nb])

    def __dfs(self, vertex):
        """Algorytm DFS powiększający skojarzenie za pomocą ścieżek powiekszających.
        :returns: czy powiększono skojarzenie"""
        self.__is_visited[vertex] = True

        for neighbour in self.__bigraph.neighbours(vertex):
            if self.__matching[neighbour] is _NO_MATCH:
                self.__matching[vertex] = neighbour
                self.__matching[neighbour] = vertex

                return True
            else:
                mtc = self.__matching[neighbour]

                if self.__distances[mtc] == self.__distances[vertex]+1 \
                   and not self.__is_visited[mtc] and self.__dfs(mtc):
                    self.__matching[vertex] = neighbour
                    self.__matching[neighbour] = vertex

                    return True

        return False
