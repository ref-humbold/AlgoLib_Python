# -*- coding: utf-8 -*-
"""Tests: Structure of double heap"""
import unittest

from algolib.structures import DoubleHeap


class DoubleHeapTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self._test_object = None

    def setUp(self):
        self._test_object = DoubleHeap(self._numbers)

    def tearDown(self):
        self._test_object = None

    def test__len__when_empty__then_zero(self):
        self._test_object = DoubleHeap()
        # when
        result = len(self._test_object)
        # then
        self.assertEqual(0, result)

    def test__len__when_not_empty__then_number_of_elements(self):
        # when
        result = len(self._test_object)
        # then
        self.assertEqual(len(self._numbers), result)

    def test_left__when_empty__then_key_error(self):
        # given
        self._test_object = DoubleHeap()
        # then
        with self.assertRaises(KeyError):
            # when
            _ = self._test_object.left

    def test_left__when_not_empty__then_minimal_element(self):
        # when
        result = self._test_object.left
        # then
        self.assertEqual(min(self._numbers), result)

    def test_right__when_empty__then_key_error(self):
        # given
        self._test_object = DoubleHeap()
        # then
        with self.assertRaises(KeyError):
            # when
            _ = self._test_object.right

    def test_right__when_single_element__then_this_element(self):
        # given
        element = 19
        self._test_object = DoubleHeap([element])
        # when
        result = self._test_object.right
        # then
        self.assertEqual(element, result)

    def test_right__when_multiple_elements__then_maximal_element(self):
        # when
        result = self._test_object.right
        # then
        self.assertEqual(max(self._numbers), result)

    def test_push__when_empty__then_added(self):
        # given
        element = 19
        self._test_object = DoubleHeap()
        # when
        self._test_object.push(element)
        # then
        self.assertEqual(1, len(self._test_object))
        self.assertEqual(element, self._test_object.left)
        self.assertEqual(element, self._test_object.right)

    def test_push__when_new_element_is_less__then_added_to_left(self):
        # given
        element = min(self._numbers) - 1
        # when
        self._test_object.push(element)
        # then
        self.assertEqual(len(self._numbers) + 1, len(self._test_object))
        self.assertEqual(element, self._test_object.left)

    def test_push__when_new_element_is_greater__then_added_to_right(self):
        # given
        element = max(self._numbers) + 1
        # when
        self._test_object.push(element)
        # then
        self.assertEqual(len(self._numbers) + 1, len(self._test_object))
        self.assertEqual(element, self._test_object.right)

    def test_push__when_new_element__then_added(self):
        # when
        self._test_object.push(46)
        # then
        self.assertEqual(len(self._numbers) + 1, len(self._test_object))
        self.assertEqual(min(self._numbers), self._test_object.left)
        self.assertEqual(max(self._numbers), self._test_object.right)

    def test_popleft__when_empty__then_key_error(self):
        # given
        self._test_object = DoubleHeap()
        # then
        with self.assertRaises(KeyError):
            # when
            _ = self._test_object.popleft()

    def test_popleft__when_not_empty__then_minimal_element_removed(self):
        # when
        result = self._test_object.popleft()
        # then
        self.assertEqual(len(self._numbers) - 1, len(self._test_object))
        self.assertEqual(min(self._numbers), result)

    def test_popleft__when_single_element__then_this_element_removed(self):
        # given
        element = 19
        self._test_object = DoubleHeap([element])
        # when
        result = self._test_object.popleft()
        # then
        self.assertEqual(0, len(self._test_object))
        self.assertEqual(element, result)

    def test_popright__when_empty__then_key_error(self):
        # given
        self._test_object = DoubleHeap()
        # then
        with self.assertRaises(KeyError):
            # when
            _ = self._test_object.popright()

    def test_popleft__when_multiple_calls__then_sorted_ascending(self):
        # when
        result = []

        while len(self._test_object) > 0:
            result.append(self._test_object.popleft())

        # then
        self.assertListEqual(sorted(self._numbers), result)

    def test_popright__when_single_element__then_this_element_removed(self):
        # given
        element = 19
        self._test_object = DoubleHeap([element])
        # when
        result = self._test_object.popright()
        # then
        self.assertEqual(0, len(self._test_object))
        self.assertEqual(element, result)

    def test_popright__when_multiple_elements__then_maximal_element_removed(self):
        # when
        result = self._test_object.popright()
        # then
        self.assertEqual(len(self._numbers) - 1, len(self._test_object))
        self.assertEqual(max(self._numbers), result)

    def test_popright__when_multiple_calls__then_sorted_descending(self):
        # when
        result = []

        while len(self._test_object) > 0:
            result.append(self._test_object.popright())

        # then
        self.assertListEqual(sorted(self._numbers, key=lambda x: -x), result)

    def test_clear__when_not_empty__then_empty(self):
        # when
        self._test_object.clear()
        # then
        self.assertEqual(0, len(self._test_object))
