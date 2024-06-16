# -*- coding: utf-8 -*-
"""Tests: Structure of tree graph ."""
import unittest

from assertpy import assert_that

from algolib.graphs import Edge, TreeGraph, Vertex


class TreeGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = TreeGraph(0)
        self.test_object.add_vertex(1, Vertex(0))
        self.test_object.add_vertex(2, Vertex(0))
        self.test_object.add_vertex(3, Vertex(0))
        self.test_object.add_vertex(4, Vertex(1))
        self.test_object.add_vertex(5, Vertex(1))
        self.test_object.add_vertex(6, Vertex(2))
        self.test_object.add_vertex(7, Vertex(2))

    def test__properties_op_setitem_op_getitem__when_setting_property__then_property(self):
        # given
        vertex = Vertex(2)
        edge = self.test_object.get_edge(6, 2)
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
        assert_that(result).is_equal_to(8)

    def test__edges_count__then_number_of_edges(self):
        # when
        result = self.test_object.edges_count

        # then
        assert_that(result).is_equal_to(7)

    def test__vertices__then_all_vertices(self):
        # when
        result = self.test_object.vertices

        # then
        assert_that(sorted(result)).is_equal_to(
            [Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), Vertex(6),
             Vertex(7)])

    def test__edges__then_all_edges(self):
        # when
        result = self.test_object.edges

        # then
        assert_that(sorted(result)).is_equal_to(
            [Edge(Vertex(1), Vertex(0)), Edge(Vertex(2), Vertex(0)), Edge(Vertex(3), Vertex(0)),
             Edge(Vertex(4), Vertex(1)), Edge(Vertex(5), Vertex(1)), Edge(Vertex(6), Vertex(2)),
             Edge(Vertex(7), Vertex(2))])

    def test__get_vertex__when_exists__then_vertex(self):
        # given
        vertex_id = 3

        # when
        result = self.test_object.get_vertex(vertex_id)

        # then
        assert_that(result.id).is_equal_to(vertex_id)

    def test__get_edge__when_in_direction__then_edge(self):
        # given
        source = Vertex(7)
        destination = Vertex(2)

        # when
        result = self.test_object.get_edge(source, destination)

        # then
        assert_that(result.source).is_equal_to(source)
        assert_that(result.destination).is_equal_to(destination)

    def test__neighbours__then_destination_vertices_of_outgoing_edges(self):
        # when
        result = self.test_object.neighbours(Vertex(1))

        # then
        assert_that(sorted(result)).is_equal_to([Vertex(0), Vertex(4), Vertex(5)])

    def test__adjacent_edges__then_outgoing_edges(self):
        # when
        result = self.test_object.adjacent_edges(Vertex(1))

        # then
        assert_that(sorted(result)).is_equal_to(
            [Edge(Vertex(1), Vertex(0)), Edge(Vertex(4), Vertex(1)), Edge(Vertex(5), Vertex(1))])

    def test__output_degree__then_number_of_outgoing_edges(self):
        # when
        result = self.test_object.output_degree(Vertex(1))

        # then
        assert_that(result).is_equal_to(3)

    def test__input_degree__then_number_of_incoming_edges(self):
        # when
        result = self.test_object.input_degree(Vertex(1))

        # then
        assert_that(result).is_equal_to(3)

    def test__add_vertex__when_new_vertex__then_created_edge(self):
        # given
        new_vertex_id = 13
        neighbour = Vertex(5)
        vertex_property = "qwerty"
        edge_property = "asdfg"

        # when
        result = self.test_object.add_vertex(new_vertex_id, neighbour, vertex_property,
                                             edge_property)

        # then
        assert_that(result.source.id).is_equal_to(new_vertex_id)
        assert_that(result.destination).is_equal_to(neighbour)
        assert_that(self.test_object.vertices_count).is_equal_to(9)
        assert_that(list(self.test_object.neighbours(result.source))).is_equal_to([neighbour])
        assert_that(self.test_object.properties[result.source]).is_equal_to(vertex_property)
        assert_that(self.test_object.properties[result]).is_equal_to(edge_property)

    def test__add_vertex__when_existing_vertex__then_value_error(self):
        # given
        vertex = Vertex(6)
        vertex_property = "qwerty"
        self.test_object.properties[vertex] = vertex_property

        # when
        def function(vertex_):
            return self.test_object.add_vertex(vertex_, Vertex(3), "abcdefg", "xyz")

        # then
        assert_that(function).raises(ValueError).when_called_with(vertex)
        assert_that(self.test_object.vertices_count).is_equal_to(8)
        assert_that(self.test_object.properties[vertex]).is_equal_to(vertex_property)
