# -*- coding: utf-8 -*-
"""Structure of pairing heap."""
from collections import deque
from typing import Iterable, Optional, Sized, TypeVar

_T = TypeVar("_T")


class PairingHeap(Sized, Iterable):
    def __init__(self, elements=()):
        self._heap = None
        self._size = 0

        for e in elements:
            self.append(e)

    def __len__(self):
        """Gets the number of elements in this pairing heap.

        :return: the number of elements"""
        return self._size

    def __iter__(self):
        """Get the iterator of this pairing heap.

        :return: the iterator object"""
        nodes_queue = deque()

        if self._heap is not None:
            nodes_queue.append(self._heap)

        while len(nodes_queue) > 0:
            node = nodes_queue.popleft()
            yield node.element
            nodes_queue.extend(node.children)

    def clear(self):
        """Removes all elements from this pairing heap."""
        self._heap = None
        self._size = 0

    @property
    def head(self) -> _T:
        """Retrieves minimal element from this pairing heap.

        :return: the minimal element
        :raise KeyError: if this pairing heap is empty"""
        if self._heap is None:
            raise KeyError("Pairing heap is empty")

        return self._heap.element

    def append(self, element: _T):
        """Adds new element to this pairing heap.

        :param element: the new element"""
        self._heap = self._HeapNode(element) if self._heap is None else self._heap.append(element)
        self._size += 1

    def pop(self) -> _T:
        """Retrieves and removes minimal element from this pairing heap.

        :return: the removed minimal element
        :raise KeyError: if this pairing heap is empty"""
        if self._heap is None:
            raise KeyError("Pairing heap is empty")

        value = self._heap.element
        self._heap = self._heap.pop()
        self._size -= 1
        return value

    def __or__(self, other: "PairingHeap") -> "PairingHeap":
        """Merges this and given pairing heaps into a new single heap.

        :param other: the pairing heap
        :return: merged pairing heap"""
        new_heap = PairingHeap()
        new_heap._heap = other._heap if self._heap is None else self._heap | other._heap
        new_heap._size = len(self) + len(other)
        return new_heap

    def __ior__(self, other: "PairingHeap"):
        """Merges given pairing heap to this heap.

        :param other: the pairing heap"""
        self._heap = other._heap if self._heap is None else self._heap | other._heap
        self._size += len(other)
        return self

    class _HeapNode:
        def __init__(self, element: _T, children: Iterable["PairingHeap._HeapNode"] = ()):
            self.element = element
            self.children = list(children)

        def append(self, item: _T) -> "PairingHeap._HeapNode":
            return PairingHeap._HeapNode(self.element,
                                         [PairingHeap._HeapNode(item), *self.children]) \
                if self.element <= item else \
                PairingHeap._HeapNode(item, [self])

        def pop(self) -> "PairingHeap._HeapNode":
            return self._merge_pairs(0)

        def __or__(self, node: "PairingHeap._HeapNode") -> "PairingHeap._HeapNode":
            if node is None:
                return self

            return PairingHeap._HeapNode(self.element, [node, *self.children]) \
                if self.element <= node.element else \
                PairingHeap._HeapNode(node.element, [self, *node.children])

        def _merge_pairs(self, index: int) \
                -> Optional["PairingHeap._HeapNode"]:
            if index >= len(self.children):
                return None

            if index == len(self.children) - 1:
                return self.children[index]

            return self.children[index] | self.children[index + 1] | self._merge_pairs(index + 2)
