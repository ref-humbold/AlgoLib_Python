# -*- coding: utf-8 -*-
"""HOPCROFT-KARP MATCHING ALGORITHM"""
import queue


def match(partgraph):
    """Wyznaczanie maksymalnego skojarzenia.

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

        self._graph = partgraph  # Reprezentacja grafu dwudzielnego
        self._matching = matching  # Skojarzenia wierzchołków
        self._distances = None  # Odległości wierzchołków
        self._is_visited = None  # Lista odwiedzonych wierzchołków

        if matching is None:
            self._matching = [None] * partgraph.vertices_number

    @property
    def matching(self):
        return self._matching

    def augment_match(self):
        self._distances = [self._graph.INF] * self._graph.vertices_number
        self._is_visited = [False] * self._graph.vertices_number
        self._bfs()
        return any([self._dfs(v) for v in self._graph.get_group(1)])

    def _bfs(self):
        vertex_queue = queue.Queue()

        for v in self._graph.get_group(1):
            self._distances[v] = 0
            vertex_queue.put(v)

        while not vertex_queue.empty():
            v = vertex_queue.get()

            for nb in self._graph.get_neighbours(v):
                if self._matching[nb] is not None \
                        and self._distances[self._matching[nb]] == self._graph.INF:
                    self._distances[self._matching[nb]] = self._distances[v] + 1
                    vertex_queue.put(self._matching[nb])

    def _dfs(self, vertex):
        self._is_visited[vertex] = True

        for neighbour in self._graph.get_neighbours(vertex):
            if self._matching[neighbour] is None:
                self._matching[vertex] = neighbour
                self._matching[neighbour] = vertex
                return True
            else:
                mtc = self._matching[neighbour]

                if self._distances[mtc] == self._distances[vertex] + 1 \
                        and not self._is_visited[mtc] and self._dfs(mtc):
                    self._matching[vertex] = neighbour
                    self._matching[neighbour] = vertex
                    return True

        return False
