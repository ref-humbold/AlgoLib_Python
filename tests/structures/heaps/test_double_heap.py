# -*- coding: utf-8 -*-
"""Tests: Structure of double heap."""
import unittest

from assertpy import assert_that

from algolib.structures.heaps import DoubleHeap


class DoubleHeapTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.minimum = min(self.numbers)
        self.maximum = max(self.numbers)
        self.test_object = None

    def setUp(self):
        self.test_object = DoubleHeap(self.numbers)

    @staticmethod
    def test__op_len__when_empty__then_zero():
        # when
        result = len(DoubleHeap())
        # then
        assert_that(result).is_equal_to(0)

    def test__op_len__when_not_empty__then_number_of_elements(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(len(self.numbers))

    def test__clear__when_not_empty__then_empty(self):
        # when
        self.test_object.clear()
        # then
        assert_that(self.test_object).is_empty()

    # region op_iter & op_reversed

    @staticmethod
    def test__op_iter__when_empty__then_no_elements():
        # when
        result = list(DoubleHeap())
        # then
        assert_that(result).is_empty()

    def test__op_iter__when_single_element__then_this_element_only(self):
        # given
        element = self.numbers[0]
        # when
        iterator = iter(DoubleHeap([element]))
        # then
        assert_that(next(iterator)).is_equal_to(element)
        assert_that(next).raises(StopIteration).when_called_with(iterator)

    def test__op_iter__when_multiple_elements__then_all_elements_minimum_first_maximum_last(self):
        # when
        result = list(self.test_object)
        # then
        assert_that(result).is_length(len(self.numbers))
        assert_that(result).contains_only(*self.numbers)
        assert_that(result[0]).is_equal_to(self.minimum)
        assert_that(result[-1]).is_equal_to(self.maximum)

    @staticmethod
    def test__op_reversed__when_empty__then_no_elements():
        # when
        result = list(reversed(DoubleHeap()))
        # then
        assert_that(result).is_empty()

    def test__op_reversed__when_single_element__then_this_element_only(self):
        # given
        element = self.numbers[0]
        # when
        iterator = reversed(DoubleHeap([element]))
        # then
        assert_that(next(iterator)).is_equal_to(element)
        assert_that(next).raises(StopIteration).when_called_with(iterator)

    def test__op_reversed__when_multiple_elements__then_all_elements_maximum_first_minimum_last(
        self):
        # when
        result = list(reversed(self.test_object))
        # then
        assert_that(result).is_length(len(self.numbers))
        assert_that(result).contains_only(*self.numbers)
        assert_that(result[0]).is_equal_to(self.maximum)
        assert_that(result[-1]).is_equal_to(self.minimum)

    # endregion
    # region append

    def test__append__when_empty__then_added(self):
        # given
        element = self.numbers[0]
        self.test_object = DoubleHeap()
        # when
        self.test_object.append(element)
        # then
        assert_that(self.test_object).is_length(1)
        assert_that(self.test_object.left).is_equal_to(element)
        assert_that(self.test_object.right).is_equal_to(element)

    def test__append__when_new_element_between_minimum_and_maximum__then_added(self):
        # when
        self.test_object.append((self.minimum + self.maximum) // 2)
        # then
        assert_that(self.test_object).is_length(len(self.numbers) + 1)
        assert_that(self.test_object.left).is_equal_to(self.minimum)
        assert_that(self.test_object.right).is_equal_to(self.maximum)

    def test__append__when_new_element_less_than_minimum__then_new_minimum(self):
        # given
        element = self.minimum - 3
        # when
        self.test_object.append(element)
        # then
        assert_that(self.test_object).is_length(len(self.numbers) + 1)
        assert_that(self.test_object.left).is_equal_to(element)

    def test__append__when_new_element_greater_than_maximum__then_new_maximum(self):
        # given
        element = self.maximum + 3
        # when
        self.test_object.append(element)
        # then
        assert_that(self.test_object).is_length(len(self.numbers) + 1)
        assert_that(self.test_object.right).is_equal_to(element)

    # endregion
    # region left & right

    @staticmethod
    def test__left__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.left

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__left__when_single_element__then_this_element(self):
        # given
        element = self.numbers[0]
        self.test_object = DoubleHeap([element])
        # when
        result = self.test_object.left
        # then
        assert_that(result).is_equal_to(element)

    def test__left__when_multiple_elements__then_minimal_element(self):
        # when
        result = self.test_object.left
        # then
        assert_that(result).is_equal_to(self.minimum)

    @staticmethod
    def test__right__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.right

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__right__when_single_element__then_this_element(self):
        # given
        element = self.numbers[0]
        self.test_object = DoubleHeap([element])
        # when
        result = self.test_object.right
        # then
        assert_that(result).is_equal_to(element)

    def test__right__when_multiple_elements__then_maximal_element(self):
        # when
        result = self.test_object.right
        # then
        assert_that(result).is_equal_to(self.maximum)

    # endregion
    # region popleft & popright

    @staticmethod
    def test__popleft__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.popleft()

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__popleft__when_single_element__then_this_element_removed(self):
        # given
        element = self.numbers[0]
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
        assert_that(self.test_object).is_length(len(self.numbers) - 1)
        assert_that(result).is_equal_to(self.minimum)

    def test__popleft__when_multiple_calls__then_sorted_ascending(self):
        # when
        result = []

        while len(self.test_object) > 0:
            result.append(self.test_object.popleft())

        # then
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(self.numbers))

    @staticmethod
    def test__popright__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.popright()

        # then
        assert_that(function).raises(KeyError).when_called_with(DoubleHeap())

    def test__popright__when_single_element__then_this_element_removed(self):
        # given
        element = self.numbers[0]
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
        assert_that(self.test_object).is_length(len(self.numbers) - 1)
        assert_that(result).is_equal_to(self.maximum)

    def test__popright__when_multiple_calls__then_sorted_descending(self):
        # when
        result = []

        while len(self.test_object) > 0:
            result.append(self.test_object.popright())

        # then
        assert_that(result).is_sorted(key=lambda x: -x)
        assert_that(result).is_equal_to(sorted(self.numbers, key=lambda x: -x))

    # endregion
