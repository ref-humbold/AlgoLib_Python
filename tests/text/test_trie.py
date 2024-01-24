# -*- coding: utf-8 -*-
"""Tests: Structure of trie tree."""
from unittest import TestCase

from assertpy import assert_that

from algolib.text import Trie


class TestTrie(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.texts = ["abcd", "ab", "xyz"]
        self.test_object = Trie(self.texts)

    def test__op_len__when_empty__then_zero(self):
        # given
        self.test_object = Trie()
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(0)

    def test__op_len__when_not_empty__then_number_of_texts(self):
        # when
        result = len(self.test_object)
        # then
        assert_that(result).is_equal_to(len(self.texts))

    def test__clear__when_not_empty__then_empty(self):
        # when
        self.test_object.clear()
        # then
        assert_that(self.test_object).is_empty()

    def test__op_contains__when_present__then_true(self):
        # when
        result = "abcd" in self.test_object
        # then
        assert_that(result).is_true()

    def test__op_contains__when_absent__then_false(self):
        # when
        result = "abxx" in self.test_object
        # then
        assert_that(result).is_false()

    def test__op_contains__when_absent_prefix__then_false(self):
        # when
        result = "xy" in self.test_object
        # then
        assert_that(result).is_false()

    def test__op_contains__when_wrong_type__then_type_error(self):
        # when
        def function(element):
            return element in self.test_object

        # then
        assert_that(function).raises(TypeError).when_called_with(123)

    def test__add__when_present__then_nothing(self):
        # given
        text = "abcd"
        # when
        self.test_object.add(text)
        # then
        assert_that(self.test_object).contains(text)
        assert_that(self.test_object).is_length(len(self.texts))

    def test__add__when_absent__then_added(self):
        # given
        text = "abxx"
        # when
        self.test_object.add(text)
        # then
        assert_that(self.test_object).contains(text)
        assert_that(self.test_object).is_length(len(self.texts) + 1)

    def test__add__when_absent_prefix__then_added(self):
        # given
        text = "xy"
        # when
        self.test_object.add(text)
        # then
        assert_that(text in self.test_object).is_true()
        assert_that(self.test_object).is_length(len(self.texts) + 1)

    def test__remove__when_present__then_removed(self):
        # given
        text = "abcd"
        # when
        self.test_object.remove(text)
        # then
        assert_that(text in self.test_object).is_false()
        assert_that(self.test_object).is_length(len(self.texts) - 1)

    def test__remove__when_absent__then_key_error(self):
        # when
        def function(element):
            self.test_object.remove(element)

        # then
        assert_that(function).raises(KeyError).when_called_with("abxx")

    def test__remove__when_absent_prefix__then_key_error(self):
        # when
        def function(element):
            self.test_object.remove(element)

        # then
        assert_that(function).raises(KeyError).when_called_with("xy")

    def test__discard__when_present__then_removed(self):
        # given
        text = "abcd"
        # when
        self.test_object.discard(text)
        # then
        assert_that(self.test_object).does_not_contain(text)
        assert_that(self.test_object).is_length(len(self.texts) - 1)

    def test__discard__when_absent__then_nothing(self):
        # given
        text = "abxx"
        # when
        self.test_object.discard(text)
        # then
        assert_that(self.test_object).does_not_contain(text)
        assert_that(self.test_object).is_length(len(self.texts))

    def test__discard__when_absent_prefix__then_nothing(self):
        # given
        text = "xy"
        # when
        self.test_object.discard(text)
        # then
        assert_that(self.test_object).contains("xyz")
        assert_that(self.test_object).does_not_contain(text)
        assert_that(self.test_object).is_length(len(self.texts))
