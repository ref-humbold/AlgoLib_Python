# -*- coding: utf-8 -*-
"""Structure of double heap"""


class DoubleHeap:
    _INDEX_FRONT = 0
    _INDEX_BACK = 0

    def __init__(self, elements=None, key=None):
        self._heap = []
        self._key = key if key is not None else lambda x: x

        if elements is not None:
            for e in elements:
                self.push(e)

    def __len__(self):
        return len(self._heap)

    @property
    def front(self):
        """:return: minimal element from this double heap"""
        if len(self._heap) == 0:
            raise ValueError()

        return self._heap[self._INDEX_FRONT]

    @property
    def back(self):
        """:return: maximal element from this double heap"""
        if len(self._heap) == 0:
            raise ValueError()

        return self._heap[self._INDEX_BACK] if len(self._heap) > 1 else \
            self._heap[self._INDEX_FRONT]

    def push(self, element):
        self._heap.append(element)

        if self.__len__() == 1:
            return

        index = self.__len__() - 1

        if index % 2 == 1:
            if self._key(self._heap[index - 1]) < self._key(self._heap[index]):
                self._heap[index - 1], self._heap[index] = self._heap[index], self._heap[index - 1]
                self._move_to_front(index - 1)
            else:
                self._move_to_back(index)
        else:
            self._move_to_front(index)

    def pop_front(self):
        element = self.front

        if self.__len__() == 1:
            del self._heap[-1]
        else:
            self._heap[self._INDEX_FRONT] = self._heap[-1]
            del self._heap[-1]
            self._move_from_front()

        return element

    def pop_back(self):
        element = self.back

        if self.__len__() <= 2:
            del self._heap[-1]
        else:
            self._heap[self._INDEX_BACK] = self._heap[-1]
            del self._heap[-1]
            self._move_from_back()

        return element

    def _move_to_front(self, index):
        while index > self._INDEX_FRONT:
            parent_index = (index // 2 - 1) // 2 * 2

            if self._key(self._heap[index]) < self._key(self._heap[parent_index]):
                self._heap[index], self._heap[parent_index] = \
                    self._heap[parent_index], self._heap[index]
                index = parent_index
            else:
                break

    def _move_to_back(self, index):
        while index > 1:
            parent_index = (index // 2 - 1) // 2 * 2 + 1

            if self._key(self._heap[index]) > self._key(self._heap[parent_index]):
                self._heap[index], self._heap[parent_index] = \
                    self._heap[parent_index], self._heap[index]
                index = parent_index
            else:
                break

    def _move_from_front(self):
        index = self._INDEX_FRONT
        # TODO

    def _move_from_back(self):
        index = self._INDEX_BACK
        # TODO
