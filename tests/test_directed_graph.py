# -*- coding: utf-8 -*-
"""Tests: Structure of directed graphs"""
import unittest

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.graph import Edge


class DirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = DirectedSimpleGraph(range(10))

    def tearDown(self):
        del self._test_object

    def test__setitem_getitem__when_setting_property__then_property(self):
        # given
        vertex_property = "x"
        edge_property = "y"
        vertex = 2
        edge = self._test_object.add_edge(0, 1)
        # when
        self._test_object[vertex] = vertex_property
        self._test_object[edge] = edge_property

        result_vertex = self._test_object[vertex]
        result_edge = self._test_object[edge]
        # then
        self.assertEqual(vertex_property, result_vertex)
        self.assertEqual(edge_property, result_edge)

    def test__getitem__when_no_property__then_null(self):
        # given
        edge = self._test_object.add_edge(6, 7)
        # when
        result_vertex = self._test_object[4]
        result_edge = self._test_object[edge]
        # then
        self.assertIsNone(result_vertex)
        self.assertIsNone(result_edge)

    def test__vertices_count__then_number_of_vertices(self):
        # when
        result = self._test_object.vertices_count
        # then
        self.assertEqual(10, result)

    def test__vertices__then_all_vertices(self):
        # when
        result = self._test_object.vertices
        # then
        self.assertListEqual(list(range(10)), sorted(result))

    def test__add_vertex__when_new_vertex__then_true(self):
        # given
        new_vertex = 13
        vertex_property = "qwerty"
        # when
        result = self._test_object.add_vertex(new_vertex, vertex_property)
        # then
        self.assertTrue(result)
        self.assertEqual(11, self._test_object.vertices_count)
        self.assertListEqual([], list(self._test_object.get_neighbours(new_vertex)))
        self.assertEqual(vertex_property, self._test_object[new_vertex])

    def test__add_vertex__when_existing_vertex__then_false(self):
        # given
        vertex = 6
        vertex_property = "qwerty"
        self._test_object[vertex] = vertex_property
        # when
        result = self._test_object.add_vertex(vertex, "abcdefg")
        # then
        self.assertFalse(result)
        self.assertEqual(10, self._test_object.vertices_count)
        self.assertEqual(vertex_property, self._test_object[vertex])

    def test__edges_count__then_number_of_edges(self):
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
        self.assertEqual(7, result)

    def test__edges__then_all_edges(self):
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
        self.assertListEqual([Edge(1, 5), Edge(2, 4), Edge(3, 6), Edge(6, 3), Edge(7, 7),
                              Edge(8, 0), Edge(9, 3)], sorted(result))

    def test__get_edge__when_in_direction__then_edge(self):
        # given
        source = 9
        destination = 5
        self._test_object.add_edge(source, destination)
        # when
        result = self._test_object.get_edge(source, destination)
        # then
        self.assertEqual(source, result.source)
        self.assertEqual(destination, result.destination)

    def test__get_edge__when_reversed_direction__then_None(self):
        # given
        source = 9
        destination = 5
        self._test_object.add_edge(source, destination)
        # when
        result = self._test_object.get_edge(destination, source)
        # then
        self.assertIsNone(result)

    def test__get_edge__when_not_exists__then_None(self):
        # when
        result = self._test_object.get_edge(1, 2)
        # then
        self.assertIsNone(result)

    def test__add_edge__when_new_edge__then_created_edge(self):
        # given
        edge_property = "zxcvb"
        # when
        result = self._test_object.add_edge(1, 5, edge_property)
        self._test_object.add_edge(1, 1)
        # then
        self.assertEqual(1, result.source)
        self.assertEqual(5, result.destination)
        self.assertEqual(edge_property, self._test_object[result])
        self.assertListEqual([1, 5], sorted(self._test_object.get_neighbours(1)))
        self.assertListEqual([], list(self._test_object.get_neighbours(5)))

    def add_edge__when_duplicated_edge__then_existing_edge(self):
        # given
        source = 3
        destination = 7
        expected = self._test_object.add_edge(source, destination)
        # when
        result = self._test_object.add_edge(source, destination)
        # then
        self.assertIs(expected, result)

    def test__get_neighbours__then_destination_vertices_of_outgoing_edges(self):
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
        self.assertListEqual([1, 3, 4, 7, 9], sorted(result))

    def test__get_adjacent_edges__then_outgoing_edges(self):
        # given
        self._test_object.add_edge(1, 1)
        self._test_object.add_edge(1, 3)
        self._test_object.add_edge(1, 4)
        self._test_object.add_edge(1, 7)
        self._test_object.add_edge(1, 9)
        self._test_object.add_edge(2, 1)
        self._test_object.add_edge(6, 1)
        # when
        result = self._test_object.get_adjacent_edges(1)
        # then
        self.assertListEqual([Edge(1, 1), Edge(1, 3), Edge(1, 4), Edge(1, 7), Edge(1, 9)],
                             sorted(result))

    def test__get_output_degree__then_number_of_outgoing_edges(self):
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
        self.assertEqual(5, result)

    def test__get_input_degree__then_number_of_incoming_edges(self):
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
        self.assertEqual(5, result)

    def test__reverse__then_all_edges_have_reversed_direction(self):
        # given
        vertex = 5
        vertex_property = "123456"
        edge_property = "zxcvb"
        edge = self._test_object.add_edge(1, 2)
        self._test_object.add_edge(3, 5)
        self._test_object.add_edge(4, 9)
        self._test_object.add_edge(5, 4)
        self._test_object.add_edge(5, 7)
        self._test_object.add_edge(6, 2)
        self._test_object.add_edge(6, 6)
        self._test_object.add_edge(7, 8)
        self._test_object.add_edge(9, 1)
        self._test_object.add_edge(9, 6)
        self._test_object[vertex] = vertex_property
        self._test_object[edge] = edge_property
        # when
        self._test_object.reverse()
        # then
        self.assertListEqual([Edge(1, 9), Edge(2, 1), Edge(2, 6), Edge(4, 5), Edge(5, 3),
                              Edge(6, 6), Edge(6, 9), Edge(7, 5), Edge(8, 7), Edge(9, 4)],
                             sorted(self._test_object.edges))
        self.assertEqual(vertex_property, self._test_object[vertex])
        self.assertIsNone(self._test_object[9])
        self.assertEqual(edge_property, self._test_object[self._test_object.get_edge(2, 1)])
        self.assertIsNone(self._test_object[self._test_object.get_edge(5, 3)])

    def test__reversed_copy__then_new_graph_with_reversed_edges(self):
        # given
        vertex = 5
        vertex_property = "123456"
        edge_property = "zxcvb"
        edge = self._test_object.add_edge(1, 2)
        self._test_object.add_edge(3, 5)
        self._test_object.add_edge(4, 9)
        self._test_object.add_edge(5, 4)
        self._test_object.add_edge(5, 7)
        self._test_object.add_edge(6, 2)
        self._test_object.add_edge(6, 6)
        self._test_object.add_edge(7, 8)
        self._test_object.add_edge(9, 1)
        self._test_object.add_edge(9, 6)
        self._test_object[vertex] = vertex_property
        self._test_object[edge] = edge_property
        # when
        result = self._test_object.reversed_copy()
        # then
        self.assertListEqual(self._test_object.vertices, result.vertices)
        self.assertListEqual([Edge(1, 9), Edge(2, 1), Edge(2, 6), Edge(4, 5), Edge(5, 3),
                              Edge(6, 6), Edge(6, 9), Edge(7, 5), Edge(8, 7), Edge(9, 4)],
                             sorted(result.edges))
        self.assertEqual(vertex_property, result[vertex])
        self.assertIsNone(result[9])
        self.assertEqual(edge_property, result[result.get_edge(2, 1)])
        self.assertIsNone(result[result.get_edge(5, 3)])
