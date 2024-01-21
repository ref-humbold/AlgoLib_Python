# -*- coding: utf-8 -*-
"""Tests: Algorithms for edit distance."""
import unittest

from assertpy import assert_that

from algolib.text import count_hamming, count_lcs, count_levenshtein


class EditDistanceTest(unittest.TestCase):
    _PRECISION = 1e-6

    # region count_levenshtein

    @classmethod
    def test__count_levenshtein__when_different_text__then_distance(cls):
        # given
        source = "qwertyuiop"
        destination = "wertzuiopsx"
        # when
        result = count_levenshtein(source, destination)
        # then
        assert_that(result).is_close_to(4.0, cls._PRECISION)

    @staticmethod
    def test__count_levenshtein__when_same_text__then_zero():
        # given
        text = "qwertyuiop"
        # when
        result = count_levenshtein(text, text)
        # then
        assert_that(result).is_zero()

    @classmethod
    def test__count_levenshtein__when_empty_source__then_sum_of_insertions(cls):
        # given
        text = "qwertyuiop"
        insertion_cost = 2
        # when
        result = count_levenshtein("",
                                   text,
                                   insertion_cost=insertion_cost,
                                   deletion_cost=1,
                                   substitution_cost=1)
        # then
        assert_that(result).is_close_to(len(text) * insertion_cost, cls._PRECISION)

    @classmethod
    def test__count_levenshtein__when_empty_destination__then_sum_of_deletions(cls):
        # given
        text = "qwertyuiop"
        deletion_cost = 2
        # when
        result = count_levenshtein(text,
                                   "",
                                   insertion_cost=1,
                                   deletion_cost=deletion_cost,
                                   substitution_cost=1)
        # then
        assert_that(result).is_close_to(len(text) * deletion_cost, cls._PRECISION)

    @staticmethod
    def test__count_levenshtein__when_negative_cost__then_value_error():
        # when
        def function(cost):
            count_levenshtein("a", "b", substitution_cost=cost)

        # then
        assert_that(function).raises(ValueError).when_called_with(-1)

    # endregion
    # region count_lcs

    @classmethod
    def test__count_lcs__when_different_text__then_distance(cls):
        # given
        source = "qwertyuiop"
        destination = "wertzuiopsx"
        # when
        result = count_lcs(source, destination)
        # then
        assert_that(result).is_close_to(5.0, cls._PRECISION)

    @staticmethod
    def test__count_lcs__when_same_text__then_zero():
        # given
        text = "qwertyuiop"
        # when
        result = count_lcs(text, text)
        # then
        assert_that(result).is_zero()

    @classmethod
    def test__count_lcs__when_empty_source__then_sum_of_insertions(cls):
        # given
        text = "qwertyuiop"
        insertion_cost = 2
        # when
        result = count_lcs("", text, insertion_cost=insertion_cost, deletion_cost=1)
        # then
        assert_that(result).is_close_to(len(text) * insertion_cost, cls._PRECISION)

    @classmethod
    def test__count_lcs__when_empty_destination__then_sum_of_deletions(cls):
        # given
        text = "qwertyuiop"
        deletion_cost = 2
        # when
        result = count_lcs(text, "", insertion_cost=1, deletion_cost=deletion_cost)
        # then
        assert_that(result).is_close_to(len(text) * deletion_cost, cls._PRECISION)

    @staticmethod
    def test__count_lcs__when_negative_cost__then_value_error():
        # when
        def function(cost):
            count_lcs("a", "b", deletion_cost=cost)

        # then
        assert_that(function).raises(ValueError).when_called_with(-1)

    # endregion
    # region count_hamming

    @classmethod
    def test__count_hamming__when_different_text__then_distance(cls):
        # given
        source = "qwertyuiop"
        destination = "qvertzuimp"
        substitution_cost = 2.0
        # when
        result = count_hamming(source, destination, substitution_cost=substitution_cost)
        # then
        assert_that(result).is_close_to(6.0, cls._PRECISION)

    @staticmethod
    def test__count_hamming__when_empty__then_zero():
        # when
        result = count_hamming("", "")
        # then
        assert_that(result).is_zero()

    @staticmethod
    def test__count_hamming__when_same_text__then_zero():
        # given
        text = "qwertyuiop"
        # when
        result = count_hamming(text, text)
        # then
        assert_that(result).is_zero()

    @staticmethod
    def test__count_hamming__when_different_length__then_value_error():
        # when
        def function():
            count_hamming("qwerty", "asdf")

        # then
        assert_that(function).raises(ValueError)

    @staticmethod
    def test__count_hamming__when_negative_cost__then_value_error():
        # when
        def function(cost):
            count_hamming("a", "b", substitution_cost=cost)

        # then
        assert_that(function).raises(ValueError).when_called_with(-1)

    # endregion
