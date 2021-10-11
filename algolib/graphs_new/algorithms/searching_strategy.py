# -*- coding: utf-8 -*-
"""Strategies for graph searching"""
from abc import ABCMeta, abstractmethod

from ..graph import Vertex


class BFSStrategy(metaclass=ABCMeta):
    @abstractmethod
    def for_root(self, root: Vertex):
        pass

    @abstractmethod
    def on_entry(self, vertex: Vertex):
        pass

    @abstractmethod
    def on_next_vertex(self, vertex: Vertex, neighbour: Vertex):
        pass

    @abstractmethod
    def on_exit(self, vertex: Vertex):
        pass


class DFSStrategy(BFSStrategy, metaclass=ABCMeta):
    @abstractmethod
    def on_edge_to_visited(self, vertex: Vertex, neighbour: Vertex):
        pass


class EmptyStrategy(DFSStrategy):
    def for_root(self, root: Vertex):
        pass

    def on_entry(self, vertex: Vertex):
        pass

    def on_next_vertex(self, vertex: Vertex, neighbour: Vertex):
        pass

    def on_exit(self, vertex: Vertex):
        pass

    def on_edge_to_visited(self, vertex: Vertex, neighbour: Vertex):
        pass
