# -*- coding: utf-8 -*-
"""ALGORYTM KNUTHA-MORRISA-PRATTA WYSZUKIWANIA WZORCA W TEKŚCIE"""


def kmp(text, pattern):
    """Algorytm Knutha-Morrisa-Pratta
    :param text: słowo
    :param pattern: wzorzec
    :returns: generator pozycji wystąpień wzorca w słowie"""
    if not isinstance(text, str):
        raise TypeError("Text should be of type 'str', not {0}.".format(type(text).__name__))

    if not isinstance(pattern, str):
        raise TypeError("Pattern should be of type 'str', not {0}.".format(type(pattern).__name__))

    return _match(text, pattern)


def _match(text, pattern):
    """Wyszukiwanie wystąpień wzorca w słowie
    :param text: słowo
    :param pattern: wzorzec
    :returns: generator pozycji wystąpień wzorca w słowie"""
    if pattern == "":
        return

    pi_values = _prefix(pattern)
    pos = 0

    for i, letter in enumerate(text):
        while pos > 0 and pattern[pos] != letter:
            pos = pi_values[pos - 1]

        if pattern[pos] == letter:
            pos += 1

        if pos == len(pattern):
            yield i - len(pattern) + 1
            pos = pi_values[pos - 1]


def _prefix(pattern):
    """Funkcja prefiksowa pi Knutha
    :param pattern: wzorzec
    :returns: wartości funkcji prefiksowej"""
    pi_values = [0]
    pos = 0

    for letter in pattern[1:]:
        while pos > 0 and pattern[pos] != letter:
            pos = pi_values[pos - 1]

        if pattern[pos] == letter:
            pos += 1

        pi_values.append(pos)

    return pi_values
