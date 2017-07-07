# -*- coding: utf-8 -*-
"""TESTY DLA ALGORYTMÓW WYSZUKIWANIA MOSTÓW I PUNKTÓW ARTYKULACJI"""
import unittest
from algolib.graphs import find_bridges, find_vertex_separators, UndirectedSimpleGraph


class CuttingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_bridges_when_present_bridges(self):
        graph = UndirectedSimpleGraph(12, [(0, 1), (0, 2), (0, 7), (1, 2), (1, 3), (1, 4), (3, 5),
                                           (4, 5), (5, 6), (7, 8), (7, 9), (7, 11), (8, 9), (9, 10),
                                           (9, 11), (10, 11)])

        result = find_bridges(graph)

        self.assertListEqual([(0, 7), (5, 6)], sorted(result))

    def test_find_bridges_when_no_bridges(self):
        graph = UndirectedSimpleGraph(6, [(0, 1), (0, 2), (1, 2),
                                          (1, 3), (1, 4), (3, 5), (4, 5)])

        result = find_bridges(graph)

        self.assertListEqual([], sorted(result))

    def test_find_vertex_separators_when_present_separators(self):
        graph = UndirectedSimpleGraph(12, [(0, 1), (0, 2), (0, 7), (1, 2), (1, 3), (1, 4), (3, 5),
                                           (4, 5), (5, 6), (7, 8), (7, 9), (7, 11), (8, 9), (9, 10),
                                           (9, 11), (10, 11)])

        result = find_vertex_separators(graph)

        self.assertListEqual([0, 1, 5, 7], sorted(result))

    def test_find_vertex_separators_when_no_separators(self):
        graph = UndirectedSimpleGraph(6, [(0, 1), (0, 2), (1, 2), (1, 3),
                                          (1, 4), (2, 3), (3, 5), (4, 5)])

        result = find_vertex_separators(graph)

        self.assertListEqual([], sorted(result))
