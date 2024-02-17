# -*- coding: utf-8 -*-
"""Structure of double heap."""
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterable, Iterator, Reversible, Sized
from typing import List, TypeVar

_T = TypeVar("_T")


class DoubleHeap(Sized, Reversible):
    _INDEX_MIN = 0
    _INDEX_MAX = 1

    def __init__(self, elements: Iterable[_T] = (), key=None):
        self._heap = []
        self._key = key if key is not None else lambda x: x

        for e in elements:
            self.append(e)

    def __len__(self):
        """Gets the number of elements in this heap.

        :return: the number of elements"""
        return len(self._heap)

    def __iter__(self):
        """Get the forward iterator of this heap.

        :return: the forward iterator object"""
        return self._HeapIterator(self._heap)

    def __reversed__(self):
        """Get the reversed iterator of this heap.

        :return: the reversed iterator object"""
        return self._HeapReversedIterator(self._heap)

    def clear(self):
        """Removes all elements from this heap."""
        self._heap = []

    @property
    def left(self) -> _T:
        """Retrieves minimal element from this heap.

        :return: the minimal element
        :raise KeyError: if this heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_MIN]

    @property
    def right(self) -> _T:
        """Retrieves maximal element from this heap.

        :return: the maximal element
        :raise KeyError: if this heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_MAX] if len(self._heap) > 1 else \
            self._heap[self._INDEX_MIN]

    def append(self, element: _T):
        """Adds new element to this heap.

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
        """Retrieves and removes minimal element from this heap.

        :return: the removed minimal element
        :raise KeyError: if this heap is empty"""
        minimal = self.left

        self._heap[self._INDEX_MIN] = self._heap[-1]
        del self._heap[-1]
        self._move_to_right(self._INDEX_MIN)

        return minimal

    def popright(self) -> _T:
        """Retrieves and removes maximal element from this heap.

        :return: the removed maximal element
        :raise KeyError: if this heap is empty"""
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

    class _AbstractHeapIterator(ABC, Iterator):
        def __init__(self, heap):
            self._order_queue = self._initialize(heap)

        def __next__(self):
            if len(self._order_queue) == 0:
                raise StopIteration()

            return self._order_queue.popleft()

        @abstractmethod
        def _initialize(self, heap: List[_T]):
            pass

        @staticmethod
        def _create_ordered_minimal_list(heap: List[_T]):
            indices = deque()
            minimal_list = []

            if len(heap) > 0:
                indices.append(DoubleHeap._INDEX_MIN)

            while len(indices) > 0:
                index = indices.popleft()
                minimal_list.append(heap[index])

                if index + index + 2 < len(heap):
                    indices.append(index + index + 2)

                if index + index + 4 < len(heap):
                    indices.append(index + index + 4)

            return minimal_list

        @staticmethod
        def _create_ordered_maximal_list(heap: List[_T]):
            indices = deque()
            minimal_list = []

            if len(heap) > DoubleHeap._INDEX_MAX:
                indices.append(DoubleHeap._INDEX_MAX)

            while len(indices) > 0:
                index = indices.popleft()
                minimal_list.append(heap[index])

                if index + index + 1 < len(heap):
                    indices.append(index + index + 1)

                if index + index + 3 < len(heap):
                    indices.append(index + index + 3)

            return minimal_list

    class _HeapIterator(_AbstractHeapIterator):
        def _initialize(self, heap: List[_T]):
            minimal_list = self._create_ordered_minimal_list(heap)
            maximal_list = self._create_ordered_maximal_list(heap)
            order_queue = deque()
            order_queue.extend(minimal_list)
            order_queue.extend(reversed(maximal_list))
            return order_queue

    class _HeapReversedIterator(_AbstractHeapIterator):
        def _initialize(self, heap: List[_T]):
            minimal_list = self._create_ordered_minimal_list(heap)
            maximal_list = self._create_ordered_maximal_list(heap)
            order_queue = deque()
            order_queue.extend(maximal_list)
            order_queue.extend(reversed(minimal_list))
            return order_queue
