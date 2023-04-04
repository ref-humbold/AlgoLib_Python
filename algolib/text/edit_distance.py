# -*- coding: utf-8 -*-
"""Algorithms for edit distance"""


def count_levenshtein(source: str,
                      destination: str,
                      insertion_cost: float = 1.0,
                      deletion_cost: float = 1.0,
                      substitution_cost: float = 1.0) -> float:
    """Computes cost of Levenshtein edit distance between given texts.

    :param source: initial text
    :param destination: final text
    :param insertion_cost: cost of insertion operation
    :param deletion_cost: cost of deletion operation
    :param substitution_cost: cost of substitution operation
    :return: cost of edit distance"""
    if insertion_cost < 0 or deletion_cost < 0 or substitution_cost < 0:
        raise ValueError("Cost cannot be negative")

    distance = [i * insertion_cost for i in range(len(destination) + 1)]

    for element1 in source:
        previous_above = distance[0]
        distance[0] += deletion_cost

        for i, element2 in enumerate(destination):
            previous_diagonal = previous_above
            previous_above = distance[i + 1]
            distance[i + 1] = previous_diagonal if element1 == element2 else min(
                    previous_above + deletion_cost, distance[i] + insertion_cost, previous_diagonal
                    + substitution_cost)

    return distance[-1]


def count_lcs(source: str,
              destination: str,
              insertion_cost: float = 1.0,
              deletion_cost: float = 1.0) -> float:
    """Computes cost of LCS edit distance between given texts.

    :param source: initial text
    :param destination: final text
    :param insertion_cost: cost of insertion operation
    :param deletion_cost: cost of deletion operation
    :return: cost of edit distance"""
    if insertion_cost < 0 or deletion_cost < 0:
        raise ValueError("Cost cannot be negative")

    distance = [i * insertion_cost for i in range(len(destination) + 1)]

    for element1 in source:
        previous_above = distance[0]
        distance[0] += deletion_cost

        for i, element2 in enumerate(destination):
            previous_diagonal = previous_above
            previous_above = distance[i + 1]
            distance[i + 1] = previous_diagonal if element1 == element2 else min(
                    previous_above + deletion_cost, distance[i] + insertion_cost)

    return distance[-1]


def count_hamming(source: str, destination: str, substitution_cost: float = 1.0) -> float:
    """Computes cost of Hamming edit distance between given texts of equal length.

    :param source: initial text
    :param destination: final text
    :param substitution_cost: cost of substitution operation
    :return: cost of edit distance"""
    if substitution_cost < 0:
        raise ValueError("Cost cannot be negative")

    if len(source) != len(destination):
        raise ValueError("Texts should have equal length")

    return sum(substitution_cost for sc, dc in zip(source, destination) if sc != dc)
