# -*- coding: utf-8 -*-
"""Tests: lowest common ancestor algorithm."""
import unittest

from assertpy import assert_that

from algolib.graphs import TreeGraph
from algolib.graphs.algorithms import LowestCommonAncestor


class LowestCommonAncestorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        tree = TreeGraph(0)
        tree.add_vertex(1, tree.get_vertex(0))
        tree.add_vertex(2, tree.get_vertex(0))
        tree.add_vertex(3, tree.get_vertex(1))
        tree.add_vertex(4, tree.get_vertex(1))
        tree.add_vertex(5, tree.get_vertex(1))
        tree.add_vertex(6, tree.get_vertex(2))
        tree.add_vertex(7, tree.get_vertex(4))
        tree.add_vertex(8, tree.get_vertex(6))
        tree.add_vertex(9, tree.get_vertex(6))

        self.test_object = LowestCommonAncestor(tree, tree.get_vertex(0))

    def test__find_lca__when_same_vertex__then_vertex_is_lca(self):
        # given
        vertex = self.test_object.tree.get_vertex(6)
        # when
        result = self.test_object.find_lca(vertex, vertex)
        # then
        assert_that(result).is_equal_to(vertex)

    def test__find_lca__when_vertices_in_different_subtrees__then_lca(self):
        # when
        result = self.test_object.find_lca(self.test_object.tree.get_vertex(5),
                                           self.test_object.tree.get_vertex(7))
        # then
        assert_that(result).is_equal_to(self.test_object.tree.get_vertex(1))

    def test__find_lca__when_vertices_swapped__then_same_lca(self):
        # when
        result1 = self.test_object.find_lca(self.test_object.tree.get_vertex(5),
                                            self.test_object.tree.get_vertex(7))
        result2 = self.test_object.find_lca(self.test_object.tree.get_vertex(7),
                                            self.test_object.tree.get_vertex(5))
        # then
        assert_that(result1).is_equal_to(self.test_object.tree.get_vertex(1))
        assert_that(result2).is_equal_to(result1)

    def test__find_lca__when_root_is_common_ancestor__then_root(self):
        # when
        result = self.test_object.find_lca(self.test_object.tree.get_vertex(3),
                                           self.test_object.tree.get_vertex(9))
        # then
        assert_that(result).is_equal_to(self.test_object.root)

    def test__find_lca__when_vertices_are_offsprings__then_lca_is_closer_to_root(self):
        # given
        vertex1 = self.test_object.tree.get_vertex(8)
        vertex2 = self.test_object.tree.get_vertex(2)
        # when
        result = self.test_object.find_lca(vertex1, vertex2)
        # then
        assert_that(result).is_equal_to(vertex2)

    def test__find_lca__when_root_is_one_of_vertices__then_root(self):
        # when
        result = self.test_object.find_lca(self.test_object.tree.get_vertex(4),
                                           self.test_object.root)
        # then
        assert_that(result).is_equal_to(self.test_object.root)
