# -*- coding: utf-8 -*-
"""TESTY DLA ALGORYTMU WYZNACZANIA SILNIE SPÓLJNYCH SKŁADOWYCH"""
import unittest
from algolib.graphs import find_scc, DirectedSimpleGraph


class PathsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__digraph = None

    def setUp(self):
        self.__digraph = DirectedSimpleGraph(10, [(0, 4), (0, 5), (1, 0), (2, 3),
                                                  (3, 1), (4, 1), (4, 3), (6, 5), (6, 9),
                                                  (7, 4), (7, 6), (8, 3), (8, 7), (9, 8)])

    def tearDown(self):
        self.__digraph = None

    def test_find_scc(self):
        result = find_scc(self.__digraph)

        self.assertEqual(4, len(result))
        self.assertIn({5}, result)
        self.assertIn({2}, result)
        self.assertIn({0, 1, 3, 4}, result)
        self.assertIn({6, 7, 8, 9}, result)
