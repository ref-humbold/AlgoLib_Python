# -*- coding: utf-8 -*-
"""HOPCROFT-KARP MATCHING ALGORITHM"""
import queue


def match(partgraph):
    """Wyznaczanie maksymalnego skojarzenia
    :param partgraph: graf wielodzielny
    :return: pary skojarzonych wierzchołków"""
    augmenter = _MatchAugmenter(partgraph)

    while augmenter.augment_match():
        pass

    matching = augmenter.matching
    return [(v, matching[v]) for v in partgraph.get_group(1) if matching[v] is not None]


class _MatchAugmenter:
    def __init__(self, partgraph, matching=None):
        if partgraph.groups_number != 2:
            raise ValueError("Graph is not bipartite.")

        # Reprezentacja grafu dwudzielnego
        self.__graph = partgraph
        # Skojarzenia wierzchołków
        self.__matching = matching
        # Odległości wierzchołków
        self.__distances = None
        # Lista odwiedzonych wierzchołków
        self.__is_visited = None

        if matching is None:
            self.__matching = [None] * partgraph.vertices_number

    @property
    def matching(self):
        """:return: skojarzenia wierzchołków"""
        return self.__matching

    def augment_match(self):
        """Powiększanie skojarzenia przy pomocy ścieżek powiększających
        :return: czy powiększono skojarzenie"""
        self.__distances = [self.__graph.INF] * self.__graph.vertices_number
        self.__is_visited = [False] * self.__graph.vertices_number
        self.__bfs()
        return any([self.__dfs(v) for v in self.__graph.get_group(1)])

    def __bfs(self):
        """Algorytm BFS wyliczający odległości wierzchołków"""
        vertex_queue = queue.Queue()

        for v in self.__graph.get_group(1):
            self.__distances[v] = 0
            vertex_queue.put(v)

        while not vertex_queue.empty():
            v = vertex_queue.get()

            for nb in self.__graph.get_neighbours(v):
                if self.__matching[nb] is not None \
                        and self.__distances[self.__matching[nb]] == self.__graph.INF:
                    self.__distances[self.__matching[nb]] = self.__distances[v] + 1
                    vertex_queue.put(self.__matching[nb])

    def __dfs(self, vertex):
        """Algorytm DFS powiększający skojarzenie za pomocą ścieżek powiekszających
        :return: czy powiększono skojarzenie"""
        self.__is_visited[vertex] = True

        for neighbour in self.__graph.get_neighbours(vertex):
            if self.__matching[neighbour] is None:
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
