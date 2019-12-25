# -*- coding: utf-8 -*-
"""Tests: AVL tree structure."""
import unittest

from algolib.structures import AVLTree


class AVLTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_object = None
        self._numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]

    def setUp(self):
        self._test_object = AVLTree(self._numbers)

    def tearDown(self):
        self._test_object = None

    def test__str__then_text_representation(self):
        result = str(self._test_object)

        self.assertEqual("{|2, 6, 10, 14, 18, 24, 26, 30, 37, 45, 51, 68, 71, 97|}", result)

    def test__empty__when_empty__then_true(self):
        self._test_object = AVLTree()

        result = self._test_object.empty()

        self.assertTrue(result)

    def test__empty__when_not_empty__then_false(self):
        result = self._test_object.empty()

        self.assertFalse(result)

    def test__len__when_empty__then_zero(self):
        self._test_object = AVLTree()

        result = len(self._test_object)

        self.assertEqual(0, result)

    def test__len__when_not_empty__then_number_of_elements(self):
        result = len(self._test_object)

        self.assertEqual(len(self._numbers), result)

    def test__in__when_present_element__then_true(self):
        for i in self._numbers:
            result = i in self._test_object

            self.assertTrue(result)

    def test__in__when_outer_element(self):
        for i in [111, 140, 187]:
            result = i in self._test_object

            self.assertFalse(result)

    def test__iterator__then_ordered_elements(self):
        result = []

        iterator = iter(self._test_object)

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break

        self.assertListEqual(sorted(self._numbers), result)

    def test__reversed__then_reverse_ordered_elements(self):
        result = []

        iterator = reversed(self._test_object)

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break

        self.assertListEqual(sorted(self._numbers, reverse=True), result)

    def test__add__when_new_element__then_increase_length(self):
        for i, e in enumerate([111, 140, 187], start=1):
            self._test_object.add(e)

            self.assertIn(e, self._test_object)
            self.assertEqual(len(self._numbers) + i, len(self._test_object))

    def test__add__when_present_element__then_same_length(self):
        for e in [14, 24, 30, 45]:
            self._test_object.add(e)

            self.assertIn(e, self._test_object)
            self.assertEqual(len(self._numbers), len(self._test_object))

    def test__remove__when_present_element__then_not_in(self):
        for i in [14, 24, 30, 45]:
            self._test_object.remove(i)

            self.assertNotIn(i, self._test_object)

    def test__remove_root__when_two_elements__then_root_not_in__1(self):
        root = 27
        elem = 11

        self._test_object = AVLTree([root, elem])

        self._test_object.remove(root)

        self.assertNotIn(root, self._test_object)
        self.assertIn(elem, self._test_object)

    def test__remove_root__when_two_elements__then_root_not_in__2(self):
        root = 11
        elem = 27
        self._test_object = AVLTree([root, elem])

        self._test_object.remove(root)

        self.assertNotIn(root, self._test_object)
        self.assertIn(elem, self._test_object)

    def test__remove_root__when_one_element__then_empty(self):
        root = 0
        self._test_object = AVLTree([root])

        self._test_object.remove(root)

        self.assertNotIn(root, self._test_object)
        self.assertTrue(self._test_object.empty())

    def test__remove__when_empty__then_value_error(self):
        self._test_object = AVLTree()

        with self.assertRaises(ValueError):
            self._test_object.remove(0)

        self.assertTrue(self._test_object.empty())

    def test__remove__when_outer_element__then_value_error(self):
        for e in [111, 140, 187]:
            with self.assertRaises(ValueError):
                self._test_object.remove(e)

            self.assertNotIn(e, self._test_object)

    def test__clear__then_empty(self):
        self._test_object.clear()

        self.assertTrue(self._test_object.empty())
