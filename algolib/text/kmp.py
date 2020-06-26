# -*- coding: utf-8 -*-
"""Knuth-Morris-Pratt algorithm"""


def kmp(text, pattern):
    """Searches for pattern occurrences in specified text using Knuth-Morris-Pratt algorithm.

    :param text: a text
    :param pattern: a pattern to search for
    :return: generator of pattern occurrence positions"""
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
    # Counts values of Knuth's PI prefix function for specified pattern.
    pi_values = [0]
    pos = 0

    for c in pattern[1:]:
        while pos > 0 and pattern[pos] != c:
            pos = pi_values[pos - 1]

        if pattern[pos] == c:
            pos += 1

        pi_values.append(pos)

    return pi_values
