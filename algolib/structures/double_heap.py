# -*- coding: utf-8 -*-
"""Structure of double heap."""
from collections.abc import Sized
from typing import Iterable, TypeVar

_T = TypeVar("_T")


class DoubleHeap(Sized):
    _INDEX_MIN = 0
    _INDEX_MAX = 1

    def __init__(self, elements: Iterable[_T] = (), key=None):
        self._heap = []
        self._key = key if key is not None else lambda x: x

        for e in elements:
            self.append(e)

    def __len__(self):
        """Gets the number of elements in this double heap.

        :return: the number of elements"""
        return len(self._heap)

    def clear(self):
        """Removes all elements from this double heap."""
        self._heap = []

    @property
    def left(self) -> _T:
        """Retrieves minimal element from this double heap.

        :return: the minimal element
        :raise KeyError: if this double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_MIN]

    @property
    def right(self) -> _T:
        """Retrieves maximal element from this double heap.

        :return: the maximal element
        :raise KeyError: if this double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_MAX] if len(self._heap) > 1 else \
            self._heap[self._INDEX_MIN]

    def append(self, element: _T):
        """Adds new element to this double heap.

        :param element: the new element"""
        self._heap.append(element)

        if len(self) == 1:
            return

        index = len(self) - 1

        if index % 2 == 1:
            if self._key(self._heap[index]) < self._key(self._heap[index - 1]):
                self._heap[index - 1], self._heap[index] = self._heap[index], self._heap[index - 1]
                self._move_to_left(index - 1)
            else:
                self._move_to_right(index)
        else:
            new_index = ((index + 1) // 2 - 1) // 2 * 2 + 1

            if self._key(self._heap[index]) > self._key(self._heap[new_index]):
                self._heap[new_index], self._heap[index] = self._heap[index], self._heap[new_index]
                self._move_to_right(new_index)
            else:
                self._move_to_left(index)

    def popleft(self) -> _T:
        """Retrieves and removes minimal element from this double heap.

        :return: the removed minimal element
        :raise KeyError: if this double heap is empty"""
        minimal = self.left

        self._heap[self._INDEX_MIN] = self._heap[-1]
        del self._heap[-1]
        self._move_to_right(self._INDEX_MIN)

        return minimal

    def popright(self) -> _T:
        """Retrieves and removes maximal element from this double heap.

        :return: the removed maximal element
        :raise KeyError: if this double heap is empty"""
        if len(self) == 1:
            return self.popleft()

        maximal = self.right
        self._heap[self._INDEX_MAX] = self._heap[-1]
        del self._heap[-1]
        self._move_to_left(self._INDEX_MAX)

        return maximal

    def _move_to_left(self, index):
        # Moves element from given index towards minimum.
        if index == self._INDEX_MIN:
            return

        if index % 2 == 0:
            self._step_to_left(index, (index // 2 - 1) // 2 * 2)
        else:
            left_index = index + index + 1
            right_index = index + index + 3

            if right_index < len(self):
                child_index = left_index if \
                    self._key(self._heap[left_index]) > self._key(self._heap[right_index]) else \
                    right_index

                self._step_to_left(index, child_index)
            elif left_index < len(self):
                self._step_to_left(index, left_index)
            elif index < len(self):
                self._step_to_left(index, index - 1)

    def _step_to_left(self, index, next_index):
        # Performs a single step of movement towards minimum.
        if self._key(self._heap[index]) < self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = self._heap[next_index], self._heap[index]
            self._move_to_left(next_index)

    def _move_to_right(self, index):
        # Moves element from given index towards maximum.
        if index == self._INDEX_MAX:
            return

        if index % 2 == 1:
            self._step_to_right(index, (index // 2 - 1) // 2 * 2 + 1)
        else:
            left_index = index + index + 2
            right_index = index + index + 4

            if right_index < len(self):
                child_index = left_index if \
                    self._key(self._heap[left_index]) < self._key(self._heap[right_index]) else \
                    right_index

                self._step_to_right(index, child_index)
            elif left_index < len(self):
                self._step_to_right(index, left_index)
            elif index + 1 < len(self):
                self._step_to_right(index, index + 1)

    def _step_to_right(self, index, next_index):
        # Performs a single step of movement towards maximum.
        if self._key(self._heap[index]) > self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = self._heap[next_index], self._heap[index]
            self._move_to_right(next_index)
