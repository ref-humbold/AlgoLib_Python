# -*- coding: utf-8 -*-
"""Knuth-Morris-Pratt algorithm"""


def kmp(text, pattern):
    """Knuth-Morris-Pratt algorithm
    :param text: text
    :param pattern: pattern to search for
    :returns: generator of pattern occurrence positions"""
    if pattern == "":
        return

    pi_values = _prefix(pattern)
    pos = 0

    for i, ltr in enumerate(text):
        while pos > 0 and pattern[pos] != ltr:
            pos = pi_values[pos - 1]

        if pattern[pos] == ltr:
            pos += 1

        if pos == len(pattern):
            yield i - len(pattern) + 1
            pos = pi_values[pos - 1]


def _prefix(pattern):
    """Knuth's pi prefix function
    :param pattern: pattern to count the function for
    :returns: list of prefix function values"""
    pi_values = [0]
    pos = 0

    for ltr in pattern[1:]:
        while pos > 0 and pattern[pos] != ltr:
            pos = pi_values[pos - 1]

        if pattern[pos] == ltr:
            pos += 1

        pi_values.append(pos)

    return pi_values
