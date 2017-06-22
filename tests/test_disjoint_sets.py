# -*- coding: utf-8 -*-
"""TESTY DLA STRUKTURY ZBIORÓW ROZŁĄCZNYCH"""
import unittest
from algolib.structures import DisjointSets


class DisjointSetsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__test_object = None

    def setUp(self):
        self.__test_object = DisjointSets(range(10))

    def tearDown(self):
        self.__test_object = None

    def test_len(self):
        result = len(self.__test_object)

        self.assertEqual(10, result)

    def test_in_when_contains(self):
        result = 4 in self.__test_object

        self.assertTrue(result)

    def test_in_when_not_contains(self):
        result = 17 in self.__test_object

        self.assertFalse(result)

    def test_make_set_when_new_element(self):
        elem = 20

        self.__test_object.make_set(elem)

        self.assertIn(elem, self.__test_object)
        self.assertEqual(elem, self.__test_object.find_set(elem))

    def test_make_set_when_present_element(self):
        elem = 7

        with self.assertRaises(ValueError):
            self.__test_object.make_set(elem)

    def test_find_set(self):
        elem = 4

        result = self.__test_object.find_set(elem)

        self.assertEqual(elem, result)

    def test_union_set_when_different_sets(self):
        elem1 = 4
        elem2 = 6

        self.__test_object.union_set(elem1, elem2)

        self.assertTrue(self.__test_object.is_same_set(elem1, elem2))
        self.assertEqual(self.__test_object.find_set(elem1), self.__test_object.find_set(elem2))

    def test_union_set_when_same_sets_1(self):
        elem = 4

        self.__test_object.union_set(elem, elem)

        self.assertTrue(self.__test_object.is_same_set(elem, elem))
        self.assertEqual(self.__test_object.find_set(elem), self.__test_object.find_set(elem))

    def test_union_set_when_same_sets_2(self):
        elem1 = 3
        elem2 = 8

        self.__test_object.union_set(elem1, elem2)
        self.__test_object.union_set(elem2, elem1)

        self.assertTrue(self.__test_object.is_same_set(elem1, elem2))
        self.assertEqual(self.__test_object.find_set(elem1), self.__test_object.find_set(elem2))

    def test_is_same_set_when_different_sets(self):
        elem1 = 4
        elem2 = 6

        result = self.__test_object.is_same_set(elem1, elem2)

        self.assertFalse(result)

    def test_is_same_set_when_same_set_1(self):
        elem = 4

        result = self.__test_object.is_same_set(elem, elem)

        self.assertTrue(result)

    def test_is_same_set_when_same_sets_2(self):
        elem1 = 3
        elem2 = 8

        self.__test_object.union_set(elem1, elem2)
        result = self.__test_object.is_same_set(elem1, elem2)

        self.assertTrue(result)
