# -*- coding: utf-8 -*-
"""Structure of leftist heap."""
from collections import deque
from typing import Iterable, Optional, Sized, TypeVar

_T = TypeVar("_T")


class LeftistHeap(Sized, Iterable):
    def __init__(self, elements=()):
        self._heap = None
        self._size = 0

        for e in elements:
            self.append(e)

    def __len__(self):
        """Gets the number of elements in this heap.

        :return: the number of elements"""
        return self._size

    def __iter__(self):
        """Gets the iterator of this heap.

        :return: the iterator object"""
        nodes_stack = deque([self._heap] if self._heap is not None else [])

        while len(nodes_stack) > 0:
            node = nodes_stack.pop()
            yield node.element

            if node.left is not None:
                nodes_stack.append(node.left)

            if node.right is not None:
                nodes_stack.append(node.right)

    def __add__(self, other: "LeftistHeap") -> "LeftistHeap":
        """Merges this heap and given heap to new heap.

        :param other: the heap
        :return: merged heap"""
        new_heap = LeftistHeap()
        new_heap._heap = self._heap + other._heap
        new_heap._size = len(self) + len(other)
        return new_heap

    def __iadd__(self, other: "LeftistHeap"):
        """Merges given heap to this heap.

        :param other: the heap"""
        self._heap += other._heap
        self._size += len(other)
        return self

    def clear(self):
        """Removes all elements from this heap."""
        self._heap = None
        self._size = 0

    @property
    def head(self) -> _T:
        """Retrieves minimal element from this heap.

        :return: the minimal element
        :raise KeyError: if this heap is empty"""
        if self._heap is None:
            raise KeyError("heap is empty")

        return self._heap.element

    def append(self, element: _T):
        """Adds new element to this heap.

        :param element: the new element"""
        self._heap += self._HeapNode(element)
        self._size += 1

    def pop(self) -> _T:
        """Retrieves and removes minimal element from this heap.

        :return: the removed minimal element
        :raise KeyError: if this heap is empty"""
        if self._heap is None:
            raise KeyError("Pairing heap is empty")

        value = self._heap.element
        self._heap = self._heap.pop()
        self._size -= 1
        return value

    class _HeapNode:
        def __init__(self,
                     element: _T,
                     node1: Optional["LeftistHeap._HeapNode"] = None,
                     node2: Optional["LeftistHeap._HeapNode"] = None):
            self.rank = 0
            self.element = element

            rank1 = node1.rank if node1 is not None else 0
            rank2 = node2.rank if node2 is not None else 0

            if rank1 < rank2:
                self.rank = rank1 + 1
                self.left = node2
                self.right = node1
            else:
                self.rank = rank2 + 1
                self.left = node1
                self.right = node2

        def __add__(self, node: Optional["LeftistHeap._HeapNode"]):
            if node is None:
                return self

            return LeftistHeap._HeapNode(self.element, self.left, self.right + node) \
                if self.element < node.element else \
                LeftistHeap._HeapNode(node.element, node.left, node.right + self)

        __radd__ = __add__

        def pop(self):
            return self.left + self.right
