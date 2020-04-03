# -*- coding: utf-8 -*-
"""Tests: Strongly connected components algorithm"""
import unittest

from algolib.graphs import DirectedSimpleGraph
from algolib.graphs.algorithms import find_scc


class SCCTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__find_scc(self):
        digraph = DirectedSimpleGraph(10, [(0, 4), (0, 5), (1, 0), (2, 3), (3, 1), (4, 1), (4, 3),
                                           (6, 5), (6, 9), (7, 4), (7, 6), (8, 3), (8, 7), (9, 8)])

        result = find_scc(digraph)

        self.assertEqual(4, len(result))
        self.assertIn({5}, result)
        self.assertIn({2}, result)
        self.assertIn({0, 1, 3, 4}, result)
        self.assertIn({6, 7, 8, 9}, result)
