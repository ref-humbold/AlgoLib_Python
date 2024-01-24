# -*- coding: utf-8 -*-
"""Tests: Structure of multipartite graph."""
import unittest

from assertpy import assert_that

from algolib.graphs import Edge, GraphPartitionError, MultipartiteGraph, Vertex


class MultipartiteGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = MultipartiteGraph(5, [[0, 1, 2], [3, 4], [5, 6, 7, 8], [9]])
        self.test_object.add_edge_between(Vertex(0), Vertex(3))
        self.test_object.add_edge_between(Vertex(1), Vertex(5))
        self.test_object.add_edge_between(Vertex(2), Vertex(9))
        self.test_object.add_edge_between(Vertex(4), Vertex(6))
        self.test_object.add_edge_between(Vertex(7), Vertex(9))

    def test__properties_op_setitem_op_getitem__when_setting_property__then_property(self):
        # given
        vertex = Vertex(2)
        edge = self.test_object.get_edge(0, 3)
        vertex_property = "x"
        edge_property = "y"
        # when
        self.test_object.properties[vertex] = vertex_property
        self.test_object.properties[edge] = edge_property

        result_vertex = self.test_object.properties[vertex]
        result_edge = self.test_object.properties[edge]
        # then
        assert_that(result_vertex).is_equal_to(vertex_property)
        assert_that(result_edge).is_equal_to(edge_property)

    def test__vertices_count__then_number_of_vertices(self):
        # when
        result = self.test_object.vertices_count
        # then
        assert_that(result).is_equal_to(10)

    def test__vertices__then_all_vertices(self):
        # when
        result = self.test_object.vertices
        # then
        assert_that(sorted(result)).is_equal_to(
            [Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), Vertex(6), Vertex(7),
             Vertex(8), Vertex(9)])

    def test__edges_count__then_number_of_edges(self):
        # when
        result = self.test_object.edges_count
        # then
        assert_that(result).is_equal_to(5)

    def test__edges__then_all_edges(self):
        # when
        result = self.test_object.edges
        # then
        assert_that(sorted(result)).is_equal_to(
            [Edge(Vertex(0), Vertex(3)), Edge(Vertex(1), Vertex(5)), Edge(Vertex(2), Vertex(9)),
             Edge(Vertex(4), Vertex(6)), Edge(Vertex(7), Vertex(9))])

    def test__get_vertex__when_exists__then_vertex(self):
        # given
        vertex_id = 6
        # when
        result = self.test_object.get_vertex(vertex_id)
        # then
        assert_that(result.id).is_equal_to(vertex_id)

    def test__get_edge__when_exists__then_edge(self):
        # given
        source = Vertex(2)
        destination = Vertex(9)
        # when
        result = self.test_object.get_edge(source, destination)
        # then
        assert_that(result.source).is_equal_to(source)
        assert_that(result.destination).is_equal_to(destination)

    def test__neighbours__then_destination_vertices_of_outgoing_edges(self):
        # when
        result = self.test_object.neighbours(Vertex(9))
        # then
        assert_that(sorted(result)).is_equal_to([Vertex(2), Vertex(7)])

    def test__adjacent_edges__then_outgoing_edges(self):
        # when
        result = self.test_object.adjacent_edges(Vertex(9))
        # then
        assert_that(sorted(
            result)).is_equal_to([Edge(Vertex(2), Vertex(9)),
                                  Edge(Vertex(7), Vertex(9))])

    def test__output_degree__then_number_of_outgoing_edges(self):
        # when
        result = self.test_object.output_degree(Vertex(9))
        # then
        assert_that(result).is_equal_to(2)

    def test__input_degree__then_number_of_incoming_edges(self):
        # when
        result = self.test_object.input_degree(Vertex(9))
        # then
        assert_that(result).is_equal_to(2)

    def test__vertices_from_group__when_valid_group__then_vertices(self):
        # when
        result = self.test_object.vertices_from_group(2)
        # then
        assert_that(sorted(result)).is_equal_to([Vertex(5), Vertex(6), Vertex(7), Vertex(8)])

    def test__vertices_from_group__when_invalid_group__then_index_error(self):
        # then
        with self.assertRaises(IndexError):
            # when
            self.test_object.vertices_from_group(14)

    def test__add_vertex__when_new_vertex__then_created_vertex(self):
        # given
        new_vertex_id = 13
        vertex_property = "qwerty"
        # when
        result = self.test_object.add_vertex(4, new_vertex_id, vertex_property)
        # then
        assert_that(result.id).is_equal_to(new_vertex_id)
        assert_that(self.test_object.vertices_count).is_equal_to(11)
        assert_that(list(self.test_object.neighbours(result))).is_empty()
        assert_that(self.test_object.properties[result]).is_equal_to(vertex_property)

    def test__add_vertex__when_existing_vertex__then_value_error(self):
        # given
        vertex = Vertex(6)
        vertex_property = "qwerty"
        self.test_object.properties[vertex] = vertex_property

        # when
        def function(vertex_):
            return self.test_object.add_vertex(3, vertex_, "xyz")

        # then
        assert_that(function).raises(ValueError).when_called_with(vertex)
        assert_that(self.test_object.vertices_count).is_equal_to(10)
        assert_that(self.test_object.properties[vertex]).is_equal_to(vertex_property)

    def test__add_vertex__when_invalid_group__then_index_error(self):
        # when
        def function(group):
            return self.test_object.add_vertex(group, 19)

        # then
        assert_that(function).raises(IndexError).when_called_with(-3)

    def test__add_edge_between__when_new_edge__then_created_edge(self):
        # given
        vertex1 = Vertex(2)
        vertex2 = Vertex(8)
        edge_property = "asdfgh"
        # when
        result = self.test_object.add_edge_between(vertex1, vertex2, edge_property)
        # then
        assert_that(result.source).is_equal_to(vertex1)
        assert_that(result.destination).is_equal_to(vertex2)
        assert_that(self.test_object.properties[result]).is_equal_to(edge_property)
        assert_that(list(self.test_object.neighbours(vertex2))).is_equal_to([vertex1])

    def test__add_edge_between__when_duplicated_edge__then_value_error(self):
        # given
        source = Vertex(8)
        destination = Vertex(3)
        self.test_object.add_edge_between(source, destination)

        # when
        def function(source_, destination_):
            return self.test_object.add_edge_between(source_, destination_)

        # then
        assert_that(function).raises(ValueError).when_called_with(source, destination)

    def test__add_edge_between__when_same_group__then_graph_partition_error(self):
        # when
        def function(source, destination):
            return self.test_object.add_edge_between(source, destination)

        # then
        assert_that(function).raises(GraphPartitionError).when_called_with(Vertex(5), Vertex(8))

    def test__add_edge_between__when_invalid_vertex__then_value_error(self):
        # when
        def function(source, destination):
            return self.test_object.add_edge_between(source, destination)

        # then
        assert_that(function).raises(ValueError).when_called_with(Vertex(15), Vertex(18))
