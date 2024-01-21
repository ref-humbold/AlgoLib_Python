# -*- coding: utf-8 -*-
"""Tests: Algorithms for topological sorting."""
import unittest

from assertpy import assert_that

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.algorithms import DirectedCyclicGraphError, dfs_topological_sort, \
    inputs_topological_sort


class TopologicalSortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # region inputs_topological_sort

    @staticmethod
    def test__inputs_topological_sort__when_acyclic_graph__then_topological_order():
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(4))
        # when
        result = inputs_topological_sort(graph)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to(
            [graph.get_vertex(3), graph.get_vertex(5), graph.get_vertex(1), graph.get_vertex(0),
             graph.get_vertex(2), graph.get_vertex(4)])

    @staticmethod
    def test__inputs_topological_sort__when_cyclic_graph__then_directed_cyclic_graph_error():
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(2), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(4))

        # when
        def function(graph_):
            inputs_topological_sort(graph_)

        # then
        assert_that(function).raises(DirectedCyclicGraphError).when_called_with(graph)

    @staticmethod
    def test__inputs_topological_sort__when_empty_graph__then_vertices():
        # given
        graph = DirectedSimpleGraph(range(6))
        # when
        result = inputs_topological_sort(graph)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to(sorted(graph.vertices))

    # endregion
    # region dfs_topological_sort

    @staticmethod
    def test__dfs_topological_sort__when_acyclic_graph__then_topological_order():
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(4))
        # when
        result = dfs_topological_sort(graph)
        # then
        assert_that(result).is_instance_of(list)

        assert_that(result).is_in([
            graph.get_vertex(5),
            graph.get_vertex(3),
            graph.get_vertex(1),
            graph.get_vertex(0),
            graph.get_vertex(4),
            graph.get_vertex(2)], [
            graph.get_vertex(3),
            graph.get_vertex(5),
            graph.get_vertex(1),
            graph.get_vertex(0),
            graph.get_vertex(2),
            graph.get_vertex(4)], [
            graph.get_vertex(5),
            graph.get_vertex(3),
            graph.get_vertex(1),
            graph.get_vertex(0),
            graph.get_vertex(2),
            graph.get_vertex(4)], [
            graph.get_vertex(3),
            graph.get_vertex(5),
            graph.get_vertex(1),
            graph.get_vertex(0),
            graph.get_vertex(4),
            graph.get_vertex(2)])

    @staticmethod
    def test__dfs_topological_sort__when_cyclic_graph__then_directed_cyclic_graph_error():
        # given
        graph = DirectedSimpleGraph(range(6))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(0), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(1), graph.get_vertex(4))
        graph.add_edge_between(graph.get_vertex(2), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(0))
        graph.add_edge_between(graph.get_vertex(3), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(1))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(2))
        graph.add_edge_between(graph.get_vertex(5), graph.get_vertex(4))

        # when
        def function(graph_):
            dfs_topological_sort(graph_)

        # then
        assert_that(function).raises(DirectedCyclicGraphError).when_called_with(graph)

    @staticmethod
    def test__dfs_topological_sort__when_empty_graph__then_vertices():
        # given
        graph = DirectedSimpleGraph(range(6))
        # when
        result = dfs_topological_sort(graph)
        # then
        assert_that(result).is_instance_of(list)
        assert_that(result).is_equal_to(sorted(graph.vertices))

    # endregion
