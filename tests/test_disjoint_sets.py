# -*- coding: utf-8 -*-
"""TEST : Disjoint sets structure (union-find)."""
import unittest

from algolib.structures import DisjointSets


class DisjointSetsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None

    def setUp(self):
        self._test_object = DisjointSets(range(10))

    def tearDown(self):
        self._test_object = None

    def test_len(self):
        result = len(self._test_object)

        self.assertEqual(10, result)

    def test_in_when_contains(self):
        result = 4 in self._test_object

        self.assertTrue(result)

    def test_in_when_not_contains(self):
        result = 17 in self._test_object

        self.assertFalse(result)

    def test_add_elem_when_new_element(self):
        elem = 20

        self._test_object.add_elem(elem)

        self.assertIn(elem, self._test_object)
        self.assertEqual(elem, self._test_object.find_set(elem))

    def test_add_elem_when_present_element(self):
        with self.assertRaises(ValueError):
            self._test_object.add_elem(7)

    def test_find_set(self):
        elem = 4

        result = self._test_object.find_set(elem)

        self.assertEqual(elem, result)

    def test_union_set_when_different_sets(self):
        elem1 = 4
        elem2 = 6

        self._test_object.union_set(elem1, elem2)

        self.assertTrue(self._test_object.is_same_set(elem1, elem2))
        self.assertEqual(self._test_object.find_set(elem1), self._test_object.find_set(elem2))

    def test_union_set_when_same_sets_1(self):
        elem = 4

        self._test_object.union_set(elem, elem)

        self.assertTrue(self._test_object.is_same_set(elem, elem))
        self.assertEqual(self._test_object.find_set(elem), self._test_object.find_set(elem))

    def test_union_set_when_same_sets_2(self):
        elem1 = 3
        elem2 = 8

        self._test_object.union_set(elem1, elem2)
        self._test_object.union_set(elem2, elem1)

        self.assertTrue(self._test_object.is_same_set(elem1, elem2))
        self.assertEqual(self._test_object.find_set(elem1), self._test_object.find_set(elem2))

    def test_is_same_set_when_different_sets(self):
        elem1 = 4
        elem2 = 6

        result = self._test_object.is_same_set(elem1, elem2)

        self.assertFalse(result)

    def test_is_same_set_when_same_set_1(self):
        elem = 4

        result = self._test_object.is_same_set(elem, elem)

        self.assertTrue(result)

    def test_is_same_set_when_same_sets_2(self):
        elem1 = 3
        elem2 = 8

        self._test_object.union_set(elem1, elem2)
        result = self._test_object.is_same_set(elem1, elem2)

        self.assertTrue(result)
