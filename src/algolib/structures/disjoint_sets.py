# -*- coding: utf-8 -*-
"""STRUKTURA ZBIORÓW ROZŁĄCZNYCH UNION-FIND"""
class DisjointSets:
    def __init__(self, universe):
        self.__represents = {i : i for i in universe}    # słownik reprezentantów elementów

    def find_set(self, element):
        """Ustalanie reprezentanta składowej.
        :param element: element ze składowej
        :returns: reprezentant elementu"""
        if self.__represents[element] != element:
            self.__represents[element] = self.find_set(self.__represents[element])

        return self.__represents[element]

    def union_set(self, element1, element2):
        """Scalanie dwóch zbiorów.
        :param element1: element pierwszej składowej
        :param element2: element drugiej składowej"""
        if self.is_set_different(element1, element2):
            self.__represents[self.find_set(element1)] = self.find_set(element2)

    def is_set_different(self, element1, element2):
        """Sprawdzanie, czy elementy są w różnych składowych.
        :param element1: element pierwszej składowej
        :param element2: element drugiej składowej
        :returns: czy elementy znajdują się w różnych składowych"""
        return self.find_set(element1) != self.find_set(element2)
