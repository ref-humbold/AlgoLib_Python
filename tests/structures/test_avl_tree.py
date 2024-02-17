# -*- coding: utf-8 -*-
"""Tests: Structure of AVL tree."""
import unittest

from assertpy import assert_that

from algolib.structures import AvlTree


class AVLTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = [10, 6, 14, 97, 24, 37, 2, 30, 45, 18, 51, 71, 68, 26]
        self.absent = [111, 140, 187, 253]
        self.present = [x for i, x in enumerate(self.numbers) if i % 3 == 2]
        self.test_object = None

    def setUp(self):
        self.test_object = AvlTree(self.numbers)

    def test__op_str__then_text_representation(self):
        # when
        result = str(self.test_object)
        # then
        assert_that(result).is_equal_to("{|2, 6, 10, 14, 18, 24, 26, 30, 37, 45, 51, 68, 71, 97|}")

    @staticmethod
    def test__op_len__when_empty__then_zero():
        # when
        result = len(AvlTree())
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
        result = list(AvlTree())
        # then
        assert_that(result).is_empty()

    def test__op_iter__when_single_element__then_this_element_only(self):
        # given
        element = self.numbers[0]
        # when
        iterator = iter(AvlTree([element]))
        # then
        assert_that(next(iterator)).is_equal_to(element)
        assert_that(next).raises(StopIteration).when_called_with(iterator)

    def test__op_iter__when_multiple_elements__then_ordered_elements(self):
        # when
        result = list(self.test_object)
        # then
        assert_that(result).is_sorted()
        assert_that(result).is_equal_to(sorted(self.numbers))

    @staticmethod
    def test__op_reversed__when_empty__then_no_elements():
        # when
        result = list(reversed(AvlTree()))
        # then
        assert_that(result).is_empty()

    def test__op_reversed__when_single_element__then_this_element_only(self):
        # given
        element = self.numbers[0]
        # when
        iterator = reversed(AvlTree([element]))
        # then
        assert_that(next(iterator)).is_equal_to(element)
        assert_that(next).raises(StopIteration).when_called_with(iterator)

    def test__op_reversed__when_multiple_elements__then_reverse_ordered_elements(self):
        # when
        result = list(reversed(self.test_object))
        # then
        assert_that(result).is_sorted(reverse=True)
        assert_that(result).is_equal_to(sorted(self.numbers, reverse=True))

    # endregion
    # region op_contains

    def test__op_contains__when_empty__then_false(self):
        # when
        result = self.numbers[0] in AvlTree()
        # then
        assert_that(result).is_false()

    def test__op_contains__when_present_element__then_true(self):
        for e in self.present:
            # when
            result = e in self.test_object
            # then
            assert_that(result).is_true()

    def test__op_contains__when_absent_element__then_false(self):
        for e in self.absent:
            # when
            result = e in self.test_object
            # then
            assert_that(result).is_false()

    # endregion
    # region add

    def test__add__when_empty__then_added(self):
        # given
        element = self.numbers[0]
        self.test_object = AvlTree()
        # when
        self.test_object.add(element)
        # then
        assert_that(self.test_object).contains(element)
        assert_that(self.test_object).is_length(1)

    def test__add__when_new_element__then_added(self):
        for e in self.absent:
            # when
            self.test_object.add(e)
            # then
            assert_that(self.test_object).contains(e)

        assert_that(self.test_object).is_length(len(self.numbers) + len(self.absent))

    def test__add__when_present_element__then_nothing(self):
        for e in self.present:
            # when
            self.test_object.add(e)
            # then
            assert_that(self.test_object).contains(e)

        assert_that(self.test_object).is_length(len(self.numbers))

    # endregion
    # region remove

    def test__remove__when_empty__then_key_error(self):
        # when
        def function(tree):
            tree.remove(self.numbers[0])

        # then
        assert_that(function).raises(KeyError).when_called_with(AvlTree())

    def test__remove__when_present_element__then_removed(self):
        for e in self.present:
            # when
            self.test_object.remove(e)
            # then
            assert_that(self.test_object).does_not_contain(e)

        assert_that(self.test_object).is_length(len(self.numbers) - len(self.present))

    def test__remove__when_absent_element__then_key_error(self):
        # when
        def function(tree, element):
            tree.remove(element)

        # then
        for e in self.absent:
            assert_that(function).raises(KeyError).when_called_with(self.test_object, e)
            assert_that(self.test_object).does_not_contain(e)

        assert_that(self.test_object).is_length(len(self.numbers))

    def test__remove__when_root_greater_than_element__then_removed(self):
        # given
        root = self.absent[1]
        element = self.absent[0]
        self.test_object = AvlTree([root, element])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).contains(element)
        assert_that(self.test_object).is_length(1)

    def test__remove__when_root_less_than_element__then_removed(self):
        # given
        root = self.absent[0]
        element = self.absent[1]
        self.test_object = AvlTree([root, element])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).contains(element)
        assert_that(self.test_object).is_length(1)

    def test__remove__when_root_only__then_empty(self):
        # given
        root = self.absent[0]
        self.test_object = AvlTree([root])
        # when
        self.test_object.remove(root)
        # then
        assert_that(self.test_object).does_not_contain(root)
        assert_that(self.test_object).is_empty()

    # endregion
    # region discard & pop

    def test__discard__when_empty__then_nothing(self):
        # given
        self.test_object = AvlTree()
        # when
        self.test_object.discard(self.numbers[0])
        # then
        assert_that(self.test_object).is_empty()

    def test__discard__when_present_element__then_removed(self):
        for e in self.present:
            # when
            self.test_object.discard(e)
            # then
            assert_that(self.test_object).does_not_contain(e)

        assert_that(self.test_object).is_length(len(self.numbers) - len(self.present))

    def test__discard__when_absent_element__then_nothing(self):
        for e in self.absent:
            # when
            self.test_object.discard(e)
            # then
            assert_that(self.test_object).does_not_contain(e)

        assert_that(self.test_object).is_length(len(self.numbers))

    @staticmethod
    def test__pop__when_empty__then_key_error():
        # when
        def function(tree):
            tree.pop()

        # then
        assert_that(function).raises(KeyError).when_called_with(AvlTree())

    def test__pop__when_not_empty__then_remove_and_return_element(self):
        # when
        result = self.test_object.pop()
        # then
        assert_that(self.test_object).does_not_contain(result)
        assert_that(result).is_in(*self.numbers)
        assert_that(self.test_object).is_length(len(self.numbers) - 1)

    # endregion
