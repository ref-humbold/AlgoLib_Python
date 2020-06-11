# -*- coding: utf-8 -*-
"""Strategies for graph searching"""


class EmptyStrategy:
    def __init__(self):
        pass

    def for_root(self, vertex):
        pass

    def on_entry(self, vertex):
        pass

    def on_next_vertex(self, vertex, neighbour):
        pass

    def on_exit(self, vertex):
        pass

    def on_edge_to_visited(self, vertex, neighbour):
        pass
