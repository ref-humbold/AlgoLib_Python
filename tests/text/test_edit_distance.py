# -*- coding: utf-8 -*-
"""Tests: Algorithms for edit distance"""
import unittest

from assertpy import assert_that

from algolib.text import count_lcs, count_levenshtein


class EditDistanceTest(unittest.TestCase):
    # region count_levenshtein

    @staticmethod
    def count_levenshtein__when_same_text__then_zero():
        # given
        text = "qwertyuiop"
        # when
        result = count_levenshtein(text, text)
        # then
        assert_that(result).is_zero()

    @staticmethod
    def count_levenshtein__when_empty_source__then_sum_of_insertions(self):
        # given
        text = "qwertyuiop"
        insertion_cost = 2
        # when
        result = count_levenshtein("", text, insertion_cost, 1, 1)
        # then
        assert_that(result).is_equal_to(len(text) * insertion_cost)

    @staticmethod
    def count_levenshtein__when_empty_destination__then_sum_of_deletions(self):
        # given
        text = "qwertyuiop"
        deletion_cost = 2
        # when
        result = count_levenshtein(text, "", 1, deletion_cost, 1)
        # then
        assert_that(result).is_equal_to(len(text) * deletion_cost)

    @staticmethod
    def count_levenshtein__when_negative_cost__then_value_error():
        # when
        def function(cost):
            count_levenshtein("a", "b", substitution_cost=cost)

        # then
        assert_that(function).raises(ValueError).when_called_with(-1)

    # endregion
    # region count_lcs

    @staticmethod
    def count_lcs__when_same_text__then_zero():
        # given
        text = "qwertyuiop"
        # when
        result = count_lcs(text, text)
        # then
        assert_that(result).is_zero()

    @staticmethod
    def count_lcs__when_empty_source__then_sum_of_insertions(self):
        # given
        text = "qwertyuiop"
        insertion_cost = 2
        # when
        result = count_lcs("", text, insertion_cost, 1)
        # then
        assert_that(result).is_equal_to(len(text) * insertion_cost)

    @staticmethod
    def count_lcs__when_empty_destination__then_sum_of_deletions(self):
        # given
        text = "qwertyuiop"
        deletion_cost = 2
        # when
        result = count_lcs(text, "", 1, deletion_cost)
        # then
        assert_that(result).is_equal_to(len(text) * deletion_cost)

    @staticmethod
    def count_lcs__when_negative_cost__then_value_error():
        # when
        def function(cost):
            count_lcs("a", "b", deletion_cost=cost)

        # then
        assert_that(function).raises(ValueError).when_called_with(-1)

    # endregion
