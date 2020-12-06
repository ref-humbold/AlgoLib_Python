# -*- coding: utf-8 -*-
"""Tests: lowest common ancestor algorithm"""
import unittest

from algolib.graphs import TreeGraph
from algolib.graphs.algorithms import LowestCommonAncestor


class LCATest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        tree = TreeGraph(0)
        tree.add_vertex(1, 0)
        tree.add_vertex(2, 0)
        tree.add_vertex(3, 1)
        tree.add_vertex(4, 1)
        tree.add_vertex(5, 1)
        tree.add_vertex(6, 2)
        tree.add_vertex(7, 4)
        tree.add_vertex(8, 6)
        tree.add_vertex(9, 6)

        self.test_object = LowestCommonAncestor(tree, 0)

    def tearDown(self):
        self.test_object = None

    def test__find__when_same_vertex__then_vertex_is_lca(self):
        # given
        vertex = 6
        # when
        result = self.test_object.find(vertex, vertex)
        # then
        self.assertEqual(vertex, result)

    def test__find__when_vertices_in_different_subtrees__then_lca(self):
        # when
        result = self.test_object.find(5, 7)
        # then
        self.assertEqual(1, result)

    def test__find__when_vertices_swapped__then_same_lca(self):
        # when
        result1 = self.test_object.find(5, 7)
        result2 = self.test_object.find(7, 5)
        # then
        self.assertEqual(1, result1)
        self.assertEqual(result1, result2)

    def test__find__when_root_is_common_ancestor__then_root(self):
        # when
        result = self.test_object.find(3, 9)
        # then
        self.assertEqual(self.test_object.root, result)

    def test__find__when_vertices_are_offsprings__then_lca_is_closer_to_root(self):
        # given
        vertex1 = 8
        vertex2 = 2
        # when
        result = self.test_object.find(vertex1, vertex2)
        # then
        self.assertEqual(vertex2, result)

    def test__find__when_root_is_one_of_vertices__then_root(self):
        # when
        result = self.test_object.find(4, self.test_object.root)
        # then
        self.assertEqual(self.test_object.root, result)
