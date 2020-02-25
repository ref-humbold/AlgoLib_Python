# -*- coding: utf-8 -*-
"""Disjoint sets structure (union-find)"""


class DisjointSets:
    def __init__(self, universe=None):
        self._represents = \
            {} if universe is None else {e: e for e in universe}  # Dict of represents
        self._sets = len(self._represents)  # Number of sets

    def __len__(self):
        """:returns: number of sets"""
        return self._sets

    def __contains__(self, element):
        """:param element: element to be found
        :returns: ``true`` if the element is included in one of sets, otherwise ``false``"""
        return element in self._represents

    def __getitem__(self, element):
        """Finds a represent of an element
        :param element: an element
        :returns: the represent of the element
        :raises KeyError: if element is not in this structure"""
        if self._represents[element] != element:
            self._represents[element] = self.__getitem__(self._represents[element])

        return self._represents[element]

    def __setitem__(self, element1, element2):
        """Joins two sets together
        :param element1: element from the first set
        :param element2: element from the second set
        :returns: a joined set represent
        :raises KeyError: if either element is not in this structure"""
        if not self.is_same_set(element1, element2):
            self._represents[self.__getitem__(element2)] = self.__getitem__(element1)
            self._sets -= 1

        return self.__getitem__(element1)

    def __iadd__(self, elements):
        """Adds elements as singleton sets
        :param elements: a sequence of elements
        :returns: ``self``
        :raises ValueError: if any of the elements is already in this structure"""
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
        :param elements: a sequence of elements
        :raises ValueError: if any of the elements is already in this structure
        :returns: ``self`` for method chaining"""
        self.__iadd__(elements)
        return self

    def find_set(self, element, default=None):
        """Finds a represent of the element
        :param element: an element
        :param default: a value to return if the element not inside
        :returns: the represent of the element"""
        try:
            return self.__getitem__(element)
        except KeyError:
            return default

    def union_set(self, element1, element2):
        """Joins two sets together
        :param element1: element from the first set
        :param element2: element from the second set
        :returns: ``self`` for method chaining
        :raises KeyError: if either element is not in this structure"""
        self.__setitem__(element1, element2)
        return self

    def is_same_set(self, element1, element2):
        """Checks whether two elements belong to the same set
        :param element1: a first element
        :param element2: a second element
        :returns: ``true`` if both elements are in the same set, otherwise ``false``
        :raises KeyError: if either element is not in this structure"""
        return self.__getitem__(element1) == self.__getitem__(element2)
