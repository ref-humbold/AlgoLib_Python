# -*- coding: utf-8 -*-
import unittest

from assertpy import assert_that

from algolib.graphs import TreeGraph
from algolib.graphs.algorithms import count_diameter


class TreeDiameterTest(unittest.TestCase):
    @staticmethod
    def test__count_diameter__when_one_vertex__then_zero():
        # given
        tree = TreeGraph(0)

        # when
        result = count_diameter(tree)

        # then
        assert_that(result).is_zero()

    def test__count_diameter__when_all_weights_equal__then_diameter_length(self):
        # given
        weight = self._Weight(1)
        tree = TreeGraph(0)
        tree.add_vertex(1, tree.get_vertex(0), None, weight)
        tree.add_vertex(2, tree.get_vertex(0), None, weight)
        tree.add_vertex(3, tree.get_vertex(1), None, weight)
        tree.add_vertex(4, tree.get_vertex(1), None, weight)
        tree.add_vertex(5, tree.get_vertex(1), None, weight)
        tree.add_vertex(6, tree.get_vertex(2), None, weight)
        tree.add_vertex(7, tree.get_vertex(4), None, weight)
        tree.add_vertex(8, tree.get_vertex(6), None, weight)
        tree.add_vertex(9, tree.get_vertex(6), None, weight)

        # when
        result = count_diameter(tree)

        # then
        assert_that(result).is_equal_to(6)

    def test__count_diameter__when_edge_with_big_weight__then_longest_path(self):
        # given
        tree = TreeGraph(0)
        tree.add_vertex(1, tree.get_vertex(0), None, self._Weight(1000))
        tree.add_vertex(2, tree.get_vertex(1), None, self._Weight(10))
        tree.add_vertex(3, tree.get_vertex(1), None, self._Weight(10))
        tree.add_vertex(4, tree.get_vertex(2), None, self._Weight(5))
        tree.add_vertex(5, tree.get_vertex(3), None, self._Weight(5))

        # when
        result = count_diameter(tree)

        # then
        assert_that(result).is_equal_to(1015)

    class _Weight:
        def __init__(self, weight):
            self.weight = weight
