# -*- coding: utf-8 -*-
"""Structure of double heap"""
import collections.abc
from typing import Iterable, Optional, TypeVar

_T = TypeVar("_T")


class DoubleHeap(collections.abc.Sized):
    _INDEX_FRONT = 0
    _INDEX_BACK = 1

    def __init__(self, elements: Optional[Iterable[_T]] = None, key=None):
        self._heap = []
        self._key = key if key is not None else lambda x: x

        if elements is not None:
            for e in elements:
                self.push(e)

    def __len__(self):
        return len(self._heap)

    @property
    def left(self) -> _T:
        """Retrieves minimal element from this double heap.

        :return: minimal element
        :raise KeyError: if double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_FRONT]

    @property
    def right(self) -> _T:
        """Retrieves maximal element from this double heap.

        :return: maximal element
        :raise KeyError: if double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_BACK] if len(self._heap) > 1 else \
            self._heap[self._INDEX_FRONT]

    def push(self, element: _T):
        """Adds new value to this double heap.

        :param element: value to be added
        """
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

        :return: removed minimal element
        :raise KeyError: if double heap is empty
        """
        minimal = self.left

        self._heap[self._INDEX_FRONT] = self._heap[-1]
        del self._heap[-1]
        self._move_to_right(self._INDEX_FRONT)

        return minimal

    def popright(self) -> _T:
        """Retrieves and removes maximal element from this double heap.

        :return: removed maximal element
        :raise KeyError: if double heap is empty
        """
        if len(self) == 1:
            return self.popleft()

        maximal = self.right
        self._heap[self._INDEX_BACK] = self._heap[-1]
        del self._heap[-1]
        self._move_to_left(self._INDEX_BACK)

        return maximal

    def clear(self):
        """Removes all elements from this double heap."""
        self._heap = []

    def _move_to_left(self, index):
        if index == self._INDEX_FRONT:
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
        if self._key(self._heap[index]) < self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = self._heap[next_index], self._heap[index]
            self._move_to_left(next_index)

    def _move_to_right(self, index):
        if index == self._INDEX_BACK:
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
        if self._key(self._heap[index]) > self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = self._heap[next_index], self._heap[index]
            self._move_to_right(next_index)
