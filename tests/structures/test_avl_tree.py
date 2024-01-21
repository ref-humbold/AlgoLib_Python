# -*- coding: utf-8 -*-
"""Tests: Structure of AVL tree."""
import unittest

from assertpy import assert_that

from algolib.structures import AVLTree


class AVLTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.test_object = None

    def setUp(self):
        self.test_object = AVLTree(self.numbers)

    def test__op_str__then_text_representation(self):
        # when
        result = str(self.test_object)
        # then
        assert_that(result).is_equal_to("{|2, 6, 10, 14, 18, 24, 26, 30, 37, 45, 51, 68, 71, 97|}")

    def test__op_len__when_empty__then_zero(self):
        # given
        self.test_object = AVLTree()
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(0)

    def test__op_len__when_not_empty__then_number_of_elements(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(len(self.numbers))

    def test__op_contains__when_present_element__then_true(self):
        for e in self.numbers:
            # when
            result = e in self.test_object
            # then
            assert_that(result).is_true()

    def test__op_contains__when_outer_element(self):
        for e in [111, 140, 187]:
            # when
            result = e in self.test_object
            # then
            assert_that(result).is_false()

    def test__op_iter__when_not_empty__then_ordered_elements(self):
        # when
        iterator = iter(self.test_object)
        result = []

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break
        # then
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(self.numbers))

    def test__op_iter__when_empty__then_no_elements(self):
        # given
        self.test_object = AVLTree()
        # when
        iterator = iter(self.test_object)
        result = []

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break
        # then
        assert_that(result).is_empty()

    def test__op_reversed__when_not_empty__then_reverse_ordered_elements(self):
        # when
        iterator = reversed(self.test_object)
        result = []

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break
        # then
        assert_that(result).is_sorted(reverse=True)
        assert_that(result).is_equal_to(sorted(self.numbers, reverse=True))

    def test__op_reversed__when_empty__then_no_elements(self):
        # given
        self.test_object = AVLTree()
        # when
        iterator = reversed(self.test_object)
        result = []

        while True:
            try:
                result.append(next(iterator))
            except StopIteration:
                break
        # then
        assert_that(result).is_empty()

    def test__add__when_new_element__then_increase_length(self):
        # given
        for i, e in enumerate([111, 140, 187], start=1):
            # when
            self.test_object.add(e)
            # then
            assert_that(self.test_object).contains(e)
            assert_that(self.test_object).is_length(len(self.numbers) + i)

    def test__add__when_present_element__then_same_length(self):
        # given
        elements = [14, 24, 30, 45]
        # when
        for e in elements:
            self.test_object.add(e)
        # then
        assert_that(self.test_object).contains(*elements)
        assert_that(self.test_object).is_length(len(self.numbers))

    def test__remove__when_present_element__then_not_in(self):
        # given
        elements = [14, 24, 30, 45]
        # when
        for e in [14, 24, 30, 45]:
            self.test_object.remove(e)
        # then
        assert_that(self.test_object).does_not_contain(*elements)

    def test__remove__when_two_elements_with_root__then_root_not_in__1(self):
        # given
        root = 27
        elem = 11
        self.test_object = AVLTree([root, elem])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).contains(elem)

    def test__remove__when_two_elements_with_root__then_root_not_in__2(self):
        # given
        root = 11
        elem = 27
        self.test_object = AVLTree([root, elem])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).contains(elem)

    def test__remove__when_one_element_with_root__then_empty(self):
        # given
        root = 0
        self.test_object = AVLTree([root])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).is_empty()

    def test__remove__when_empty__then_key_error(self):
        # given
        self.test_object = AVLTree()

        # when
        def function(element):
            self.test_object.remove(element)

        # then
        assert_that(function).raises(KeyError).when_called_with(0)
        assert_that(self.test_object).is_empty()

    def test__remove__when_outer_element__then_key_error(self):
        # when
        def function(element):
            self.test_object.remove(element)

        # then
        for e in [111, 140, 187]:
            assert_that(function).raises(KeyError).when_called_with(e)
            assert_that(self.test_object).does_not_contain(e)

    def test__discard__when_present_element__then_not_in(self):
        # given
        elements = [14, 24, 30, 45]
        # when
        for e in elements:
            self.test_object.discard(e)
        # then
        assert_that(self.test_object).does_not_contain(*elements)

    def test__discard__when_outer_element__then_nothing(self):
        # given
        elements = [111, 140, 187]
        # when
        for e in elements:
            self.test_object.discard(e)
        # then
        assert_that(self.test_object).does_not_contain(*elements)

    def test__discard__when_empty__then_nothing(self):
        # given
        self.test_object = AVLTree()
        # when
        self.test_object.discard(0)
        # then
        assert_that(self.test_object).is_empty()

    def test__pop__when_not_empty__then_remove_and_return_element(self):
        # when
        result = self.test_object.pop()
        # then
        assert_that(self.test_object).does_not_contain(result)
        assert_that(result).is_in(*self.numbers)
        assert_that(self.test_object).is_length(len(self.numbers) - 1)

    @staticmethod
    def test__pop__when_empty__then_key_error():
        # when
        def function(tree):
            tree.pop()

        # then
        assert_that(function).raises(KeyError).when_called_with(AVLTree())

    def test__clear__when_not_empty__then_empty(self):
        # when
        self.test_object.clear()
        # then
        assert_that(self.test_object).is_empty()
