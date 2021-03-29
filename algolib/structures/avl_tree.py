# -*- coding: utf-8 -*-
"""Structure of AVL tree"""
import collections.abc
from typing import Iterable, TypeVar

_T = TypeVar("_T")


class AVLTree(collections.abc.MutableSet):
    def __init__(self, elements: Iterable[_T] = ()):
        self._tree = None
        self._count = 0

        for i in elements:
            self.add(i)

    def __str__(self):
        """:return: string representation of the tree"""
        return f"{{|{', '.join(str(x) for x in self)}|}}"

    def __len__(self):
        """:return: number of elements in the tree"""
        return self._count

    def __iter__(self):
        """:return: a forward iterator object"""
        return self._AVLIterator(self._tree and self._tree.minimum)

    def __reversed__(self):
        """:return: a reversed iterator object"""
        return self._AVLReverseIterator(self._tree and self._tree.maximum)

    def __contains__(self, element: _T):
        """:param element: element to be checked
        :return: ``True`` if value is present in the tree, otherwise ``False``"""
        return len(self) > 0 and self._find_node(element, lambda n, e: n.element == e) is not None

    def add(self, value: _T):
        """Adds a new value to the tree.

        :param value: value to be added"""
        node_parent = self._find_node(
            value, lambda n, e: self._search(n, e) is None or self._search(n, e).element == e)

        if node_parent is None:
            new_node = self._AVLNode(value)
            self._root = new_node
            self._count += 1
        else:
            the_node = self._search(node_parent, value)

            if the_node is None:
                new_node = self._AVLNode(value)

                if value < node_parent.element:
                    node_parent.left = new_node
                else:
                    node_parent.right = new_node

                self._balance(new_node)
                self._count += 1

    def remove(self, value: _T):
        """Removes specified element from the tree.

        :param value: element to be removed
        :raises KeyError: if the element is not present"""
        the_node = self._find_node(value, lambda n, e: n.element == e)

        if the_node is None:
            raise KeyError(value)

        self._delete_node(the_node)

    def discard(self, value: _T):
        """Removes specified element from the tree if present.

        :param value: element to be removed"""
        try:
            self.remove(value)
        except KeyError:
            pass

    def pop(self):
        """Removes and returns an arbitrary element from the tree.

        :raises KeyError: if the tree is empty"""
        if self._tree is None:
            raise KeyError("pop from an empty tree")

        removed = self._tree.minimum
        self._delete_node(removed)

        return removed.element

    def clear(self):
        """Removes all elements from the tree."""
        self._root = None
        self._count = 0

    @property
    def _root(self):
        return self._tree

    @_root.setter
    def _root(self, node):
        self._tree = node

        if node is not None:
            self._tree.parent = None

    @staticmethod
    def _is_left_child(node):
        return node.parent and node.parent.left is node

    @staticmethod
    def _is_right_child(node):
        return node.parent and node.parent.right is node

    @staticmethod
    def _search(node, element):
        # Determines the subtree where given value might be present:
        # - node if element is in it
        # - left child if element is less than node's element
        # - right child if element is greater than node's element
        return node.left if element < node.element else \
            node.right if element > node.element else node

    def _find_node(self, value, predicate):
        # Searches for node that satisfies specified predicate with specified value.
        node = self._tree

        while node and not predicate(node, value):
            node = AVLTree._search(node, value)

        return node

    def _delete_node(self, node):
        # Removes inner node from the tree.
        if node.left and node.right:
            succ = node.right.minimum
            succ.element, node.element = node.element, succ.element
            self._delete_node(succ)
        else:
            child = node.left or node.right

            if node.parent is not None:
                node_parent = node.parent
                self._replace_node(node, child)
                self._balance(node_parent)
            else:
                self._root = child

            self._count -= 1

    def _replace_node(self, node1, node2):
        # Replaces the first node as a child of its parent with the second node.
        if self._is_left_child(node1):
            node1.parent.left = node2
        elif self._is_right_child(node1):
            node1.parent.right = node2
        else:
            self._root = node2

        node1.parent = None

    def _rotate(self, node):
        # Rotates the node along the edge to its parent.
        if self._is_right_child(node):
            upper_node = node.parent
            upper_node.right = node.left
            self._replace_node(upper_node, node)
            node.left = upper_node
        elif self._is_left_child(node):
            upper_node = node.parent
            upper_node.left = node.right
            self._replace_node(upper_node, node)
            node.right = upper_node

    def _balance(self, node):
        # Restores balancing on a path from specified node to the root.
        while node is not None:
            if self._count_balance(node) > 1:
                if self._count_balance(node.left) > 0:
                    self._rotate(node.left)
                elif self._count_balance(node.left) < 0:
                    self._rotate(node.left.right)
                    self._rotate(node.left)
            elif self._count_balance(node) < -1:
                if self._count_balance(node.right) < 0:
                    self._rotate(node.right)
                elif self._count_balance(node.right) > 0:
                    self._rotate(node.right.left)
                    self._rotate(node.right)

            node = node.parent

    @staticmethod
    def _count_balance(node):
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height
        return left_height - right_height

    class _AVLNode:
        def __init__(self, element):
            self.element = element  # Value in the node
            self._height = 1
            self._left = None
            self._right = None
            self._parent = None

        @property
        def height(self):
            return self._height

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, node):
            self._left = node

            if self._left is not None:
                self._left.parent = self

            self._count_height()

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, node):
            self._right = node

            if self._right is not None:
                self._right.parent = self

            self._count_height()

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, parent):
            self._parent = parent

        @property
        def minimum(self):
            # Searches in its subtree for the node with minimal value.
            return self if self._left is None else self._left.minimum

        @property
        def maximum(self):
            # Searches in its subtree for the node with maximal value.
            return self if self._right is None else self._right.maximum

        def _count_height(self):
            # Recounts the height of the node.
            left_height = 0 if self._left is None else self._left.height
            right_height = 0 if self._right is None else self._right.height
            self._height = max(left_height, right_height) + 1

    class _AVLIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            return_value = self._current_node.element

            if self._current_node.right is not None:
                self._current_node = self._current_node.right.minimum
            else:
                while self._current_node.parent is not None \
                        and self._current_node.parent.left is not self._current_node:
                    self._current_node = self._current_node.parent

                self._current_node = self._current_node.parent

            return return_value

    class _AVLReverseIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            ret_elem = self._current_node.element

            if self._current_node.left is not None:
                self._current_node = self._current_node.left.maximum
            else:
                while self._current_node.parent is not None \
                        and self._current_node.parent.right is not self._current_node:
                    self._current_node = self._current_node.parent

                self._current_node = self._current_node.parent

            return ret_elem
