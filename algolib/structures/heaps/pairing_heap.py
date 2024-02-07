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
        """Gets the number of elements in this heap.

        :return: the number of elements"""
        return self._size

    def __iter__(self):
        """Gets the iterator of this heap.

        :return: the iterator object"""
        nodes_queue = deque([self._heap] if self._heap is not None else [])

        while len(nodes_queue) > 0:
            node = nodes_queue.popleft()
            yield node.element

            if node.children is not None:
                nodes_queue.extend(node.children)

    def __add__(self, other: "PairingHeap") -> "PairingHeap":
        """Merges this heap and given heap to new heap.

        :param other: the heap
        :return: merged heap"""
        new_heap = PairingHeap()
        new_heap._heap = self._heap + other._heap
        new_heap._size = len(self) + len(other)
        return new_heap

    def __iadd__(self, other: "PairingHeap"):
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
        self._heap = self._HeapNode(element) if self._heap is None else self._heap.append(element)
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

    class _HeapNodeList(Iterable):
        def __init__(self,
                     node: "PairingHeap._HeapNode",
                     next_: Optional["PairingHeap._HeapNodeList"] = None):
            self.node = node
            self.next = next_

        def __iter__(self):
            yield self.node

            if self.next is not None:
                yield from self.next

    class _HeapNode:
        def __init__(self, element: _T, children: Optional["PairingHeap._HeapNodeList"] = None):
            self.element = element
            self.children = children

        def __add__(self, node: Optional["PairingHeap._HeapNode"]) \
                -> Optional["PairingHeap._HeapNode"]:
            if node is None:
                return self

            return PairingHeap._HeapNode(self.element,
                                         PairingHeap._HeapNodeList(node, self.children)) \
                if self.element <= node.element else \
                PairingHeap._HeapNode(node.element, PairingHeap._HeapNodeList(self, node.children))

        __radd__ = __add__

        def append(self, item: _T) -> "PairingHeap._HeapNode":
            return PairingHeap._HeapNode(self.element,
                                         PairingHeap._HeapNodeList(
                                             PairingHeap._HeapNode(item), self.children)) \
                if self.element <= item else \
                PairingHeap._HeapNode(item, PairingHeap._HeapNodeList(self))

        def pop(self) -> "PairingHeap._HeapNode":
            return self.__merge_pairs(self.children)

        def __merge_pairs(self, list_: "PairingHeap._HeapNodeList") \
                -> Optional["PairingHeap._HeapNode"]:
            return None if list_ is None else \
                list_.node if list_.next is None else \
                    list_.node + list_.next.node + self.__merge_pairs(list_.next.next)
