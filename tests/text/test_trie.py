# -*- coding: utf-8 -*-
"""Tests: Structure of trie tree"""
from unittest import TestCase

from algolib.text import Trie


class TestTrie(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.texts = ["abcd", "ab", "xyz"]
        self.test_object = Trie(self.texts)

    def test__len__when_empty__then_zero(self):
        # given
        self.test_object = Trie()
        # when
        result = len(self.test_object)
        # then
        self.assertEqual(0, result)

    def test__size__when_not_empty__then_number_of_texts(self):
        # when
        result = len(self.test_object)
        # then
        self.assertEqual(len(self.texts), result)

    def test__find__when_present__then_true(self):
        # when
        result = "abcd" in self.test_object
        # then
        self.assertTrue(result)

    def test__find__when_absent__then_false(self):
        # when
        result = "abxx" in self.test_object
        # then
        self.assertFalse(result)

    def test__find__when_absent_prefix__then_false(self):
        # when
        result = "xy" in self.test_object
        # then
        self.assertFalse(result)

    def test__add__when_present__then_nothing(self):
        # given
        text = "abcd"
        # when
        self.test_object.add(text)
        # then
        self.assertTrue(text in self.test_object)
        self.assertEqual(len(self.texts), len(self.test_object))

    def test__add__when_absent__then_added(self):
        # given
        text = "abxx"
        # when
        self.test_object.add(text)
        # then
        self.assertTrue(text in self.test_object)
        self.assertEqual(len(self.texts) + 1, len(self.test_object))

    def test__add__when_absent_prefix__then_added(self):
        # given
        text = "xy"
        # when
        self.test_object.add(text)
        # then
        self.assertTrue(text in self.test_object)
        self.assertEqual(len(self.texts) + 1, len(self.test_object))

    def test__remove__when_present__then_removed(self):
        # given
        text = "abcd"
        # when
        self.test_object.remove(text)
        # then
        self.assertFalse(text in self.test_object)
        self.assertEqual(len(self.texts) - 1, len(self.test_object))

    def test__remove__when_absent__then_key_error(self):
        # then
        with self.assertRaises(KeyError):
            # when
            self.test_object.remove("abxx")

    def test__remove__when_absent_prefix__then_key_error(self):
        # then
        with self.assertRaises(KeyError):
            # when
            self.test_object.remove("xy")

    def test__discard__when_present__then_removed(self):
        # given
        text = "abcd"
        # when
        self.test_object.discard(text)
        # then
        self.assertFalse(text in self.test_object)
        self.assertEqual(len(self.texts) - 1, len(self.test_object))

    def test__discard__when_absent__then_nothing(self):
        # given
        text = "abxx"
        # when
        self.test_object.discard(text)
        # then
        self.assertFalse(text in self.test_object)
        self.assertEqual(len(self.texts), len(self.test_object))

    def test__discard__when_absent_prefix__then_nothing(self):
        # given
        text = "xy"
        # when
        self.test_object.discard(text)
        # then
        self.assertTrue("xyz" in self.test_object)
        self.assertFalse(text in self.test_object)
        self.assertEqual(len(self.texts), len(self.test_object))
