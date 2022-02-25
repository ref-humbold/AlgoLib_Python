# -*- coding: utf-8 -*-
"""Structure of pairing heap"""
from typing import Optional, Sized, TypeVar

_T = TypeVar("_T")


class PairingHeap(Sized):
    def __init__(self, elements=()):
        self._heap = None
        self._size = 0

        for e in elements:
            self.append(e)

    def __len__(self):
        """:return: number of elements in this pairing heap"""
        return self._size

    def clear(self):
        """Removes all elements from this pairing heap."""
        self._heap = None
        self._size = 0

    @property
    def head(self) -> _T:
        """Retrieves minimal element from this pairing heap.

        :return: minimal element
        :raise KeyError: if pairing heap is empty"""
        if self._heap is None:
            raise KeyError("Pairing heap is empty")

        return self._heap.element

    def append(self, element: _T):
        """Adds new value to this pairing heap.

        :param element: the value"""
        if self._heap is None:
            self._heap = self._HeapNode(element, None)
        elif element <= self._heap.element:
            self._heap = self._HeapNode(element, self._HeapNodeList(self._heap, None))
        else:
            self._heap.append(self._HeapNode(element, None))

        self._size += 1

    def pop(self) -> _T:
        """Retrieves and removes minimal element from this pairing heap.

        :return: removed minimal element
        :raise KeyError: if pairing heap is empty"""
        if self._heap is None:
            raise KeyError("Pairing heap is empty")

        value = self._heap.element
        self._heap = self._heap.pop()
        self._size -= 1
        return value

    def __or__(self, other: "PairingHeap") -> "PairingHeap":
        """Merges two pairing heaps into a new single heap.

        :param other: the pairing heap
        :return: merged pairing heap"""
        new_heap = PairingHeap()
        new_heap._heap = other._heap if self._heap is None else self._heap.merge(other._heap)
        new_heap._size = len(self) + len(other)
        return new_heap

    def __ior__(self, other: "PairingHeap"):
        """Merges given pairing heap to this heap.

        :param other: the pairing heap"""
        self._heap = other._heap if self._heap is None else self._heap.merge(other._heap)
        self._size += len(other)
        return self

    class _HeapNodeList:
        def __init__(self, node: "PairingHeap._HeapNode",
                     next_: Optional["PairingHeap._HeapNodeList"]):
            self.node = node
            self.next = next_

    class _HeapNode:
        def __init__(self, element: _T, children: Optional["PairingHeap._HeapNodeList"]):
            self.element = element
            self.children = children

        def pop(self) -> "PairingHeap._HeapNode":
            return self._merge_pairs(self.children)

        def merge(self, node: "PairingHeap._HeapNode") -> "PairingHeap._HeapNode":
            if node is None:
                return self

            if self.element <= node.element:
                self.append(node)
                return self

            return PairingHeap._HeapNode(node.element,
                                         PairingHeap._HeapNodeList(self, node.children))

        def append(self, node: "PairingHeap._HeapNode"):
            self.children = PairingHeap._HeapNodeList(node, self.children)

        def _merge_pairs(self, list_: "PairingHeap._HeapNodeList") \
                -> Optional["PairingHeap._HeapNode"]:
            if list_ is None:
                return None

            if list_.next is None:
                return list_.node

            return list_.node.merge(list_.next.node).merge(self._merge_pairs(list_.next.next))
