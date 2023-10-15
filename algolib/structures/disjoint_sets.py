# -*- coding: utf-8 -*-
"""Structure of disjoint sets (union-find)."""
from collections.abc import Container, Sized
from typing import Iterable, Optional, TypeVar

_T = TypeVar("_T")


class DisjointSets(Sized, Container):
    def __init__(self, universe: Iterable[_T] = ()):
        self._represents = {e: e for e in universe}  # Dict of represents
        self._sets = len(self._represents)  # Number of sets

    def __len__(self):
        """Gets the number of sets in this structure.

        :return: the number of sets"""
        return self._sets

    def __contains__(self, element: _T):
        """Checks whether given element belongs to any set.

        :param element: the element
        :return: ``True`` if the element is included in one of sets, otherwise ``False``"""
        return element in self._represents

    def __getitem__(self, element: _T) -> _T:
        """Searches for represent of given element.

        :param element: the element
        :return: the represent of the element
        :raises KeyError: if element is not present"""
        if self._represents[element] != element:
            self._represents[element] = self[self._represents[element]]

        return self._represents[element]

    def __iadd__(self, elements: Iterable[_T]):
        """Adds new elements as singleton sets.

        :param elements: the new elements
        :return: ``self``
        :raises ValueError: if any of the elements is already present"""
        elements = tuple(elements)

        for elem in elements:
            if elem in self:
                raise ValueError(f"Value {elem} already present.")

        for elem in elements:
            self._represents[elem] = elem
            self._sets += 1

        return self

    def add(self, *elements: _T):
        """Adds new elements as singleton sets.

        :param elements: the new elements
        :raises ValueError: if any of the elements is already present
        :return: ``self`` for method chaining"""
        for elem in elements:
            if elem in self:
                raise ValueError(f"Value {elem} already present.")

        for elem in elements:
            self._represents[elem] = elem
            self._sets += 1

        return self

    def find_set(self, element: _T, default: Optional[_T] = None) -> Optional[_T]:
        """Searches for represent of given element.

        :param element: the element
        :param default: the value to return if element not present
        :return: the represent of the element, if present, otherwise the default value"""
        try:
            return self[element]
        except KeyError:
            return default

    def union_set(self, element1: _T, element2: _T):
        """Joins two sets together.

        :param element1: the element from the first set
        :param element2: the element from the second set
        :return: ``self`` for method chaining
        :raises KeyError: if either element is not present"""
        if not self.is_same_set(element1, element2):
            self._represents[self[element2]] = self[element1]
            self._sets -= 1

        return self

    def is_same_set(self, element1: _T, element2: _T) -> bool:
        """Checks whether given elements belong to the same set.

        :param element1: the element from the first set
        :param element2: the element from the second set
        :return: ``True`` if elements are in the same set, otherwise ``False``
        :raises KeyError: if either element is not present"""
        return self[element1] == self[element2]
