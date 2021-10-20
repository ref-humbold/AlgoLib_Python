# -*- coding: utf-8 -*-
"""Tests: Structure of disjoint sets  (union-find)"""
import unittest

from assertpy import assert_that

from algolib.structures import DisjointSets


class DisjointSetsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_object = None

    def setUp(self):
        self.test_object = DisjointSets(range(10))

    def test__len__then_sets_count(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(10)

    def test__contains__when_present__then_true(self):
        # when
        result = 4 in self.test_object
        # then
        assert_that(result).is_true()

    def test__contains__when_absent__then_false(self):
        # when
        result = 17 in self.test_object
        # then
        assert_that(result).is_false()

    def test__iadd__when_new_elements__then_singleton_sets(self):
        # given
        elements = [14, 18, 23]
        # when
        self.test_object += elements
        # then
        assert_that(self.test_object).contains(*elements)

        for elem in elements:
            assert_that(self.test_object.find_set(elem)).is_equal_to(elem)

    def test__iadd__when_present_element__then_value_error(self):
        # when
        def function(elements):
            self.test_object += elements

        # then
        assert_that(function).raises(ValueError).when_called_with([11, 7, 15])

    def test__getitem__when_present_element__then_represent(self):
        # given
        elem = 4
        # when
        result = self.test_object[elem]
        # then
        assert_that(result).is_equal_to(elem)

    def test__getitem__when_absent_element__then_key_error(self):
        # when
        def function(element):
            return self.test_object[element]

        # then
        assert_that(function).raises(KeyError).when_called_with(18)

    def test__find_set__when_present_element__then_represent(self):
        # given
        elem = 4
        # when
        result = self.test_object.find_set(elem, 10)
        # then
        assert_that(result).is_equal_to(elem)

    def test__find_set__when_absent_element__then_default(self):
        # given
        default = 0
        # when
        result = self.test_object.find_set(22, default)
        # then
        assert_that(result).is_equal_to(default)

    def test__find_set__when_absent_element_and_no_default__then_none(self):
        # when
        result = self.test_object.find_set(12)
        # then
        assert_that(result).is_none()

    def test__union_set__when_different_sets__then_same_represent(self):
        # given
        elem1 = 4
        elem2 = 6
        # when
        self.test_object.union_set(elem1, elem2)
        # then
        assert_that(self.test_object.is_same_set(elem1, elem2)).is_true()
        assert_that(self.test_object[elem2]).is_equal_to(self.test_object[elem1])

    def test__union_set__when_same_element__then_same_represent(self):
        # given
        elem = 4
        # when
        self.test_object.union_set(elem, elem)
        # then
        assert_that(self.test_object.is_same_set(elem, elem)).is_true()
        assert_that(self.test_object[elem]).is_equal_to(self.test_object[elem])

    def test__union_set__when_elements_in_one_set__then_same_represent(self):
        # given
        elem1 = 3
        elem2 = 8
        self.test_object.union_set(elem1, elem2)
        # when
        self.test_object.union_set(elem2, elem1)
        # then
        assert_that(self.test_object.is_same_set(elem1, elem2)).is_true()
        assert_that(self.test_object[elem2]).is_equal_to(self.test_object[elem1])

    def test__union_set__when_absent_element__then_key_error(self):
        def function(elem1, elem2):
            self.test_object.union_set(elem1, elem2)

        # then
        assert_that(function).raises(KeyError).when_called_with(15, 6)

    def test__union_set__when_new_elements_in_chain__then_same_represent(self):
        # given
        elements = [20, 17, 35]
        # when
        self.test_object.add(*elements) \
            .union_set(elements[0], elements[1]) \
            .union_set(elements[1], elements[2])
        # then
        assert_that(self.test_object.is_same_set(elements[0], elements[2])).is_true()
        assert_that(self.test_object[elements[2]]).is_equal_to(self.test_object[elements[0]])

    def test__is_same_set__when_different_sets__then_false(self):
        # when
        result = self.test_object.is_same_set(4, 6)
        # then
        assert_that(result).is_false()

    def test__is_same_set__when_same_element__then_true(self):
        # when
        result = self.test_object.is_same_set(4, 4)
        # then
        assert_that(result).is_true()

    def test__is_same_set__when_same_set__then_true(self):
        # given
        elem1 = 3
        elem2 = 8
        self.test_object.union_set(elem1, elem2)
        # when
        result = self.test_object.is_same_set(elem1, elem2)
        # then
        assert_that(result).is_true()

    def test__is_same_set__when_absent__then_key_error(self):
        def function(elem1, elem2):
            return self.test_object.is_same_set(elem1, elem2)

        # then
        assert_that(function).raises(KeyError).when_called_with(15, 6)
