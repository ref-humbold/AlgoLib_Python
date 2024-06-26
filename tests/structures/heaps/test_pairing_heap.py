# -*- coding: utf-8 -*-
"""Tests: Structure of pairing heap."""
import unittest

from assertpy import assert_that

from algolib.structures.heaps import PairingHeap


class PairingHeapTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.minimum = min(self.numbers)
        self.test_object = None

    def setUp(self):
        self.test_object = PairingHeap(self.numbers)

    @staticmethod
    def test__op_len__when_empty__then_zero():
        # when
        result = len(PairingHeap())

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

    # region op_iter

    @staticmethod
    def test__op_iter__when_empty__then_no_elements():
        # when
        result = list(PairingHeap())

        # then
        assert_that(result).is_empty()

    def test__op_iter__when_single_element__then_this_element_only(self):
        # given
        element = self.numbers[0]

        # when
        iterator = iter(PairingHeap([element]))

        # then
        assert_that(next(iterator)).is_equal_to(element)
        assert_that(next).raises(StopIteration).when_called_with(iterator)

    def test__op_iter__when_multiple_elements__then_all_elements_minimum_first(self):
        # when
        result = list(self.test_object)

        # then
        assert_that(result).is_length(len(self.numbers))
        assert_that(result).contains_only(*self.numbers)
        assert_that(result[0]).is_equal_to(self.minimum)

    # endregion
    # region append

    def test__append__when_empty__then_added(self):
        # given
        element = self.numbers[0]
        self.test_object = PairingHeap()

        # when
        self.test_object.append(element)

        # then
        assert_that(self.test_object).is_length(1)
        assert_that(self.test_object.head).is_equal_to(element)

    def test__append__when_new_element_less_than_minimum__then_new_minimum(self):
        # given
        element = self.minimum - 3

        # when
        self.test_object.append(element)

        # then
        assert_that(self.test_object).is_length(len(self.numbers) + 1)
        assert_that(self.test_object.head).is_equal_to(element)

    def test__append__when_new_element_greater_than_minimum__then_added(self):
        # given
        element = self.minimum + 3

        # when
        self.test_object.append(element)

        # then
        assert_that(self.test_object).is_length(len(self.numbers) + 1)
        assert_that(self.test_object.head).is_equal_to(self.minimum)

    # endregion
    # region head

    @staticmethod
    def test__head__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.head

        # then
        assert_that(function).raises(KeyError).when_called_with(PairingHeap())

    def test__head__when_single_element__then_this_element(self):
        # given
        element = self.numbers[0]

        # when
        result = PairingHeap([element]).head

        # then
        assert_that(result).is_equal_to(element)

    def test__head__when_multiple_elements__then_minimal_element(self):
        # when
        result = self.test_object.head

        # then
        assert_that(result).is_equal_to(self.minimum)

    # endregion
    # region pop

    @staticmethod
    def test__pop__when_empty__then_key_error():
        # when
        def function(heap):
            return heap.pop()

        # then
        assert_that(function).raises(KeyError).when_called_with(PairingHeap())

    def test__pop__when_single_element__then_this_element_removed(self):
        # given
        element = self.numbers[0]
        self.test_object = PairingHeap([element])

        # when
        result = self.test_object.pop()

        # then
        assert_that(self.test_object).is_empty()
        assert_that(result).is_equal_to(element)

    def test__pop__when_multiple_elements__then_minimal_element_removed(self):
        # when
        result = self.test_object.pop()

        # then
        assert_that(self.test_object).is_length(len(self.numbers) - 1)
        assert_that(result).is_equal_to(self.minimum)

    def test__pop__when_multiple_calls__then_sorted(self):
        # when
        result = []

        while len(self.test_object) > 0:
            result.append(self.test_object.pop())

        # then
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(self.numbers))

    # endregion
    # region op_add

    def test__op_add__when_empty_and_not_empty__then_same_as_other(self):
        # given
        self.test_object = PairingHeap()
        other = PairingHeap(self.numbers)

        # when
        result = self.test_object + other

        # then
        assert_that(len(result)).is_equal_to(len(self.numbers))
        assert_that(result.head).is_equal_to(other.head)

    def test__op_add__when_not_empty_and_empty__then_no_changes(self):
        # when
        result = self.test_object + PairingHeap()

        # then
        assert_that(len(result)).is_equal_to(len(self.numbers))
        assert_that(result.head).is_equal_to(self.minimum)

    def test__op_add__when_other_has_less_minimum__then_new_minimum(self):
        # given
        other = PairingHeap([self.minimum - 3, self.minimum + 5, self.minimum + 13,
                             self.minimum + 20])

        # when
        result = self.test_object + other

        # then
        assert_that(len(result)).is_equal_to(len(self.test_object) + len(other))
        assert_that(result.head).is_equal_to(other.head)

    def test__op_add__when_other_has_greater_minimum__then_minimum_remains(self):
        # given
        other = PairingHeap([self.minimum + 5, self.minimum + 13, self.minimum + 20])

        # when
        result = self.test_object + other

        # then
        assert_that(len(result)).is_equal_to(len(self.numbers) + len(other))
        assert_that(result.head).is_equal_to(self.test_object.head)

    def test__op_add__when_multiple_merges__then_changed_only_merging_heap(self):
        # given
        first_elements = [10, 20]
        second_elements = [4, 8]

        self.test_object = PairingHeap()
        first = PairingHeap(first_elements)
        second = PairingHeap(second_elements)

        # when
        result1 = self.test_object + first
        result2 = result1 + second

        # then
        assert_that(result1.head).is_equal_to(min(first_elements))
        assert_that(list(result1)).contains_only(*first_elements)
        assert_that(result2.head).is_equal_to(min(*first_elements, *second_elements))
        assert_that(list(result2)).contains_only(*first_elements, *second_elements)
        assert_that(list(self.test_object)).is_empty()
        assert_that(list(first)).contains_only(*first_elements)
        assert_that(list(second)).contains_only(*second_elements)

    # endregion
    # region op_iadd

    def test__op_iadd__when_empty_and_not_empty__then_same_as_other(self):
        # given
        self.test_object = PairingHeap()
        other = PairingHeap(self.numbers)

        # when
        self.test_object += other

        # then
        assert_that(len(self.test_object)).is_equal_to(len(self.numbers))
        assert_that(self.test_object.head).is_equal_to(other.head)

    def test__op_iadd__when_not_empty_and_empty__then_no_changes(self):
        # when
        self.test_object += PairingHeap()

        # then
        assert_that(len(self.test_object)).is_equal_to(len(self.numbers))
        assert_that(self.test_object.head).is_equal_to(self.minimum)

    def test__op_iadd__when_other_has_less_minimum__then_new_minimum(self):
        # given
        other = PairingHeap([self.minimum - 3, self.minimum + 5, self.minimum + 13,
                             self.minimum + 20])

        # when
        self.test_object += other

        # then
        assert_that(len(self.test_object)).is_equal_to(len(self.numbers) + len(other))
        assert_that(self.test_object.head).is_equal_to(other.head)

    def test__op_iadd__when_other_has_greater_minimum__then_minimum_remains(self):
        # given
        other = PairingHeap([self.minimum + 5, self.minimum + 13, self.minimum + 20])

        # when
        self.test_object += other

        # then
        assert_that(len(self.test_object)).is_equal_to(len(self.numbers) + len(other))
        assert_that(self.test_object.head).is_equal_to(self.minimum)

    def test__op_iadd__when_multiple_merges__then_changed_only_merging_heap(self):
        # given
        first_elements = [10, 20]
        second_elements = [4, 8]

        self.test_object = PairingHeap()
        first = PairingHeap(first_elements)
        second = PairingHeap(second_elements)

        # when
        self.test_object += first
        self.test_object += second

        # then
        assert_that(self.test_object.head).is_equal_to(min(*first_elements, *second_elements))
        assert_that(list(self.test_object)).contains_only(*first_elements, *second_elements)
        assert_that(list(first)).contains_only(*first_elements)
        assert_that(list(second)).contains_only(*second_elements)

    # endregion
