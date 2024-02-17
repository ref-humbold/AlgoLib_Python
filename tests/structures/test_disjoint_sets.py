# -*- coding: utf-8 -*-
"""Tests: Structure of disjoint sets  (union-find)."""
import unittest

from assertpy import assert_that

from algolib.structures import DisjointSets


class DisjointSetsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.absent = [111, 140, 187, 253]
        self.present = [x for i, x in enumerate(self.numbers) if i % 3 == 2]
        self.test_object = None

    def setUp(self):
        self.test_object = DisjointSets((n,) for n in self.numbers)

    @staticmethod
    def test__op_init__when_duplicates_in_different_sets__then_value_error():
        # when
        def function(*sets):
            DisjointSets(sets)

        # then
        assert_that(function).raises(ValueError).when_called_with([1, 2, 3], [1, 11, 21, 31])

    def test__op_init__when_duplicates_in_same_set__then_constructed(self):
        # given
        sets = [[1, 2, 3], [10, 100, 10]]
        # when
        self.test_object = DisjointSets(sets)
        # then
        assert_that(self.test_object).is_length(len(sets))

    @staticmethod
    def test__op_len__when_empty__then_zero():
        # when
        result = len(DisjointSets())
        # then
        assert_that(result).is_zero()

    def test__op_len__when_not_empty_then_number_of_sets(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(len(self.numbers))

    def test__clear__when_not_empty__then_empty(self):
        # when
        self.test_object.clear()
        # then
        assert_that(self.test_object).is_empty()

    # region op_contains

    def test__op_contains__when_empty__then_false(self):
        # when
        result = self.numbers[0] in DisjointSets()
        # then
        assert_that(result).is_false()

    def test__op_contains__when_present__then_true(self):
        # when
        result = self.present[0] in self.test_object
        # then
        assert_that(result).is_true()

    def test__op_contains__when_absent__then_false(self):
        # when
        result = self.absent[0] in self.test_object
        # then
        assert_that(result).is_false()

    # endregion
    # region op_iadd

    def test__op_iadd__when_empty__then_new_set(self):
        # given
        self.test_object = DisjointSets()
        # when
        self.test_object += self.numbers
        # then
        assert_that(self.test_object).contains(*self.numbers)

        for element in self.numbers:
            assert_that(self.test_object.find_set(element)).is_equal_to(self.numbers[0])

        assert_that(self.test_object).is_length(1)

    def test__op_iadd__when_new_elements__then_new_set(self):
        # when
        self.test_object += self.absent
        # then
        assert_that(self.test_object).contains(*self.absent)

        for element in self.absent:
            assert_that(self.test_object.find_set(element)).is_equal_to(self.absent[0])

        assert_that(self.test_object).is_length(len(self.numbers) + 1)

    def test__op_iadd__when_present_elements__then_value_error(self):
        # when
        def function(elements):
            self.test_object += elements

        # then
        assert_that(function).raises(ValueError).when_called_with(self.present)

    def test__op_iadd__when_new_and_present_elements__then_value_error(self):
        # when
        def function(elements):
            self.test_object += elements

        # then
        assert_that(function).raises(ValueError).when_called_with(self.absent + self.present)

    # endregion
    # region add

    def test__add__when_new_elements_to_present_represent__then_added_to_existing_set(self):
        # given
        represent = self.present[0]
        # when
        self.test_object.add(self.absent, represent)
        # then
        assert_that(self.test_object).contains(*self.absent)

        for element in self.absent:
            assert_that(self.test_object[element]).is_equal_to(self.test_object[represent])

        assert_that(self.test_object).is_length(len(self.numbers))

    def test__add__when_new_elements_to_absent_represent__then_key_error(self):
        # when
        def function(represent):
            self.test_object.add(self.absent, represent)

        # then
        assert_that(function).raises(KeyError).when_called_with(self.absent[0])

    def test__add__when_present_elements_to_absent_represent__then_value_error(self):
        # when
        def function(represent):
            self.test_object.add(self.present, represent)

        # then
        assert_that(function).raises(ValueError).when_called_with(self.absent[0])

    # endregion
    # region op_getitem & find_set

    def test__op_getitem__when_empty__then_key_error(self):
        # when
        def function(sets):
            return sets[self.numbers[0]]

        # then
        assert_that(function).raises(KeyError).when_called_with(DisjointSets())

    def test__op_getitem__when_present_element__then_represent(self):
        # given
        element = self.present[0]
        # when
        result = self.test_object[element]
        # then
        assert_that(result).is_equal_to(element)

    def test__op_getitem__when_absent_element__then_key_error(self):
        # when
        def function(element):
            return self.test_object[element]

        # then
        assert_that(function).raises(KeyError).when_called_with(self.absent[0])

    def test__find_set__when_present_element__then_represent(self):
        # given
        element = self.present[0]
        default_value = self.absent[0]
        # when
        result = self.test_object.find_set(element, default_value)
        # then
        assert_that(result).is_equal_to(element)

    def test__find_set__when_absent_element__then_default(self):
        # given
        element = self.absent[0]
        default_value = self.present[0]
        # when
        result = self.test_object.find_set(element, default_value)
        # then
        assert_that(result).is_equal_to(default_value)

    def test__find_set__when_absent_element_and_no_default__then_none(self):
        # when
        result = self.test_object.find_set(self.absent[0])
        # then
        assert_that(result).is_none()

    # endregion
    # region union_set

    def test__union_set__when_different_sets__then_same_represent(self):
        # given
        element1 = self.present[0]
        element2 = self.present[1]
        # when
        self.test_object.union_set(element1, element2)
        # then
        assert_that(self.test_object.is_same_set(element1, element2)).is_true()
        assert_that(self.test_object[element2]).is_equal_to(self.test_object[element1])
        assert_that(self.test_object).is_length(len(self.numbers) - 1)

    def test__union_set__when_single_element__then_same_represent(self):
        # given
        element = self.present[0]
        # when
        self.test_object.union_set(element, element)
        # then
        assert_that(self.test_object).is_length(len(self.numbers))

    def test__union_set__when_same_set__then_same_represent(self):
        # given
        element1 = self.present[0]
        element2 = self.present[1]
        self.test_object.union_set(element1, element2)
        # when
        self.test_object.union_set(element2, element1)
        # then
        assert_that(self.test_object.is_same_set(element1, element2)).is_true()
        assert_that(self.test_object[element2]).is_equal_to(self.test_object[element1])
        assert_that(self.test_object).is_length(len(self.numbers) - 1)

    def test__union_set__when_new_elements_in_chain__then_same_represent(self):
        # given
        first = self.present[0]
        last = self.present[-1]
        # when
        for i in range(1, len(self.present)):
            self.test_object.union_set(self.present[i - 1], self.present[i])
        # then
        assert_that(self.test_object.is_same_set(first, last)).is_true()
        assert_that(self.test_object[last]).is_equal_to(self.test_object[first])
        assert_that(self.test_object).is_length(len(self.numbers) - len(self.present) + 1)

    # endregion
    # region is_same_set

    def test__is_same_set__when_different_sets__then_false(self):
        # when
        result = self.test_object.is_same_set(self.present[0], self.present[1])
        # then
        assert_that(result).is_false()

    def test__is_same_set__when_single_element__then_true(self):
        # given
        element = self.present[0]
        # when
        result = self.test_object.is_same_set(element, element)
        # then
        assert_that(result).is_true()

    def test__is_same_set__when_same_set__then_true(self):
        # given
        element1 = self.present[0]
        element2 = self.present[1]
        self.test_object.union_set(element1, element2)
        # when
        result = self.test_object.is_same_set(element2, element1)
        # then
        assert_that(result).is_true()

    # endregion
