# -*- coding: utf-8 -*-
"""Hopcroft-Karp algorithm for matching in a bipartite graph."""
from collections import deque
import math
from typing import Dict

from ..multipartite_graph import MultipartiteGraph
from ..vertex import Vertex


def match(graph: MultipartiteGraph) -> Dict[Vertex, Vertex]:
    """Computes maximal matching in given bipartite graph.

    :param graph: the bipartite graph
    :return: the dictionary of matched vertices"""
    augmenter = _MatchAugmenter(graph)
    was_augmented = True

    while was_augmented:
        was_augmented = augmenter.augment_match()

    return augmenter.matching


class _MatchAugmenter:
    _INFINITY = math.inf

    def __init__(self, graph):
        if graph.groups_count != 2:
            raise ValueError("Graph is not bipartite")

        self._graph = graph
        self.matching = {}

    def augment_match(self):
        was_added = False
        visited = set()
        distances = {v: self._INFINITY for v in self._graph.vertices}
        self._bfs(distances)

        for vertex in self._unmatched_vertices():
            was_added = self._dfs(vertex, visited, distances) or was_added

        return was_added

    def _unmatched_vertices(self):
        for vertex in self._graph.vertices_from_group(1):
            if vertex not in self.matching:
                yield vertex

    def _bfs(self, distances):
        vertex_queue = deque()

        for vertex in self._unmatched_vertices():
            distances[vertex] = 0
            vertex_queue.append(vertex)

        while len(vertex_queue) > 0:
            vertex = vertex_queue.popleft()

            for neighbour in self._graph.neighbours(vertex):
                matched = self.matching.get(neighbour)

                if matched is not None and distances[matched] == self._INFINITY:
                    distances[matched] = distances[vertex] + 1
                    vertex_queue.append(matched)

    def _dfs(self, vertex, visited, distances):
        visited.add(vertex)

        for neighbour in self._graph.neighbours(vertex):
            matched = self.matching.get(neighbour)

            if matched is None:
                self.matching[vertex] = neighbour
                self.matching[neighbour] = vertex
                return True

            if matched not in visited and distances[matched] == distances[vertex] + 1 \
                    and self._dfs(matched, visited, distances):
                self.matching[vertex] = neighbour
                self.matching[neighbour] = vertex
                return True

        return False
