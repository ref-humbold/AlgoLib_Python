# -*- coding: utf-8 -*-
"""Knuth-Morris-Pratt algorithm for pattern searching."""
from typing import Iterable


def kmp_search(text: str, pattern: str) -> Iterable[int]:
    """Searches for pattern occurrences in given text using Knuth-Morris-Pratt algorithm.

    :param text: the text
    :param pattern: the pattern
    :return: the indices with pattern occurrences"""
    if pattern == "":
        return

    pi_values = _prefix(pattern)
    position = 0

    for i, char in enumerate(text):
        while position > 0 and pattern[position] != char:
            position = pi_values[position - 1]

        if pattern[position] == char:
            position += 1

        if position == len(pattern):
            yield i - len(pattern) + 1
            position = pi_values[position - 1]


def _prefix(pattern):
    # Computes Knuth's PI prefix function values for specified pattern.
    pi_values = [0]
    position = 0

    for letter in pattern[1:]:
        while position > 0 and pattern[position] != letter:
            position = pi_values[position - 1]

        if pattern[position] == letter:
            position += 1

        pi_values.append(position)

    return pi_values
