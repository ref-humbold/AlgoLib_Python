# -*- coding: utf-8 -*-
"""Knuth-Morris-Pratt algorithm for pattern searching"""
from typing import Iterable


def kmp(text: str, pattern: str) -> Iterable[int]:
    """Searches for pattern occurrences in given text using Knuth-Morris-Pratt algorithm.

    :param text: a text
    :param pattern: a pattern
    :return: generator of indices with pattern occurrences"""
    if pattern == "":
        return

    pi_values = _prefix(pattern)
    pos = 0

    for i, char in enumerate(text):
        while pos > 0 and pattern[pos] != char:
            pos = pi_values[pos - 1]

        if pattern[pos] == char:
            pos += 1

        if pos == len(pattern):
            yield i - len(pattern) + 1
            pos = pi_values[pos - 1]


def _prefix(pattern):
    # Computes Knuth's PI prefix function values for specified pattern.
    pi_values = [0]
    pos = 0

    for char in pattern[1:]:
        while pos > 0 and pattern[pos] != char:
            pos = pi_values[pos - 1]

        if pattern[pos] == char:
            pos += 1

        pi_values.append(pos)

    return pi_values
