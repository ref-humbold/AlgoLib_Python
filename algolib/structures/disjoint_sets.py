# -*- coding: utf-8 -*-
"""Structure of disjoint sets (union-find)"""
from collections.abc import Container, Sized
from typing import Iterable, Optional, TypeVar

_T = TypeVar("_T")


class DisjointSets(Sized, Container):
    def __init__(self, universe: Iterable[_T] = ()):
        self._represents = {e: e for e in universe}  # Dict of represents
        self._sets = len(self._represents)  # Number of sets

    def __len__(self):
        """:return: number of sets"""
        return self._sets

    def __contains__(self, element: _T):
        """:param element: element to be checked
        :return: ``true`` if the element is included in one of sets, otherwise ``false``"""
        return element in self._represents

    def __getitem__(self, element: _T) -> _T:
        """Finds a represent of an element from the sets.

        :param element: an element
        :return: represent of the element
        :raises KeyError: if element is not in the structure"""
        if self._represents[element] != element:
            self._represents[element] = self.__getitem__(self._represents[element])

        return self._represents[element]

    def __iadd__(self, elements: Iterable[_T]):
        """Adds elements as singleton sets.

        :param elements: an iterable of elements
        :return: ``self``
        :raises ValueError: if any of the elements is already in the structure"""
        elements = tuple(elements)

        for elem in elements:
            if elem in self:
                raise ValueError(f"Value {elem} already present.")

        for elem in elements:
            self._represents[elem] = elem
            self._sets += 1

        return self

    def add(self, *elements: _T):
        """Adds elements as singleton sets.

        :param elements: elements to be added
        :raises ValueError: if any of the elements is already in the structure
        :return: ``self`` for method chaining"""
        self.__iadd__(elements)
        return self

    def find_set(self, element: _T, default: Optional[_T] = None) -> Optional[_T]:
        """Finds a represent of the element.

        :param element: an element
        :param default: a value to return if the element not inside
        :return: represent of the element"""
        try:
            return self.__getitem__(element)
        except KeyError:
            return default

    def union_set(self, element1: _T, element2: _T):
        """Joins two sets together.

        :param element1: element from the first set
        :param element2: element from the second set
        :return: ``self`` for method chaining
        :raises KeyError: if either element is not in the structure"""
        if not self.is_same_set(element1, element2):
            self._represents[self.__getitem__(element2)] = self.__getitem__(element1)
            self._sets -= 1

        return self

    def is_same_set(self, element1: _T, element2: _T) -> bool:
        """Checks whether two elements belong to the same set.

        :param element1: a first element
        :param element2: a second element
        :return: ``true`` if both elements are in the same set, otherwise ``false``
        :raises KeyError: if either element is not in the structure"""
        return self.__getitem__(element1) == self.__getitem__(element2)
