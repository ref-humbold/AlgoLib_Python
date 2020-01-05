# -*- coding: utf-8 -*-
"""Karp-Miller-Rosenberg algorithm."""


def kmr(text):
    """Budowa słownika podsłów bazowych
    :param text: słowo
    :returns: słownik podsłów bazowych"""
    factors = _sign_letters(text)
    length = 2

    while length <= len(text):
        _double_length(length, text, factors)
        length <<= 1

    return factors


def _sign_letters(text):
    """Budowa podsłów złożonych z pojedynczych znaków
    :param text: słowo
    :returns: słownik dla pojedynczych znaków"""
    factors = {}
    code_value = 0
    letters = sorted(text)
    factors[letters[0]] = code_value

    for i, ltr in enumerate(letters[1:], start=1):
        if ltr != letters[i - 1]:
            code_value += 1
            factors[ltr] = code_value

    return factors


def _double_length(new_length, text, factors):
    """Budowa nowych podsłów o podwojonej długości
    :param new_length: nowa długość podsłów
    :param text: słowo
    :param factors: słownik podsłów bazowych"""
    code_value = 0
    codes = sorted([(
        factors[text[i:i + new_length // 2]], factors[text[i + new_length // 2:i + new_length]
        ], i
    ) for i in range(len(text) - new_length + 1)])
    factors[text[codes[0][2]:codes[0][2] + new_length]] = code_value

    for i, code in enumerate(codes[1:], start=1):
        if code != codes[i - 1]:
            substr = text[code[2]:code[2] + new_length]
            code_value += 1
            factors[substr] = code_value
