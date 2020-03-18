# -*- coding: utf-8 -*-
"""Karp-Miller-Rosenberg algorithm"""


def kmr(text):
    """Builds a base words dictionary for specified text using Karp-Miller-Rosenberg algorithm.

    :param text: text to build the dictionary for
    :return: base words dictionary"""
    factors = _sign_letters(text)
    length = 2

    while length <= len(text):
        _sign_new_length(length, text, factors)
        length *= 2

    return factors


def _sign_letters(text):
    # Encodes single letters of specified text
    factors = {}
    code_value = 0
    letters = sorted(text)
    factors[letters[0]] = code_value

    for i, c in enumerate(letters[1:], start=1):
        if c != letters[i - 1]:
            code_value += 1
            factors[c] = code_value

    return factors


def _sign_new_length(new_length, text, factors):
    # Encodes substring of specified length using already counted factors
    code_value = 0
    codes = sorted([(factors[text[i:i + new_length // 2]],
                     factors[text[i + new_length // 2:i + new_length]], i)
                    for i in range(len(text) - new_length + 1)])
    factors[text[codes[0][2]:codes[0][2] + new_length]] = code_value

    for i, code in enumerate(codes[1:], start=1):
        if code != codes[i - 1]:
            substring = text[code[2]:code[2] + new_length]
            code_value += 1
            factors[substring] = code_value
