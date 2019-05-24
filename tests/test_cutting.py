# -*- coding: utf-8 -*-
"""TEST : Graph cutting algorithms."""
import unittest

from algolib.graphs import UndirectedSimpleGraph, find_edge_cut, find_vertex_cut


class CuttingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_edge_cut_when_present_bridges(self):
        graph = UndirectedSimpleGraph(12, [(0, 1), (0, 2), (0, 7), (1, 2), (1, 3), (1, 4), (3, 5),
                                           (4, 5), (5, 6), (7, 8), (7, 9), (7, 11), (8, 9), (9, 10),
                                           (9, 11), (10, 11)])

        result = find_edge_cut(graph)

        self.assertListEqual([(0, 7), (5, 6)], sorted(result))

    def test_find_edge_cut_when_no_bridges(self):
        graph = UndirectedSimpleGraph(6, [(0, 1), (0, 2), (1, 2),
                                          (1, 3), (1, 4), (3, 5), (4, 5)])

        result = find_edge_cut(graph)

        self.assertListEqual([], sorted(result))

    def test_find_vertex_cut_when_present_separators(self):
        graph = UndirectedSimpleGraph(12, [(0, 1), (0, 2), (0, 7), (1, 2), (1, 3), (1, 4), (3, 5),
                                           (4, 5), (5, 6), (7, 8), (7, 9), (7, 11), (8, 9), (9, 10),
                                           (9, 11), (10, 11)])

        result = find_vertex_cut(graph)

        self.assertListEqual([0, 1, 5, 7], sorted(result))

    def test_find_vertex_cut_when_no_separators(self):
        graph = UndirectedSimpleGraph(6, [(0, 1), (0, 2), (1, 2), (1, 3),
                                          (1, 4), (2, 3), (3, 5), (4, 5)])

        result = find_vertex_cut(graph)

        self.assertListEqual([], sorted(result))
