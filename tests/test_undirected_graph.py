# -*- coding: utf-8 -*-
"""Tests: Structure of undirected graphs"""
import unittest

from algolib.graphs import DirectedSimpleGraph, UndirectedSimpleGraph
from algolib.graphs.graph import Edge


class UndirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = UndirectedSimpleGraph(range(10))

    def tearDown(self):
        self._test_object = None

    def test__vertices_count(self):
        # when
        result = self._test_object.vertices_count
        # then
        self.assertEqual(10, result)

    def test__vertices(self):
        # when
        result = self._test_object.vertices
        # then
        self.assertListEqual(list(range(10)), sorted(result))

    def test__add_vertex(self):
        # given
        vertex_property = "qwerty"
        new_vertex = 13
        # when
        self._test_object.add_vertex(new_vertex, vertex_property)
        # then
        self.assertEqual(11, self._test_object.vertices_count)
        self.assertListEqual([], list(self._test_object.get_neighbours(new_vertex)))
        self.assertEqual(vertex_property, self._test_object[new_vertex])

    def test__edges_count(self):
        # given
        self._test_object.add_edge(7, 7)
        self._test_object.add_edge(1, 5)
        self._test_object.add_edge(2, 4)
        self._test_object.add_edge(8, 0)
        self._test_object.add_edge(6, 3)
        self._test_object.add_edge(3, 6)
        self._test_object.add_edge(9, 3)
        self._test_object.add_edge(8, 0)
        # when
        result = self._test_object.edges_count
        # then
        self.assertEqual(6, result)

    def test__edges(self):
        # given
        self._test_object.add_edge(7, 7)
        self._test_object.add_edge(1, 5)
        self._test_object.add_edge(2, 4)
        self._test_object.add_edge(8, 0)
        self._test_object.add_edge(6, 3)
        self._test_object.add_edge(3, 6)
        self._test_object.add_edge(9, 3)
        self._test_object.add_edge(8, 0)
        # when
        result = self._test_object.edges
        # then
        self.assertListEqual(
                [Edge(1, 5), Edge(2, 4), Edge(7, 7), Edge(6, 3), Edge(8, 0), Edge(9, 3)],
                sorted(result))

    def test__add_edge__then_new_edge(self):
        # given
        edge_property = "asdfgh"
        # when
        result = self._test_object.add_edge(1, 5, property)
        self._test_object.add_edge(1, 1)
        # then
        self.assertEqual(1, result.source)
        self.assertEqual(5, result.destination)
        self.assertEqual(edge_property, self._test_object[result])
        self.assertListEqual([1, 5], sorted(self._test_object.get_neighbours(1)))
        self.assertListEqual([1], list(self._test_object.get_neighbours(5)))

    def test__get_neighbours(self):
        # given
        self._test_object.add_edge(1, 1)
        self._test_object.add_edge(1, 3)
        self._test_object.add_edge(1, 4)
        self._test_object.add_edge(1, 7)
        self._test_object.add_edge(1, 9)
        self._test_object.add_edge(2, 1)
        self._test_object.add_edge(6, 1)
        # when
        result = self._test_object.get_neighbours(1)
        # then
        self.assertListEqual([1, 2, 3, 4, 6, 7, 9], sorted(result))

    def test__get_output_degree(self):
        # given
        self._test_object.add_edge(1, 1)
        self._test_object.add_edge(1, 3)
        self._test_object.add_edge(1, 4)
        self._test_object.add_edge(1, 7)
        self._test_object.add_edge(1, 9)
        self._test_object.add_edge(2, 1)
        self._test_object.add_edge(6, 1)
        # when
        result = self._test_object.get_output_degree(1)
        # then
        self.assertEqual(7, result)

    def test__get_input_degree(self):
        # given
        self._test_object.add_edge(1, 1)
        self._test_object.add_edge(3, 1)
        self._test_object.add_edge(4, 1)
        self._test_object.add_edge(7, 1)
        self._test_object.add_edge(9, 1)
        self._test_object.add_edge(1, 2)
        self._test_object.add_edge(1, 6)
        # when
        result = self._test_object.get_input_degree(1)
        # then
        self.assertEqual(7, result)

    def test__as_directed(self):
        # given
        self._test_object.add_edge(7, 7)
        self._test_object.add_edge(1, 5)
        self._test_object.add_edge(2, 4)
        self._test_object.add_edge(8, 0)
        self._test_object.add_edge(6, 3)
        self._test_object.add_edge(3, 6)
        self._test_object.add_edge(9, 3)
        self._test_object.add_edge(8, 0)
        # when
        result = self._test_object.to_directed()
        # then
        self.assertIsInstance(result, DirectedSimpleGraph)
        self.assertListEqual(sorted(self._test_object.vertices), sorted(result.vertices))
        self.assertListEqual(
                [Edge(0, 8), Edge(1, 5), Edge(2, 4), Edge(3, 6), Edge(3, 9), Edge(4, 2), Edge(5, 1),
                 Edge(6, 3), Edge(7, 7), Edge(8, 0), Edge(9, 3)], sorted(result.edges))
