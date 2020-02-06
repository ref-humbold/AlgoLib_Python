# -*- coding: utf-8 -*-
"""Disjoint sets structure (union-find)"""


class DisjointSets:
    def __init__(self, universe=None):
        # Dict of represents
        self._represents = {} if universe is None else {e: e for e in universe}
        self._sets = len(self._represents)  # Number of sets

    def __len__(self):
        """:returns: number of sets"""
        return self._sets

    def __contains__(self, element):
        """:param element: element
        :returns: ``true`` if the element is included in one of sets, otherwise ``false``"""
        return element in self._represents

    def __getitem__(self, element):
        """Finds a represent of the element
        :param element: element
        :returns: represent of the element
        :raises KeyError: if element is not in the structure"""
        if self._represents[element] != element:
            self._represents[element] = self.__getitem__(self._represents[element])

        return self._represents[element]

    def __setitem__(self, element1, element2):
        """Joins two sets together
        :param element1: element from the first set
        :param element2: element from the second set
        :raises KeyError: if either element is not in the structure"""
        if not self.is_same_set(element1, element2):
            self._represents[self.__getitem__(element2)] = self.__getitem__(element1)
            self._sets -= 1

        return self.__getitem__(element1)

    def __iadd__(self, elements):
        """Adds elements as singleton sets
        :param elements: sequence of elements
        :raises ValueError: if any of the elements is in the structure"""
        elems = tuple(elements)

        for elem in elems:
            if elem in self:
                raise ValueError(f"Value {elem} already present.")

        for elem in elems:
            self._represents[elem] = elem
            self._sets += 1

        return self

    def add(self, elements):
        """Adds elements as singleton sets
        :param elements: sequence of elements
        :raises ValueError: if any of the elements is in the structure"""
        self.__iadd__(elements)

    def find_set(self, element, default=None):
        """Finds a represent of the element
        :param element: element
        :param default: value to return if element not inside
        :returns: represent of the element"""
        try:
            return self.__getitem__(element)
        except KeyError:
            return default

    def union_set(self, element1, element2):
        """Joins two sets together
        :param element1: element from the first set
        :param element2: element from the second set
        :raises KeyError: if either element is not in the structure"""
        self.__setitem__(element1, element2)

    def is_same_set(self, element1, element2):
        """Check whether two elements belong to the same set
        :param element1: element from the former set
        :param element2: element from the second set
        :returns: ``true`` if both elements are in the same set, otherwise ``false``
        :raises KeyError: if either element is not in the structure"""
        return self.__getitem__(element1) == self.__getitem__(element2)
