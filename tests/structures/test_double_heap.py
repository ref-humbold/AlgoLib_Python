# -*- coding: utf-8 -*-
"""Tests: Structure of double heap"""
import unittest

from assertpy import assert_that

from algolib.structures import DoubleHeap


class DoubleHeapTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.test_object = None

    def setUp(self):
        self.test_object = DoubleHeap(self._numbers)

    def test__len__when_empty__then_zero(self):
        self.test_object = DoubleHeap()
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(0)

    def test__len__when_not_empty__then_number_of_elements(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(len(self._numbers))

    @staticmethod
    def test__left__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.left

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__left__when_not_empty__then_minimal_element(self):
        # when
        result = self.test_object.left
        # then
        assert_that(result).is_equal_to(min(self._numbers))

    @staticmethod
    def test__right__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.right

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__right__when_single_element__then_this_element(self):
        # given
        element = 19
        self.test_object = DoubleHeap([element])
        # when
        result = self.test_object.right
        # then
        assert_that(result).is_equal_to(element)

    def test__right__when_multiple_elements__then_maximal_element(self):
        # when
        result = self.test_object.right
        # then
        assert_that(result).is_equal_to(max(self._numbers))

    def test__push__when_empty__then_added(self):
        # given
        element = 19
        self.test_object = DoubleHeap()
        # when
        self.test_object.push(element)
        # then
        assert_that(self.test_object).is_length(1)
        assert_that(self.test_object.left).is_equal_to(element)
        assert_that(self.test_object.right).is_equal_to(element)

    def test__push__when_new_element_is_less__then_added_to_left(self):
        # given
        element = min(self._numbers) - 1
        # when
        self.test_object.push(element)
        # then
        assert_that(self.test_object).is_length(len(self._numbers) + 1)
        assert_that(self.test_object.left).is_equal_to(element)

    def test__push__when_new_element_is_greater__then_added_to_right(self):
        # given
        element = max(self._numbers) + 1
        # when
        self.test_object.push(element)
        # then
        assert_that(self.test_object).is_length(len(self._numbers) + 1)
        assert_that(self.test_object.right).is_equal_to(element)

    def test__push__when_new_element__then_added(self):
        # when
        self.test_object.push(46)
        # then
        assert_that(self.test_object).is_length(len(self._numbers) + 1)
        assert_that(self.test_object.left).is_equal_to(min(self._numbers))
        assert_that(self.test_object.right).is_equal_to(max(self._numbers))

    @staticmethod
    def test__popleft__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.popleft()

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__popleft__when_single_element__then_this_element_removed(self):
        # given
        element = 19
        self.test_object = DoubleHeap([element])
        # when
        result = self.test_object.popleft()
        # then
        assert_that(self.test_object).is_empty()
        assert_that(result).is_equal_to(element)

    def test__popleft__when_multiple_elements__then_minimal_element_removed(self):
        # when
        result = self.test_object.popleft()
        # then
        assert_that(self.test_object).is_length(len(self._numbers) - 1)
        assert_that(result).is_equal_to(min(self._numbers))

    def test__popleft__when_multiple_calls__then_sorted_ascending(self):
        # when
        result = []

        while len(self.test_object) > 0:
            result.append(self.test_object.popleft())

        # then
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(self._numbers))

    @staticmethod
    def test__popright__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.popright()

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__popright__when_single_element__then_this_element_removed(self):
        # given
        element = 19
        self.test_object = DoubleHeap([element])
        # when
        result = self.test_object.popright()
        # then
        assert_that(self.test_object).is_empty()
        assert_that(result).is_equal_to(element)

    def test__popright__when_multiple_elements__then_maximal_element_removed(self):
        # when
        result = self.test_object.popright()
        # then
        assert_that(self.test_object).is_length(len(self._numbers) - 1)
        assert_that(result).is_equal_to(max(self._numbers))

    def test__popright__when_multiple_calls__then_sorted_descending(self):
        # when
        result = []

        while len(self.test_object) > 0:
            result.append(self.test_object.popright())

        # then
        assert_that(result).is_sorted(key=lambda x: -x)
        assert_that(result).is_equal_to(sorted(self._numbers, key=lambda x: -x))

    def test__clear__when_not_empty__then_empty(self):
        # when
        self.test_object.clear()
        # then
        assert_that(self.test_object).is_empty()
