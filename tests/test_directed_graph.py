# -*- coding: utf-8 -*-
"""Tests: Structure of directed graphs"""
import unittest

from algolib.graphs import DirectedSimpleGraph


class DirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = DirectedSimpleGraph([None] * 10)

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
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [v.index for v in result])

    def test__add_vertex(self):
        # when
        result = self._test_object.add_vertex(None)
        # then
        self.assertEqual(10, result.index)
        self.assertIsNone(result.property)
        self.assertEqual(11, self._test_object.vertices_count)

    def test__edges_count(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(7), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(2), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(8), self._test_object.get_vertex(0),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(3), self._test_object.get_vertex(6),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(8), self._test_object.get_vertex(0),
                                   None)
        # when
        result = self._test_object.edges_count
        # then
        self.assertEqual(7, result)

    def test__edges(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(7), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(2), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(8), self._test_object.get_vertex(0),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(3), self._test_object.get_vertex(6),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(8), self._test_object.get_vertex(0),
                                   None)
        # when
        result = self._test_object.edges
        # then
        self.assertListEqual(
                [(self._test_object.get_vertex(1), self._test_object.get_vertex(5)),
                 (self._test_object.get_vertex(2), self._test_object.get_vertex(4)),
                 (self._test_object.get_vertex(3), self._test_object.get_vertex(6)),
                 (self._test_object.get_vertex(6), self._test_object.get_vertex(3)),
                 (self._test_object.get_vertex(7), self._test_object.get_vertex(7)),
                 (self._test_object.get_vertex(8), self._test_object.get_vertex(0)),
                 (self._test_object.get_vertex(9), self._test_object.get_vertex(3))],
                sorted([(e.source, e.destination) for e in result]))

    def test__add_edge(self):
        # when
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(1),
                                   None)
        # then
        self.assertEqual(2, self._test_object.edges_count)
        self.assertListEqual([self._test_object.get_vertex(1), self._test_object.get_vertex(5)],
                             sorted(self._test_object.get_neighbours(
                                     self._test_object.get_vertex(1))))
        self.assertListEqual([], sorted(self._test_object.get_neighbours(
                self._test_object.get_vertex(5))))

    def test__get_neighbours(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(9),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(2), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(1),
                                   None)
        # when
        result = self._test_object.get_neighbours(self._test_object.get_vertex(1))
        # then
        self.assertListEqual([self._test_object.get_vertex(1), self._test_object.get_vertex(3),
                              self._test_object.get_vertex(4), self._test_object.get_vertex(7),
                              self._test_object.get_vertex(9)], sorted(result))

    def test__get_output_degree(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(3),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(9),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(2), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(1),
                                   None)
        # when
        result = self._test_object.get_output_degree(self._test_object.get_vertex(1))
        # then
        self.assertEqual(5, result)

    def test__get_input_degree(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(3), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(4), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(7), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(2),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(6),
                                   None)
        # when
        result = self._test_object.get_input_degree(self._test_object.get_vertex(1))
        # then
        self.assertEqual(5, result)

    def test__reverse(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(2),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(3), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(4), self._test_object.get_vertex(9),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(5), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(5), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(2),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(6),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(7), self._test_object.get_vertex(8),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(6),
                                   None)
        # when
        self._test_object.reverse()
        # then
        self.assertListEqual([(self._test_object.get_vertex(1), self._test_object.get_vertex(9)),
                              (self._test_object.get_vertex(2), self._test_object.get_vertex(1)),
                              (self._test_object.get_vertex(2), self._test_object.get_vertex(6)),
                              (self._test_object.get_vertex(4), self._test_object.get_vertex(5)),
                              (self._test_object.get_vertex(5), self._test_object.get_vertex(3)),
                              (self._test_object.get_vertex(6), self._test_object.get_vertex(6)),
                              (self._test_object.get_vertex(6), self._test_object.get_vertex(9)),
                              (self._test_object.get_vertex(7), self._test_object.get_vertex(5)),
                              (self._test_object.get_vertex(8), self._test_object.get_vertex(7)),
                              (self._test_object.get_vertex(9), self._test_object.get_vertex(4))],
                             sorted([(edge.source, edge.destination)
                                     for edge in self._test_object.edges]))

    def test__reversed_copy(self):
        # given
        self._test_object.add_edge(self._test_object.get_vertex(1), self._test_object.get_vertex(2),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(3), self._test_object.get_vertex(5),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(4), self._test_object.get_vertex(9),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(5), self._test_object.get_vertex(4),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(5), self._test_object.get_vertex(7),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(2),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(6), self._test_object.get_vertex(6),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(7), self._test_object.get_vertex(8),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(1),
                                   None)
        self._test_object.add_edge(self._test_object.get_vertex(9), self._test_object.get_vertex(6),
                                   None)
        # when
        result = self._test_object.reversed_copy()
        # then
        self.assertListEqual(self._test_object.vertices, result.vertices)
        self.assertListEqual(
                [(self._test_object.get_vertex(1), self._test_object.get_vertex(9)),
                 (self._test_object.get_vertex(2), self._test_object.get_vertex(1)),
                 (self._test_object.get_vertex(2), self._test_object.get_vertex(6)),
                 (self._test_object.get_vertex(4), self._test_object.get_vertex(5)),
                 (self._test_object.get_vertex(5), self._test_object.get_vertex(3)),
                 (self._test_object.get_vertex(6), self._test_object.get_vertex(6)),
                 (self._test_object.get_vertex(6), self._test_object.get_vertex(9)),
                 (self._test_object.get_vertex(7), self._test_object.get_vertex(5)),
                 (self._test_object.get_vertex(8), self._test_object.get_vertex(7)),
                 (self._test_object.get_vertex(9), self._test_object.get_vertex(4))],
                sorted([(edge.source, edge.destination) for edge in result.edges]))
