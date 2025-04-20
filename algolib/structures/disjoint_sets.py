# -*- coding: utf-8 -*-
"""Structure of disjoint sets (union-find)."""
from collections import Counter
from collections.abc import Container, Iterable, Sized
from typing import Optional, TypeVar

_T = TypeVar("_T")


class DisjointSets(Sized, Container):
    def __init__(self, sets: Iterable[Iterable[_T]] = ()):
        sets_list = [tuple(set(s)) for s in sets]
        self.__validate_duplicates(sets_list)

        self._represents = {e: s[0] for s in sets_list for e in s}  # Dict of represents
        self._count = len(sets_list)  # Number of sets

    def __len__(self):
        """Gets the number of sets in this structure.

        :return: the number of sets"""
        return self._count

    def clear(self):
        """Removes all sets from this structure."""
        self._represents = {}
        self._count = 0

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
        """Adds new elements as a new set.

        :param elements: the new elements
        :return: ``self``
        :raises ValueError: if any of the elements is already present"""
        return self.add(elements)

    def add(self, elements: Iterable[_T], represent: Optional[_T] = None):
        """Adds new elements as a new set or to the existing set represented by another element.

        :param elements: the new elements
        :param represent: the represent of the set, or ``None`` if creating new set
        :raises ValueError: if any of the elements is already present
        :raises KeyError: if the represent is not present
        :return: ``self`` for method chaining"""
        elements_tuple = tuple(elements)

        for element in elements_tuple:
            if element in self:
                raise ValueError(f"Value {element} already present.")

        if len(elements_tuple) > 0:
            set_represent = self._represents[represent] if represent is not None else \
                elements_tuple[0]

            for element in elements_tuple:
                self._represents[element] = set_represent

            if represent is None:
                self._count += 1

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
            self._count -= 1

        return self

    def is_same_set(self, element1: _T, element2: _T) -> bool:
        """Checks whether given elements belong to the same set.

        :param element1: the element from the first set
        :param element2: the element from the second set
        :return: ``True`` if elements are in the same set, otherwise ``False``
        :raises KeyError: if either element is not present"""
        return self[element1] == self[element2]

    @staticmethod
    def __validate_duplicates(sets_list):
        counter = Counter([e for s in sets_list for e in s])
        duplicates = [k for k, v in counter.items() if v > 1]

        if duplicates:
            raise ValueError(f"Duplicate elements found: {', '.join(map(str, duplicates))}")
