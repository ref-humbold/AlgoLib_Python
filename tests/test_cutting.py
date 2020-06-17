# -*- coding: utf-8 -*-
"""Tests: Algorithms for graph cutting"""
import unittest

from algolib.graphs import Edge, UndirectedSimpleGraph
from algolib.graphs.algorithms import find_edge_cut, find_vertex_cut


class CuttingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__find_edge_cut__when_present_bridges(self):
        # given
        graph = UndirectedSimpleGraph(range(12))
        graph.add_edge_between(0, 1)
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 7)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(1, 3)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(3, 5)
        graph.add_edge_between(4, 5)
        graph.add_edge_between(5, 6)
        graph.add_edge_between(7, 8)
        graph.add_edge_between(7, 9)
        graph.add_edge_between(7, 11)
        graph.add_edge_between(8, 9)
        graph.add_edge_between(9, 10)
        graph.add_edge_between(9, 11)
        graph.add_edge_between(10, 11)
        # when
        result = find_edge_cut(graph)
        # then
        self.assertListEqual([Edge(0, 7), Edge(5, 6)], sorted(result))

    def test__find_edge_cut__when_no_bridges(self):
        # given
        graph = UndirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 1)
        graph.add_edge_between(0, 2)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(1, 3)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(3, 5)
        graph.add_edge_between(4, 5)
        # when
        result = find_edge_cut(graph)
        # then
        self.assertListEqual([], sorted(result))

    def test__find_vertex_cut__when_present_separators(self):
        # given
        graph = UndirectedSimpleGraph(range(12))
        graph.add_edge_between(0, 1)
        graph.add_edge_between(0, 2)
        graph.add_edge_between(0, 7)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(1, 3)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(3, 5)
        graph.add_edge_between(4, 5)
        graph.add_edge_between(5, 6)
        graph.add_edge_between(7, 8)
        graph.add_edge_between(7, 9)
        graph.add_edge_between(7, 11)
        graph.add_edge_between(8, 9)
        graph.add_edge_between(9, 10)
        graph.add_edge_between(9, 11)
        graph.add_edge_between(10, 11)
        # when
        result = find_vertex_cut(graph)
        # then
        self.assertListEqual([0, 1, 5, 7], sorted(result))

    def test__find_vertex_cut__when_no_separators(self):
        # given
        graph = UndirectedSimpleGraph(range(6))
        graph.add_edge_between(0, 1)
        graph.add_edge_between(0, 2)
        graph.add_edge_between(1, 2)
        graph.add_edge_between(1, 3)
        graph.add_edge_between(1, 4)
        graph.add_edge_between(2, 3)
        graph.add_edge_between(3, 5)
        graph.add_edge_between(4, 5)
        # when
        result = find_vertex_cut(graph)
        # then
        self.assertListEqual([], sorted(result))
