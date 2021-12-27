# -*- coding: utf-8 -*-
"""Tests: Algorithm for longest common subsequence"""
import unittest

from assertpy import assert_that

from algolib.sequences import count_lcs_length


class LongestCommonSubsequenceTests(unittest.TestCase):
    @staticmethod
    def test__count_lcs_length__when_empty__then_zero():
        # when
        result = count_lcs_length("qwertyuiop", "")
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__count_lcs_length__when_same_character_text__then_shorter_length():
        # given
        size = 4
        text = "x" * size
        # when
        result = count_lcs_length(text + text, text)
        # then
        assert_that(result).is_equal_to(size)

    @staticmethod
    def test__count_lcs_length__when_repeated_single_element__then_one():
        # when
        result = count_lcs_length("abcde", "eeee")
        # then
        assert_that(result).is_equal_to(1)

    @staticmethod
    def test__count_lcs_length__when_same_text__then_text_length():
        # given
        text = "qwertyuiop"
        # when
        result = count_lcs_length(text, text)
        # then
        assert_that(result).is_equal_to(len(text))

    @staticmethod
    def test__count_lcs_length__when_subtext__then_subtext_length():
        # when
        result = count_lcs_length("qwertyuiop", "zxqwertyasdfuiopcvb")
        # then
        assert_that(result).is_equal_to(len("qwertyuiop"))

    @staticmethod
    def test__count_lcs_length__when_different__then_zero():
        # when
        result = count_lcs_length("qwertyuiop", "asdfghjkl")
        # then
        assert_that(result).is_equal_to(0)

    @staticmethod
    def test__count_lcs_length__when_common_subtext__then_common_subtext_length():
        # when
        result = count_lcs_length("qwertyuiop", "zxrtyasdfuiopcvb")
        # then
        assert_that(result).is_equal_to(len("rtyuiop"))

    @staticmethod
    def test__count_lcs_length__when_same_element_sequence__then_shorter_length():
        # given
        size = 25
        sequence = [11] * size
        # when
        result = count_lcs_length(sequence, sequence + sequence)
        # then
        assert_that(result).is_equal_to(size)

    @staticmethod
    def test__count_lcs_length__when_same_sequence__then_sequence_length():
        # given
        sequence = list(map(ord, "qwertyuiop"))
        # when
        result = count_lcs_length(sequence, sequence)
        # then
        assert_that(result).is_equal_to(len(sequence))

    @staticmethod
    def test__count_lcs_length__when_common_subsequence__then_common_subsequence_length():
        # when
        result = count_lcs_length(list(map(ord, "qwertyuiop")), list(map(ord, "zxrtyasdfuiopcvb")))
        # then
        assert_that(result).is_equal_to(len("rtyuiop"))
