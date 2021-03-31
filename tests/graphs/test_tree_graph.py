# -*- coding: utf-8 -*-
"""Tests: Structure of tree graph """
import unittest

from algolib.graphs import TreeGraph
from algolib.graphs.graph import Edge


class TreeGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = TreeGraph(0)

        self.test_object.add_vertex(1, 0)
        self.test_object.add_vertex(2, 0)
        self.test_object.add_vertex(3, 0)
        self.test_object.add_vertex(4, 1)
        self.test_object.add_vertex(5, 1)
        self.test_object.add_vertex(6, 2)
        self.test_object.add_vertex(7, 2)

    def test__setitem_getitem__when_setting_property__then_property(self):
        # given
        vertex_property = "x"
        edge_property = "y"
        vertex = 2
        edge = self.test_object.get_edge(6, 2)
        # when
        self.test_object[vertex] = vertex_property
        self.test_object[edge] = edge_property

        result_vertex = self.test_object[vertex]
        result_edge = self.test_object[edge]
        # then
        self.assertEqual(vertex_property, result_vertex)
        self.assertEqual(edge_property, result_edge)

    def test__vertices_count__then_number_of_vertices(self):
        # when
        result = self.test_object.vertices_count
        # then
        self.assertEqual(8, result)

    def test__vertices__then_all_vertices(self):
        # when
        result = self.test_object.vertices
        # then
        self.assertListEqual(list(range(8)), sorted(result))

    def test__add_vertex__when_new_vertex__then_created_edge(self):
        # given
        new_vertex = 13
        neighbour = 5
        vertex_property = "qwerty"
        edge_property = "asdfg"
        # when
        result = self.test_object.add_vertex(new_vertex, neighbour, vertex_property, edge_property)
        # then
        self.assertEqual(new_vertex, result.source)
        self.assertEqual(neighbour, result.destination)
        self.assertEqual(9, self.test_object.vertices_count)
        self.assertListEqual([5], list(self.test_object.neighbours(new_vertex)))
        self.assertEqual(vertex_property, self.test_object[new_vertex])
        self.assertEqual(edge_property, self.test_object[result])

    def test__add_vertex__when_existing_vertex__then_none(self):
        # given
        vertex = 6
        vertex_property = "qwerty"
        self.test_object[vertex] = vertex_property
        # when
        result = self.test_object.add_vertex(vertex, 3, "abcdefg", "xyz")
        # then
        self.assertIsNone(result)
        self.assertEqual(8, self.test_object.vertices_count)
        self.assertEqual(vertex_property, self.test_object[vertex])

    def test__edges_count__then_number_of_edges(self):
        # when
        result = self.test_object.edges_count
        # then
        self.assertEqual(7, result)

    def test__edges__then_all_edges(self):
        # when
        result = self.test_object.edges
        # then
        self.assertListEqual([
            Edge(1, 0),
            Edge(2, 0),
            Edge(3, 0),
            Edge(4, 1),
            Edge(5, 1),
            Edge(6, 2),
            Edge(7, 2)], sorted(result))

    def test__get_edge__when_in_direction__then_edge(self):
        # given
        source = 7
        destination = 2
        # when
        result = self.test_object.get_edge(source, destination)
        # then
        self.assertEqual(source, result.source)
        self.assertEqual(destination, result.destination)

    def test__neighbours__then_destination_vertices_of_outgoing_edges(self):
        # when
        result = self.test_object.neighbours(1)
        # then
        self.assertListEqual([0, 4, 5], sorted(result))

    def test__adjacent_edges__then_outgoing_edges(self):
        # when
        result = self.test_object.adjacent_edges(1)
        # then
        self.assertListEqual([Edge(1, 0), Edge(4, 1), Edge(5, 1)], sorted(result))

    def test__output_degree__then_number_of_outgoing_edges(self):
        # when
        result = self.test_object.output_degree(1)
        # then
        self.assertEqual(3, result)

    def test__input_degree__then_number_of_incoming_edges(self):
        # when
        result = self.test_object.input_degree(1)
        # then
        self.assertEqual(3, result)
