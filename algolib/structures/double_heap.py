# -*- coding: utf-8 -*-
"""Structure of double heap"""


class DoubleHeap:
    _INDEX_FRONT = 0
    _INDEX_BACK = 1

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
        """:return: minimal element from this double heap
        :raise KeyError: if this double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_FRONT]

    @property
    def back(self):
        """:return: maximal element from this double heap
        :raise KeyError: if this double heap is empty"""
        if len(self._heap) == 0:
            raise KeyError("Double heap is empty")

        return self._heap[self._INDEX_BACK] if len(self._heap) > 1 else \
            self._heap[self._INDEX_FRONT]

    def push(self, element):
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
                self._move_to_front(index - 1)
            else:
                self._move_to_back(index)
        else:
            new_index = ((index + 1) // 2 - 1) // 2 * 2 + 1

            if self._key(self._heap[index]) > self._key(self._heap[new_index]):
                self._heap[new_index], self._heap[index] = self._heap[index], self._heap[new_index]
                self._move_to_back(new_index)
            else:
                self._move_to_front(index)

    def pop_front(self):
        """Retrieves and removes minimal element from this heap.

        :return: removed minimal element
        :raise KeyError: if this double heap is empty
        """
        minimal = self.front

        if len(self) == 1:
            del self._heap[-1]
        else:
            self._heap[self._INDEX_FRONT] = self._heap[-1]
            del self._heap[-1]
            self._move_to_back(self._INDEX_FRONT)

        return minimal

    def pop_back(self):
        """Retrieves and removes maximal element from this heap.

        :return: removed maximal element
        :raise KeyError: if this double heap is empty
        """
        maximal = self.back

        if len(self) <= 2:
            del self._heap[-1]
        else:
            self._heap[self._INDEX_BACK] = self._heap[-1]
            del self._heap[-1]
            self._move_to_front(self._INDEX_BACK)

        return maximal

    def clear(self):
        self._heap = []

    def _move_to_front(self, index):
        if index == self._INDEX_FRONT:
            return

        if index % 2 == 0:
            self._step_to_front(index, (index // 2 - 1) // 2 * 2)
        else:
            left_index = index + index + 1
            right_index = index + index + 3

            if right_index < len(self):
                child_index = left_index if \
                    self._key(self._heap[left_index]) > self._key(self._heap[right_index]) else \
                    right_index

                self._step_to_back(index, child_index)
            elif left_index < len(self):
                self._step_to_front(index, left_index)
            else:
                self._step_to_front(index, index - 1)

    def _step_to_front(self, index, next_index):
        if self._key(self._heap[index]) < self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = \
                self._heap[next_index], self._heap[index]
            self._move_to_front(next_index)

    def _move_to_back(self, index):
        if index == self._INDEX_BACK:
            return

        if index % 2 == 1:
            self._step_to_back(index, (index // 2 - 1) // 2 * 2 + 1)
        else:
            left_index = index + index + 2
            right_index = index + index + 4

            if right_index < len(self):
                child_index = left_index if \
                    self._key(self._heap[left_index]) < self._key(self._heap[right_index]) else \
                    right_index

                self._step_to_back(index, child_index)
            elif left_index < len(self):
                self._step_to_back(index, left_index)
            elif index + 1 < len(self):
                self._step_to_back(index, index + 1)

    def _step_to_back(self, index, next_index):
        if self._key(self._heap[index]) > self._key(self._heap[next_index]):
            self._heap[index], self._heap[next_index] = \
                self._heap[next_index], self._heap[index]
            self._move_to_back(next_index)
