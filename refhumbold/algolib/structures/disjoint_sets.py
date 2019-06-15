# -*- coding: utf-8 -*-
"""Disjoint sets structure (union-find)."""


class DisjointSets:
    def __init__(self, universe=None):
        # Dict of represents.
        self._represents = {} if universe is None else {e: e for e in universe}
        self._sets = len(self._represents)  # Number of sets.

    def __len__(self):
        """:returns: number of sets"""
        return self._sets

    def __contains__(self, element):
        """:param element: element
        :returns: `true` if the element is included in one of sets, otherwise `false`"""
        return element in self._represents

    def __iadd__(self, elements):
        """Adds elements as singleton sets.
        :param elements: sequence of elements"""
        self.add(elements)
        return self

    def add(self, elements):
        """Adds elements as singleton sets.
        :param elements: sequence of elements"""
        elems = tuple(elements)

        for elem in elems:
            if elem in self:
                raise ValueError(f"Value {elem} already present.")

        for elem in elems:
            self._represents[elem] = elem
            self._sets += 1

    def find_set(self, element):
        """Finds a represent of the element.
        :param element: element
        :returns: represent of the element"""
        if self._represents[element] != element:
            self._represents[element] = self.find_set(self._represents[element])

        return self._represents[element]

    def union_set(self, element1, element2):
        """Joins two sets together.
        :param element1: element from the first set
        :param element2: element from the second set"""
        if not self.is_same_set(element1, element2):
            self._represents[self.find_set(element2)] = self.find_set(element1)
            self._sets -= 1

    def is_same_set(self, element1, element2):
        """Check whether two elements belong to the same set.
        :param element1: element from the former set
        :param element2: element from the second set
        :returns: `true` if both elements are in the same set, otherwise `false`"""
        return self.find_set(element1) == self.find_set(element2)
