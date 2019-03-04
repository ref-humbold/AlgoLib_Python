# -*- coding: utf-8 -*-
"""Test: directed graphs structures"""
import unittest
from algolib.graphs import DirectedSimpleGraph


class DirectedSimpleGraphTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__test_object = None

    def setUp(self):
        self.__test_object = DirectedSimpleGraph(10)

    def tearDown(self):
        self.__test_object = None

    def test_vertices_number(self):
        result = self.__test_object.vertices_number

        self.assertEqual(10, result)

    def test_get_vertices(self):
        result = self.__test_object.get_vertices()

        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                             sorted(result))

    def test_add_vertex(self):
        result = self.__test_object.add_vertex()

        self.assertEqual(10, result)
        self.assertEqual(11, self.__test_object.vertices_number)

    def test_edges_number(self):
        self.__test_object.add_edge(7, 7)
        self.__test_object.add_edge(1, 5)
        self.__test_object.add_edge(2, 4)
        self.__test_object.add_edge(8, 0)
        self.__test_object.add_edge(6, 3)
        self.__test_object.add_edge(3, 6)
        self.__test_object.add_edge(9, 3)
        self.__test_object.add_edge(8, 0)

        result = self.__test_object.edges_number

        self.assertEqual(7, result)

    def test_get_edges(self):
        self.__test_object.add_edge(7, 7)
        self.__test_object.add_edge(1, 5)
        self.__test_object.add_edge(2, 4)
        self.__test_object.add_edge(8, 0)
        self.__test_object.add_edge(6, 3)
        self.__test_object.add_edge(3, 6)
        self.__test_object.add_edge(9, 3)
        self.__test_object.add_edge(8, 0)

        result = self.__test_object.get_edges()

        self.assertListEqual([(1, 5), (2, 4), (3, 6), (6, 3), (7, 7), (8, 0), (9, 3)],
                             sorted(result))

    def test_add_edge(self):
        self.__test_object.add_edge(1, 5)
        self.__test_object.add_edge(1, 5)
        self.__test_object.add_edge(1, 1)

        self.assertEqual(2, self.__test_object.edges_number)
        self.assertListEqual([1, 5], sorted(self.__test_object.get_neighbours(1)))
        self.assertListEqual([], sorted(self.__test_object.get_neighbours(5)))

    def test_get_neighbours(self):
        self.__test_object.add_edge(1, 1)
        self.__test_object.add_edge(1, 3)
        self.__test_object.add_edge(1, 4)
        self.__test_object.add_edge(1, 7)
        self.__test_object.add_edge(1, 9)
        self.__test_object.add_edge(2, 1)
        self.__test_object.add_edge(6, 1)

        result = self.__test_object.get_neighbours(1)

        self.assertListEqual([1, 3, 4, 7, 9], sorted(result))

    def test_get_outdegree(self):
        self.__test_object.add_edge(1, 1)
        self.__test_object.add_edge(1, 3)
        self.__test_object.add_edge(1, 4)
        self.__test_object.add_edge(1, 7)
        self.__test_object.add_edge(1, 9)
        self.__test_object.add_edge(2, 1)
        self.__test_object.add_edge(6, 1)

        result = self.__test_object.get_outdegree(1)

        self.assertEqual(5, result)

    def test_get_indegree(self):
        self.__test_object.add_edge(1, 1)
        self.__test_object.add_edge(3, 1)
        self.__test_object.add_edge(4, 1)
        self.__test_object.add_edge(7, 1)
        self.__test_object.add_edge(9, 1)
        self.__test_object.add_edge(1, 2)
        self.__test_object.add_edge(1, 6)

        result = self.__test_object.get_indegree(1)

        self.assertEqual(5, result)

    def test_reverse(self):
        self.__test_object.add_edge(1, 2)
        self.__test_object.add_edge(3, 5)
        self.__test_object.add_edge(4, 9)
        self.__test_object.add_edge(5, 4)
        self.__test_object.add_edge(5, 7)
        self.__test_object.add_edge(6, 2)
        self.__test_object.add_edge(6, 6)
        self.__test_object.add_edge(7, 8)
        self.__test_object.add_edge(9, 1)
        self.__test_object.add_edge(9, 6)

        self.__test_object.reverse()

        self.assertListEqual([(1, 9), (2, 1), (2, 6), (4, 5), (5, 3), (6, 6), (6, 9),
                              (7, 5), (8, 7), (9, 4)], sorted(self.__test_object.get_edges()))
