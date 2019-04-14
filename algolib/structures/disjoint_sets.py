# -*- coding: utf-8 -*-
"""Disjoint sets structure (union-find)"""


class DisjointSets:
    def __init__(self, universe=None):
        # Słownik reprezentantów elementów.
        self._represents = {} if universe is None else {e: e for e in universe}
        # Liczba zbiorów.
        self._elems = len(self._represents)

    def __len__(self):
        """:returns: liczba zbiorów"""
        return self._elems

    def __contains__(self, element):
        """:param element: element
        :returns: czy element w jednym ze zbiorów"""
        return element in self._represents

    def add_elem(self, element):
        """Dodawanie nowego elementu jako singleton
        :param element: nowy element
        :returns: struktura (dla łańcucha metod)"""
        if element in self:
            raise ValueError("Value {0} already present.".format(element))

        self._represents[element] = element
        self._elems += 1

        return self

    def find_set(self, element):
        """Ustalanie reprezentanta zbioru
        :param element: element ze zbioru
        :returns: reprezentant elementu"""
        if self._represents[element] != element:
            self._represents[element] = self.find_set(self._represents[element])

        return self._represents[element]

    def union_set(self, element1, element2):
        """Scalanie dwóch zbiorów
        :param element1: element pierwszego zbioru
        :param element2: element drugiego zbioru"""
        if not self.is_same_set(element1, element2):
            self._represents[self.find_set(element2)] = self.find_set(element1)
            self._elems -= 1

    def is_same_set(self, element1, element2):
        """Sprawdzanie, czy elementy należą do tego samego zbioru
        :param element1: element pierwszego zbioru
        :param element2: element drugiego zbioru
        :returns: czy elementy znajdują się w jednym zbiorze"""
        return self.find_set(element1) == self.find_set(element2)
