# -*- coding:utf-8 -*-
"""SPEŁNIALNOŚĆ FORMUŁ 2-CNF"""
from .graphs import DirectedGraph


def is_satisfiable(formula):
    """Sprawdzanie spełnialności formuły 2-CNF.
    :param formula: lista klauzul
    :returns: czy formuła spełnialna"""
    digraph = _make_graph(formula)

    return False


def _make_graph(formula):
    """Wyznaczanie grafu implikacji formuły 2-CNF.
    :param formula: lista klauzul
    :returns: skierowany graf implikacji"""
    digraph = DirectedGraph(2 * _count_variables(formula))

    for clause in formula:
        digraph.add_edge(_vertex(-clause[0]), _vertex(clause[1]))
        digraph.add_edge(_vertex(-clause[1]), _vertex(clause[0]))

    return digraph


def _count_variables(formula):
    """Wyliczanie liczby zmiennych występujących w formule.
    :param formula: lista klauzul
    :returns: liczba zmiennych"""
    return max({abs(var) for clause in formula for var in clause})


def _vertex(literal):
    """Wyliczanie numeru wierzchołka literału.
    :param literal: literał
    :returns: numer wierzchołka odpowiadający literałowi"""
    return 2 * literal - 2 if literal > 0 else 2 * (-literal) - 1
