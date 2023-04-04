# -*- coding: utf-8 -*-
"""Tests: Structure of directed graph"""
import unittest

from assertpy import assert_that

from algolib.graphs import DirectedSimpleGraph, Edge, Vertex


class DirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = DirectedSimpleGraph(range(10))

    def test__properties_setitem_getitem__when_setting_property__then_property(self):
        # given
        vertex = Vertex(2)
        edge = self.test_object.add_edge_between(Vertex(0), Vertex(1))
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

    def test__properties_getitem__when_no_property__then_null(self):
        # given
        vertex = Vertex(4)
        edge = self.test_object.add_edge_between(Vertex(6), Vertex(7))
        # when
        result_vertex = self.test_object.properties[vertex]
        result_edge = self.test_object.properties[edge]
        # then
        assert_that(result_vertex).is_none()
        assert_that(result_edge).is_none()

    def test__properties_getitem__when_not_existing__then_value_error(self):
        # when
        def function(item):
            return self.test_object.properties[item]

        # then
        assert_that(function).raises(ValueError).when_called_with(Vertex(14))
        assert_that(function).raises(ValueError).when_called_with(Edge(Vertex(2), Vertex(8)))
        assert_that(function).raises(ValueError).when_called_with(Edge(Vertex(0), Vertex(-1)))

    def test__properties_delitem__then_none(self):
        # given
        vertex = Vertex(4)
        edge = self.test_object.add_edge_between(Vertex(6), Vertex(7))
        self.test_object.properties[vertex] = "x"
        self.test_object.properties[edge] = "y"
        # when
        del self.test_object.properties[vertex]
        del self.test_object.properties[edge]
        # then
        assert_that(self.test_object.properties[vertex]).is_none()
        assert_that(self.test_object.properties[edge]).is_none()

    def test__vertices_count__then_number_of_vertices(self):
        # when
        result = self.test_object.vertices_count
        # then
        assert_that(result).is_equal_to(10)

    def test__edges_count__then_number_of_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(7), Vertex(7))
        self.test_object.add_edge_between(Vertex(1), Vertex(5))
        self.test_object.add_edge_between(Vertex(2), Vertex(4))
        self.test_object.add_edge_between(Vertex(8), Vertex(0))
        self.test_object.add_edge_between(Vertex(6), Vertex(3))
        self.test_object.add_edge_between(Vertex(3), Vertex(6))
        self.test_object.add_edge_between(Vertex(9), Vertex(3))
        # when
        result = self.test_object.edges_count
        # then
        assert_that(result).is_equal_to(7)

    def test__vertices__then_all_vertices(self):
        # when
        result = self.test_object.vertices
        # then
        assert_that(sorted(result)).is_equal_to(
            [Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), Vertex(6), Vertex(7),
             Vertex(8), Vertex(9)])

    def test__edges__then_all_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(7), Vertex(7))
        self.test_object.add_edge_between(Vertex(1), Vertex(5))
        self.test_object.add_edge_between(Vertex(2), Vertex(4))
        self.test_object.add_edge_between(Vertex(8), Vertex(0))
        self.test_object.add_edge_between(Vertex(6), Vertex(3))
        self.test_object.add_edge_between(Vertex(3), Vertex(6))
        self.test_object.add_edge_between(Vertex(9), Vertex(3))
        # when
        result = self.test_object.edges
        # then
        assert_that(sorted(result)).is_equal_to(
            [Edge(Vertex(1), Vertex(5)), Edge(Vertex(2), Vertex(4)), Edge(Vertex(3), Vertex(6)),
             Edge(Vertex(6), Vertex(3)), Edge(Vertex(7), Vertex(7)), Edge(Vertex(8), Vertex(0)),
             Edge(Vertex(9), Vertex(3))])

    def test__get_vertex__when_exists__then_vertex(self):
        # given
        vertex_id = 6
        # when
        result = self.test_object.get_vertex(vertex_id)
        # then
        assert_that(result.id).is_equal_to(vertex_id)

    def test__get_vertex__when_not_exists__then_key_error(self):
        # when
        def function(id_):
            return self.test_object.get_vertex(id_)

        # then
        assert_that(function).raises(KeyError).when_called_with(14)

    def test__get_edge__when_in_direction__then_edge(self):
        # given
        source = Vertex(9)
        destination = Vertex(5)
        self.test_object.add_edge_between(source, destination)
        # when
        result = self.test_object.get_edge(source, destination)
        # then
        assert_that(result.source).is_equal_to(source)
        assert_that(result.destination).is_equal_to(destination)

    def test__get_edge__when_reversed_direction__then_key_error(self):
        # given
        source = Vertex(9)
        destination = Vertex(5)
        self.test_object.add_edge_between(source, destination)

        # then
        def function(source_, destination_):
            return self.test_object.get_edge(source_, destination_)

        # then
        assert_that(function).raises(KeyError).when_called_with(destination, source)

    def test__get_edge__when_not_exists__then_key_error(self):
        # when
        def function(source, destination):
            return self.test_object.get_edge(source, destination)

        # then
        assert_that(function).raises(KeyError).when_called_with(1, 2)

    def test__adjacent_edges__then_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(1), Vertex(1))
        self.test_object.add_edge_between(Vertex(1), Vertex(3))
        self.test_object.add_edge_between(Vertex(1), Vertex(4))
        self.test_object.add_edge_between(Vertex(1), Vertex(7))
        self.test_object.add_edge_between(Vertex(1), Vertex(9))
        self.test_object.add_edge_between(Vertex(2), Vertex(1))
        self.test_object.add_edge_between(Vertex(6), Vertex(1))
        # when
        result = self.test_object.adjacent_edges(Vertex(1))
        # then
        assert_that(sorted(result)).is_equal_to(
            [Edge(Vertex(1), Vertex(1)), Edge(Vertex(1), Vertex(3)), Edge(Vertex(1), Vertex(4)),
             Edge(Vertex(1), Vertex(7)), Edge(Vertex(1), Vertex(9))])

    def test__neighbours__then_destination_vertices_of_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(1), Vertex(1))
        self.test_object.add_edge_between(Vertex(1), Vertex(3))
        self.test_object.add_edge_between(Vertex(1), Vertex(4))
        self.test_object.add_edge_between(Vertex(1), Vertex(7))
        self.test_object.add_edge_between(Vertex(1), Vertex(9))
        self.test_object.add_edge_between(Vertex(2), Vertex(1))
        self.test_object.add_edge_between(Vertex(6), Vertex(1))
        # when
        result = self.test_object.neighbours(Vertex(1))
        # then
        assert_that(sorted(
                result)).is_equal_to([Vertex(1),
                                      Vertex(3),
                                      Vertex(4),
                                      Vertex(7),
                                      Vertex(9)])

    def test__output_degree__then_number_of_outgoing_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(1), Vertex(1))
        self.test_object.add_edge_between(Vertex(1), Vertex(3))
        self.test_object.add_edge_between(Vertex(1), Vertex(4))
        self.test_object.add_edge_between(Vertex(1), Vertex(7))
        self.test_object.add_edge_between(Vertex(1), Vertex(9))
        self.test_object.add_edge_between(Vertex(2), Vertex(1))
        self.test_object.add_edge_between(Vertex(6), Vertex(1))
        # when
        result = self.test_object.output_degree(Vertex(1))
        # then
        assert_that(result).is_equal_to(5)

    def test__input_degree__then_number_of_incoming_edges(self):
        # given
        self.test_object.add_edge_between(Vertex(1), Vertex(1))
        self.test_object.add_edge_between(Vertex(3), Vertex(1))
        self.test_object.add_edge_between(Vertex(4), Vertex(1))
        self.test_object.add_edge_between(Vertex(7), Vertex(1))
        self.test_object.add_edge_between(Vertex(9), Vertex(1))
        self.test_object.add_edge_between(Vertex(1), Vertex(2))
        self.test_object.add_edge_between(Vertex(1), Vertex(6))
        # when
        result = self.test_object.input_degree(Vertex(1))
        # then
        assert_that(result).is_equal_to(5)

    def test__add_vertex__when_new_vertex__then_created_vertex(self):
        # given
        new_vertex_id = 13
        vertex_property = "qwerty"
        # when
        result = self.test_object.add_vertex(new_vertex_id, vertex_property)
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
            return self.test_object.add_vertex(vertex_, "abcdefg")

        # then
        assert_that(function).raises(ValueError).when_called_with(vertex)
        assert_that(self.test_object.vertices_count).is_equal_to(10)
        assert_that(self.test_object.properties[vertex]).is_equal_to(vertex_property)

    def test__add_edge_between__when_new_edge__then_created_edge(self):
        # given
        vertex1 = Vertex(1)
        vertex2 = Vertex(5)
        edge_property = "zxcvb"
        # when
        result = self.test_object.add_edge_between(vertex1, vertex2, edge_property)
        self.test_object.add_edge_between(vertex1, vertex1)
        # then
        assert_that(result.source).is_equal_to(vertex1)
        assert_that(result.destination).is_equal_to(vertex2)
        assert_that(self.test_object.properties[result]).is_equal_to(edge_property)
        assert_that(sorted(self.test_object.neighbours(vertex1))).is_equal_to([vertex1, vertex2])
        assert_that(list(self.test_object.neighbours(vertex2))).is_empty()

    def test__add_edge_between__when_duplicated_edge__then_value_error(self):
        # given
        source = Vertex(3)
        destination = Vertex(7)
        _ = self.test_object.add_edge_between(source, destination)

        # when
        def function(source_, destination_):
            return self.test_object.add_edge_between(source_, destination_)

        # then
        assert_that(function).raises(ValueError).when_called_with(source, destination)

    def test__reverse__then_all_edges_have_reversed_direction(self):
        # given
        vertex = Vertex(5)
        vertex_property = "123456"
        edge_property = "zxcvb"
        edge = self.test_object.add_edge_between(Vertex(1), Vertex(2))
        self.test_object.add_edge_between(Vertex(3), Vertex(5))
        self.test_object.add_edge_between(Vertex(4), Vertex(9))
        self.test_object.add_edge_between(Vertex(5), Vertex(4))
        self.test_object.add_edge_between(Vertex(5), Vertex(7))
        self.test_object.add_edge_between(Vertex(6), Vertex(2))
        self.test_object.add_edge_between(Vertex(6), Vertex(6))
        self.test_object.add_edge_between(Vertex(7), Vertex(8))
        self.test_object.add_edge_between(Vertex(9), Vertex(1))
        self.test_object.add_edge_between(Vertex(9), Vertex(6))
        self.test_object.properties[vertex] = vertex_property
        self.test_object.properties[edge] = edge_property
        # when
        self.test_object.reverse()
        # then
        assert_that(sorted(self.test_object.edges)).is_equal_to(
            [Edge(Vertex(1), Vertex(9)), Edge(Vertex(2), Vertex(1)), Edge(Vertex(2), Vertex(6)),
             Edge(Vertex(4), Vertex(5)), Edge(Vertex(5), Vertex(3)), Edge(Vertex(6), Vertex(6)),
             Edge(Vertex(6), Vertex(9)), Edge(Vertex(7), Vertex(5)), Edge(Vertex(8), Vertex(7)),
             Edge(Vertex(9), Vertex(4))])
        assert_that(self.test_object.properties[vertex]).is_equal_to(vertex_property)
        assert_that(self.test_object.properties[Vertex(9)]).is_none()
        assert_that(self.test_object.properties[self.test_object.get_edge(2, 1)]) \
            .is_equal_to(edge_property)
        assert_that(self.test_object.properties[self.test_object.get_edge(5, 3)]).is_none()

    def test__reversed_copy__then_new_graph_with_reversed_edges(self):
        # given
        vertex = Vertex(5)
        vertex_property = "123456"
        edge_property = "zxcvb"
        edge = self.test_object.add_edge_between(Vertex(1), Vertex(2))
        self.test_object.add_edge_between(Vertex(3), Vertex(5))
        self.test_object.add_edge_between(Vertex(4), Vertex(9))
        self.test_object.add_edge_between(Vertex(5), Vertex(4))
        self.test_object.add_edge_between(Vertex(5), Vertex(7))
        self.test_object.add_edge_between(Vertex(6), Vertex(2))
        self.test_object.add_edge_between(Vertex(6), Vertex(6))
        self.test_object.add_edge_between(Vertex(7), Vertex(8))
        self.test_object.add_edge_between(Vertex(9), Vertex(1))
        self.test_object.add_edge_between(Vertex(9), Vertex(6))
        self.test_object.properties[vertex] = vertex_property
        self.test_object.properties[edge] = edge_property
        # when
        result = self.test_object.reversed_copy()
        # then
        assert_that(sorted(result.vertices)).is_equal_to(sorted(self.test_object.vertices))
        assert_that(sorted(result.edges)).is_equal_to(
            [Edge(Vertex(1), Vertex(9)), Edge(Vertex(2), Vertex(1)), Edge(Vertex(2), Vertex(6)),
             Edge(Vertex(4), Vertex(5)), Edge(Vertex(5), Vertex(3)), Edge(Vertex(6), Vertex(6)),
             Edge(Vertex(6), Vertex(9)), Edge(Vertex(7), Vertex(5)), Edge(Vertex(8), Vertex(7)),
             Edge(Vertex(9), Vertex(4))])
        assert_that(result.properties[vertex]).is_equal_to(vertex_property)
        assert_that(result.properties[Vertex(9)]).is_none()
        assert_that(result.properties[result.get_edge(2, 1)]).is_equal_to(edge_property)
        assert_that(result.properties[result.get_edge(5, 3)]).is_none()
