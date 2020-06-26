# -*- coding: utf-8 -*-
"""Tests: Structure of multipartite graph"""
import unittest

from algolib.graphs import Edge, GraphPartitionError, MultipartiteGraph


class MultipartiteGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = MultipartiteGraph(5, [[0, 1, 2], [3, 4], [5, 6, 7, 8], [9]])
        self._test_object.add_edge_between(0, 3)
        self._test_object.add_edge_between(1, 5)
        self._test_object.add_edge_between(2, 9)
        self._test_object.add_edge_between(4, 6)
        self._test_object.add_edge_between(7, 9)

    def tearDown(self):
        self._test_object = None

    def test__setitem_getitem__when_setting_property__then_property(self):
        # given
        vertex_property = "x"
        edge_property = "y"
        vertex = 2
        edge = self._test_object.get_edge(0, 3)
        # when
        self._test_object[vertex] = vertex_property
        self._test_object[edge] = edge_property

        result_vertex = self._test_object[vertex]
        result_edge = self._test_object[edge]
        # then
        self.assertEqual(vertex_property, result_vertex)
        self.assertEqual(edge_property, result_edge)

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

    def test__get_vertices_from_group__whenValidGroup__thenVertices(self):
        # when
        result = self._test_object.get_vertices_from_group(2)
        # then
        self.assertListEqual([5, 6, 7, 8], sorted(result))

    def test__get_vertices_from_group__when_invalid_group__then_index_error(self):
        # then
        with self.assertRaises(IndexError):
            # when
            self._test_object.get_vertices_from_group(14)

    def test__add_vertex__when_new_vertex__then_true(self):
        # given
        new_vertex = 13
        vertex_property = "qwerty"
        # when
        result = self._test_object.add_vertex(4, new_vertex, vertex_property)
        # then
        self.assertTrue(result)
        self.assertEqual(11, self._test_object.vertices_count)
        self.assertListEqual([], list(self._test_object.neighbours(new_vertex)))
        self.assertEqual(vertex_property, self._test_object[new_vertex])

    def test__add_vertex__when_existing_vertex__then_false(self):
        # given
        vertex = 6
        vertex_property = "qwerty"

        self._test_object[vertex] = vertex_property
        # when
        result = self._test_object.add_vertex(3, vertex, "xyz")
        # then
        self.assertFalse(result)
        self.assertEqual(10, self._test_object.vertices_count)
        self.assertEqual(vertex_property, self._test_object[vertex])

    def test__add_vertex__when_invalid_group__then_index_error(self):
        # then
        with self.assertRaises(IndexError):
            # when
            self._test_object.add_vertex(-3, 19)

    def test__edges_count__then_number_of_edges(self):
        # when
        result = self._test_object.edges_count
        # then
        self.assertEqual(5, result)

    def test__edges__then_all_edges(self):
        # when
        result = self._test_object.edges
        # then
        self.assertListEqual([
                Edge(0, 3), Edge(1, 5), Edge(2, 9),
                Edge(4, 6), Edge(7, 9)], sorted(result))

    def test__get_edge__when_Exists__then_edge(self):
        # given
        source = 2
        destination = 9
        # when
        result = self._test_object.get_edge(source, destination)
        # then
        self.assertEqual(source, result.source)
        self.assertEqual(destination, result.destination)

    def test__add_edge_between__whenNewEdge__thenCreatedEdge(self):
        # given
        vertex1 = 2
        vertex2 = 8
        edge_property = "asdfgh"
        # when
        result = self._test_object.add_edge_between(vertex1, vertex2, edge_property)
        # then
        self.assertEqual(vertex1, result.source)
        self.assertEqual(vertex2, result.destination)
        self.assertEqual(edge_property, self._test_object[result])
        self.assertListEqual([vertex1], list(self._test_object.neighbours(vertex2)))

    def test__add_edge_between__whenDuplicatedEdge__thenExistingEdge(self):
        # given
        source = 8
        destination = 3
        expected = self._test_object.add_edge_between(source, destination)
        # when
        result = self._test_object.add_edge_between(source, destination)
        # then
        self.assertIs(expected, result)

    def test__add_edge_between__whenSameGroup__then_graph_partition_error(self):
        # then
        with self.assertRaises(GraphPartitionError):
            # when
            self._test_object.add_edge_between(5, 8)

    def test__neighbours__thenDestinationVerticesOfOutgoingEdges(self):
        # when
        result = self._test_object.neighbours(9)
        # then
        self.assertListEqual([2, 7], sorted(result))

    def test__adjacent_edges__thenDestinationVerticesOfOutgoingEdges(self):
        # when
        result = self._test_object.adjacent_edges(9)
        # then
        self.assertListEqual([Edge(2, 9), Edge(7, 9)], sorted(result))

    def test__output_degree__thenNumberOfOutgoingEdges(self):
        # when
        result = self._test_object.output_degree(9)
        # then
        self.assertEqual(2, result)

    def test__input_degree__thenNumberOfIncomingEdges(self):
        # when
        result = self._test_object.input_degree(9)
        # then
        self.assertEqual(2, result)
