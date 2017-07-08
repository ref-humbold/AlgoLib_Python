# -*- coding: utf-8 -*-
"""TESTY DLA DRZEWA AVL"""
import unittest
from algolib.structures import AVLTree


class AVLTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__test_object = None
        self.__numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]

    def setUp(self):
        self.__test_object = AVLTree(self.__numbers)

    def tearDown(self):
        self.__test_object = None

    def test_str(self):
        result = str(self.__test_object)

        self.assertEqual("{|2, 6, 10, 14, 18, 24, 26, 30, 37, 45, 51, 68, 71, 97|}", result)

    def test_empty_when_empty(self):
        self.__test_object = AVLTree()

        result = self.__test_object.empty()

        self.assertTrue(result)

    def test_empty_when_not_empty(self):
        result = self.__test_object.empty()

        self.assertFalse(result)

    def test_len_when_empty(self):
        self.__test_object = AVLTree()

        result = len(self.__test_object)

        self.assertEqual(0, result)

    def test_len_when_not_empty(self):
        result = len(self.__test_object)

        self.assertEqual(len(self.__numbers), result)

    def test_in_when_present_element(self):
        for i in self.__numbers:
            result = i in self.__test_object

            self.assertTrue(result)

    def test_in_when_outer_element(self):
        for i in [111, 140, 187]:
            result = i in self.__test_object

            self.assertFalse(result)

    def test_iterator(self):
        result = []

        iterator = iter(self.__test_object)

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break

        self.assertListEqual(sorted(self.__numbers), result)

    def test_reversed(self):
        result = []

        iterator = reversed(self.__test_object)

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break

        self.assertListEqual(sorted(self.__numbers, reverse=True), result)

    def test_add_when_new_element(self):
        for i in [111, 140, 187]:
            result = self.__test_object.add(i)

            self.assertTrue(result)
            self.assertIn(i, self.__test_object)

    def test_add_when_present_element(self):
        for i in [14, 24, 30, 45]:
            result = self.__test_object.add(i)

            self.assertFalse(result)
            self.assertIn(i, self.__test_object)

    def test_remove_when_present_element(self):
        for i in [14, 24, 30, 45]:
            result = self.__test_object.remove(i)

            self.assertTrue(result)
            self.assertNotIn(i, self.__test_object)

    def test_remove_root_when_two_elements1(self):
        root = 27
        elem = 11

        self.__test_object = AVLTree([root, elem])

        result = self.__test_object.remove(root)

        self.assertTrue(result)
        self.assertNotIn(root, self.__test_object)
        self.assertIn(elem, self.__test_object)

    def test_remove_root_when_two_elements2(self):
        root = 11
        elem = 27
        self.__test_object = AVLTree([root, elem])

        result = self.__test_object.remove(root)

        self.assertTrue(result)
        self.assertNotIn(root, self.__test_object)
        self.assertIn(elem, self.__test_object)

    def test_remove_root_when_one_element(self):
        root = 0
        self.__test_object = AVLTree([root])

        result = self.__test_object.remove(root)

        self.assertTrue(result)
        self.assertNotIn(root, self.__test_object)
        self.assertTrue(self.__test_object.empty())

    def test_remove_when_empty(self):
        self.__test_object = AVLTree()

        result = self.__test_object.remove(0)

        self.assertFalse(result)
        self.assertTrue(self.__test_object.empty())

    def test_remove_when_outer_element(self):
        for i in [111, 140, 187]:
            result = self.__test_object.remove(i)

            self.assertFalse(result)
            self.assertNotIn(i, self.__test_object)

    def test_clear(self):
        self.__test_object.clear()

        self.assertTrue(self.__test_object.empty())
