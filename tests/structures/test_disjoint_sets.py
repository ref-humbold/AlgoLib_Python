# -*- coding: utf-8 -*-
"""Tests: Structure of disjoint sets  (union-find)"""
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

    def test__len__then_sets_count(self):
        # when
        result = len(self._test_object)
        # then
        self.assertEqual(10, result)

    def test__in__when_present__then_true(self):
        # when
        result = 4 in self._test_object
        # then
        self.assertTrue(result)

    def test__in__when_absent__then_false(self):
        # when
        result = 17 in self._test_object
        # then
        self.assertFalse(result)

    def test__iadd__when_new_elements__then_singleton_sets(self):
        # given
        elems = [14, 18, 23]
        # when
        self._test_object += elems
        # then
        for elem in elems:
            self.assertIn(elem, self._test_object)
            self.assertEqual(elem, self._test_object.find_set(elem))

    def test__iadd__when_present_element__then_value_error(self):
        # when - then
        with self.assertRaises(ValueError):
            self._test_object += [11, 7, 15]

    def test__getitem__when_present_element__then_represent(self):
        # given
        elem = 4
        # when
        result = self._test_object[elem]
        # then
        self.assertEqual(elem, result)

    def test__getitem__when_absent_element__then_key_error(self):
        # when - then
        with self.assertRaises(KeyError):
            _ = self._test_object[18]

    def test__find_set__when_present_element__then_represent(self):
        # given
        elem = 4
        # when
        result = self._test_object.find_set(elem, 10)
        # then
        self.assertEqual(elem, result)

    def test__find_set__when_absent_element__then_default(self):
        # given
        default = 0
        # when
        result = self._test_object.find_set(22, default)
        # then
        self.assertEqual(default, result)

    def test__find_set__when_absent_element_and_no_default__then_none(self):
        # when
        result = self._test_object.find_set(12)
        # then
        self.assertEqual(None, result)

    def test__union_set__when_different_sets__then_same_represent(self):
        # given
        elem1 = 4
        elem2 = 6
        # when
        self._test_object.union_set(elem1, elem2)
        # then
        self.assertTrue(self._test_object.is_same_set(elem1, elem2))
        self.assertEqual(self._test_object[elem1], self._test_object[elem2])

    def test__union_set__when_same_element__then_same_represent(self):
        # given
        elem = 4
        # when
        self._test_object.union_set(elem, elem)
        # then
        self.assertTrue(self._test_object.is_same_set(elem, elem))
        self.assertEqual(self._test_object[elem], self._test_object[elem])

    def test__union_set__when_elements_in_one_set__then_same_represent(self):
        # given
        elem1 = 3
        elem2 = 8
        self._test_object.union_set(elem1, elem2)
        # when
        self._test_object.union_set(elem2, elem1)
        # then
        self.assertTrue(self._test_object.is_same_set(elem1, elem2))
        self.assertEqual(self._test_object[elem1], self._test_object[elem2])

    def test__union_set__when_absent_element__then_key_error(self):
        # when - then
        with self.assertRaises(KeyError):
            self._test_object.union_set(15, 6)

    def test__union_set__when_new_elements_in_chain__then_same_represent(self):
        # given
        elems = [20, 17, 35]
        # when
        self._test_object.add(*elems).union_set(elems[0], elems[1]).union_set(elems[1], elems[2])
        # then
        self.assertTrue(self._test_object.is_same_set(elems[0], elems[2]))
        self.assertEqual(self._test_object[elems[0]], self._test_object[elems[2]])

    def test__is_same_set__when_different_sets__then_false(self):
        # when
        result = self._test_object.is_same_set(4, 6)
        # then
        self.assertFalse(result)

    def test__is_same_set__when_same_element__then_true(self):
        # when
        result = self._test_object.is_same_set(4, 4)
        # then
        self.assertTrue(result)

    def test__is_same_set__when_same_set__then_true(self):
        # given
        elem1 = 3
        elem2 = 8
        self._test_object.union_set(elem1, elem2)
        # when
        result = self._test_object.is_same_set(elem1, elem2)
        # then
        self.assertTrue(result)

    def test__is_same_set__when_absent__then_key_error(self):
        # then
        with self.assertRaises(KeyError):
            # when
            self._test_object.is_same_set(15, 6)
