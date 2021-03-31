# -*- coding: utf-8 -*-
"""Tests: Structure of undirected graph"""
import unittest

from algolib.graphs import DirectedGraph, UndirectedSimpleGraph
from algolib.graphs.graph import Edge


class UndirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = UndirectedSimpleGraph(range(10))

    def test__setitem_getitem__when_setting_property__then_property(self):
        # given
        vertex_property = "x"
        edge_property = "y"
        vertex = 2
        edge = self.test_object.add_edge_between(0, 1)
        # when
        self.test_object[vertex] = vertex_property
        self.test_object[edge] = edge_property

        result_vertex = self.test_object[vertex]
        result_edge = self.test_object[edge]
        # then
        self.assertEqual(vertex_property, result_vertex)
        self.assertEqual(edge_property, result_edge)

    def test__getitem__when_no_property__then_null(self):
        # given
        edge = self.test_object.add_edge_between(6, 7)
        # when
        result_vertex = self.test_object[4]
        result_edge = self.test_object[edge]
        # then
        self.assertIsNone(result_vertex)
        self.assertIsNone(result_edge)

    def test__getitem__when_not_existing__then_value_error(self):
        # then
        with self.assertRaises(ValueError):
            # when
            _ = self.test_object[14]
            _ = self.test_object[Edge(2, 8)]
            _ = self.test_object[Edge(0, -1)]

    def test__vertices_count__then_number_of_vertices(self):
        # when
        result = self.test_object.vertices_count
        # then
        self.assertEqual(10, result)

    def test__vertices__then_all_vertices(self):
        # when
        result = self.test_object.vertices
        # then
        self.assertListEqual(list(range(10)), sorted(result))

    def test__add_vertex__when_new_vertex__then_true(self):
        # given
        new_vertex = 13
        vertex_property = "qwerty"
        # when
        result = self.test_object.add_vertex(new_vertex, vertex_property)
        # then
        self.assertTrue(result)
        self.assertEqual(11, self.test_object.vertices_count)
        self.assertListEqual([], list(self.test_object.neighbours(new_vertex)))
        self.assertEqual(vertex_property, self.test_object[new_vertex])

    def test__add_vertex__when_existing_vertex__then_false(self):
        # given
        vertex = 6
        vertex_property = "qwerty"
        self.test_object[vertex] = vertex_property
        # when
        result = self.test_object.add_vertex(vertex, "abcdefg")
        # then
        self.assertFalse(result)
        self.assertEqual(10, self.test_object.vertices_count)
        self.assertEqual(vertex_property, self.test_object[vertex])

    def test__edges_count__then_number_of_edges(self):
        # given
        self.test_object.add_edge_between(7, 7)
        self.test_object.add_edge_between(1, 5)
        self.test_object.add_edge_between(2, 4)
        self.test_object.add_edge_between(8, 0)
        self.test_object.add_edge_between(6, 3)
        self.test_object.add_edge_between(3, 6)
        self.test_object.add_edge_between(9, 3)
        self.test_object.add_edge_between(8, 0)
        # when
        result = self.test_object.edges_count
        # then
        self.assertEqual(6, result)

    def test__edges__then_all_edges(self):
        # given
        self.test_object.add_edge_between(7, 7)
        self.test_object.add_edge_between(1, 5)
        self.test_object.add_edge_between(2, 4)
        self.test_object.add_edge_between(8, 0)
        self.test_object.add_edge_between(6, 3)
        self.test_object.add_edge_between(3, 6)
        self.test_object.add_edge_between(9, 3)
        self.test_object.add_edge_between(8, 0)
        # when
        result = self.test_object.edges
        # then
        self.assertListEqual([
            Edge(1, 5), Edge(2, 4),
            Edge(6, 3), Edge(7, 7),
            Edge(8, 0), Edge(9, 3)], sorted(result))

    def test__get_edge__when_in_direction__then_edge(self):
        # given
        source = 5
        destination = 9
        self.test_object.add_edge_between(source, destination)
        # when
        result = self.test_object.get_edge(source, destination)
        # then
        self.assertEqual(source, result.source)
        self.assertEqual(destination, result.destination)

    def test__get_edge__when_reversed_direction__then_edge(self):
        # given
        source = 9
        destination = 5
        self.test_object.add_edge_between(source, destination)
        # when
        result = self.test_object.get_edge(destination, source)
        # then
        self.assertEqual(source, result.source)
        self.assertEqual(destination, result.destination)

    def test__get_edge__when_not_exists__then_key_error(self):
        # then
        with self.assertRaises(KeyError):
            # when
            self.test_object.get_edge(1, 2)

    def test__add_edge_between__when_new_edge__then_created_edge(self):
        # given
        edge_property = "asdfgh"
        # when
        result = self.test_object.add_edge_between(1, 5, edge_property)
        self.test_object.add_edge_between(1, 1)
        # then
        self.assertEqual(1, result.source)
        self.assertEqual(5, result.destination)
        self.assertEqual(edge_property, self.test_object[result])
        self.assertListEqual([1, 5], sorted(self.test_object.neighbours(1)))
        self.assertListEqual([1], list(self.test_object.neighbours(5)))

    def test__add_edge_between__when_duplicated_edge__then_existing_edge(self):
        # given
        source = 3
        destination = 7
        expected = self.test_object.add_edge_between(source, destination)
        # when
        result = self.test_object.add_edge_between(source, destination)
        # then
        self.assertIs(expected, result)

    def test__adjacent_edges__then_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(1, 1)
        self.test_object.add_edge_between(1, 3)
        self.test_object.add_edge_between(1, 4)
        self.test_object.add_edge_between(1, 7)
        self.test_object.add_edge_between(1, 9)
        self.test_object.add_edge_between(2, 1)
        self.test_object.add_edge_between(6, 1)
        # when
        result = self.test_object.adjacent_edges(1)
        # then
        self.assertListEqual([
            Edge(1, 1),
            Edge(1, 3),
            Edge(1, 4),
            Edge(1, 7),
            Edge(1, 9),
            Edge(2, 1),
            Edge(6, 1)], sorted(result))

    def test__neighbours__then_destination_vertices_of_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(1, 1)
        self.test_object.add_edge_between(1, 3)
        self.test_object.add_edge_between(1, 4)
        self.test_object.add_edge_between(1, 7)
        self.test_object.add_edge_between(1, 9)
        self.test_object.add_edge_between(2, 1)
        self.test_object.add_edge_between(6, 1)
        # when
        result = self.test_object.neighbours(1)
        # then
        self.assertListEqual([1, 2, 3, 4, 6, 7, 9], sorted(result))

    def test__output_degree__then_number_of_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(1, 1)
        self.test_object.add_edge_between(1, 3)
        self.test_object.add_edge_between(1, 4)
        self.test_object.add_edge_between(1, 7)
        self.test_object.add_edge_between(1, 9)
        self.test_object.add_edge_between(2, 1)
        self.test_object.add_edge_between(6, 1)
        # when
        result = self.test_object.output_degree(1)
        # then
        self.assertEqual(7, result)

    def test__input_degree__then_number_of_incoming_edges(self):
        # given
        self.test_object.add_edge_between(1, 1)
        self.test_object.add_edge_between(3, 1)
        self.test_object.add_edge_between(4, 1)
        self.test_object.add_edge_between(7, 1)
        self.test_object.add_edge_between(9, 1)
        self.test_object.add_edge_between(1, 2)
        self.test_object.add_edge_between(1, 6)
        # when
        result = self.test_object.input_degree(1)
        # then
        self.assertEqual(7, result)

    def test__as_directed__then_directed_graph(self):
        # given
        vertex = 5
        vertex_property = "123456"
        edge_property = "zxcvb"
        edge = self.test_object.add_edge_between(1, 5)
        self.test_object.add_edge_between(7, 7)
        self.test_object.add_edge_between(2, 4)
        self.test_object.add_edge_between(8, 0)
        self.test_object.add_edge_between(6, 3)
        self.test_object.add_edge_between(3, 6)
        self.test_object.add_edge_between(9, 3)
        self.test_object.add_edge_between(8, 0)
        self.test_object[vertex] = vertex_property
        self.test_object[edge] = edge_property
        # when
        result = self.test_object.as_directed()
        # then
        self.assertIsInstance(result, DirectedGraph)
        self.assertListEqual(sorted(self.test_object.vertices), sorted(result.vertices))
        self.assertListEqual([
            Edge(0, 8),
            Edge(1, 5),
            Edge(2, 4),
            Edge(3, 6),
            Edge(3, 9),
            Edge(4, 2),
            Edge(5, 1),
            Edge(6, 3),
            Edge(7, 7),
            Edge(8, 0),
            Edge(9, 3)], sorted(result.edges))
        self.assertEqual(vertex_property, result[vertex])
        self.assertIsNone(result[9])
        self.assertEqual(edge_property, result[result.get_edge(1, 5)])
        self.assertEqual(edge_property, result[result.get_edge(5, 1)])
        self.assertIsNone(result[result.get_edge(8, 0)])
