# -*- coding: utf-8 -*-
"""TEST : Topological sorting algorithms."""
import unittest

from refhumbold.algolib.graphs import DirectedCyclicGraphException, DirectedSimpleGraph, \
    sort_topological1, sort_topological2


class TopologicalSortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sort_topological1_when_acyclic_graph(self):
        graph = DirectedSimpleGraph(6, [(0, 2), (0, 4), (1, 0), (1, 4), (3, 1),
                                        (3, 0), (3, 2), (5, 1), (5, 2), (5, 4)])

        result = sort_topological1(graph)

        self.assertListEqual([3, 5, 1, 0, 2, 4], list(result))

    def test_sort_topological1_when_cyclic_graph(self):
        graph = DirectedSimpleGraph(6, [(0, 2), (0, 4), (1, 0), (1, 4), (2, 1), (3, 1),
                                        (3, 0), (3, 2), (5, 1), (5, 2), (5, 4)])

        with self.assertRaises(DirectedCyclicGraphException):
            sort_topological1(graph)

    def test_sort_topological1_when_empty_graph(self):
        graph = DirectedSimpleGraph(6)

        result = sort_topological1(graph)

        self.assertListEqual([0, 1, 2, 3, 4, 5], list(result))

    def test_sort_topological2_when_acyclic_graph(self):
        graph = DirectedSimpleGraph(6, [(0, 2), (0, 4), (1, 0), (1, 4), (3, 1),
                                        (3, 0), (3, 2), (5, 1), (5, 2), (5, 4)])

        result = sort_topological2(graph)

        self.assertIn(list(result), [[3, 5, 1, 0, 2, 4], [5, 3, 1, 0, 2, 4],
                                     [3, 5, 1, 0, 4, 2], [5, 3, 1, 0, 4, 2]])

    def test_sort_topological2_when_cyclic_graph(self):
        graph = DirectedSimpleGraph(6, [(0, 2), (0, 4), (1, 0), (1, 4), (2, 1), (3, 1),
                                        (3, 0), (3, 2), (5, 1), (5, 2), (5, 4)])

        with self.assertRaises(DirectedCyclicGraphException):
            sort_topological2(graph)

    def test_sort_topological2_when_empty_graph(self):
        graph = DirectedSimpleGraph(6)

        result = sort_topological2(graph)

        self.assertListEqual([0, 1, 2, 3, 4, 5], list(result))
