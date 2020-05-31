# -*- coding: utf-8 -*-
"""Algorithms for strategies for graph searching"""


class EmptyStrategy:
    def __init__(self):
        pass

    def preprocess(self, vertex):
        pass

    def for_neighbour(self, vertex, neighbour):
        pass

    def postprocess(self, vertex):
        pass

    def on_cycle(self, vertex, neighbour):
        pass


class TimerStrategy:
    def __init__(self, graph):
        self._timer = 1
        self._pre_times = [0] * graph.vertices_number
        self._post_times = [0] * graph.vertices_number

    def pre_time(self, vertex):
        return self._pre_times[vertex]

    def post_time(self, vertex):
        return self._post_times[vertex]

    def preprocess(self, vertex):
        self._pre_times[vertex] = self._timer
        self._timer += 1

    def for_neighbour(self, vertex, neighbour):
        pass

    def postprocess(self, vertex):
        self._post_times[vertex] = self._timer
        self._timer += 1

    def on_cycle(self, vertex, neighbour):
        pass
