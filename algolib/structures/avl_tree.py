# -*- coding: utf-8 -*-
"""AVL tree structure."""


class AVLTree:
    class _AVLNode:
        def __init__(self, element):
            self.element = element  # Value in the node
            self._height = 1  # Height of the node
            self._left = None  # Left child of the node
            self._right = None  # Right child of the node
            self._parent = None  # Parent of the node

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

            self.count_height()

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, node):
            self._right = node

            if self._right is not None:
                self._right.parent = self

            self.count_height()

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, parent):
            self._parent = parent

        def count_height(self):
            """Recounts the height of the node."""
            left_height = 0 if self._left is None else self._left.height
            right_height = 0 if self._right is None else self._right.height

            self._height = max(left_height, right_height) + 1

        def minimum(self):
            """Searches in its subtree for the node with minimal value.
            :returns: the node with minimal value"""
            return self if self._left is None else self._left.minimum()

        def maximum(self):
            """Searches in its subtree for the node with maximal value.
            :returns: the node with maximal value"""
            return self if self._right is None else self._right.maximum()

    class _AVLSuccIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            ret_elem = self._current_node.element

            if self._current_node.right is not None:
                self._current_node = self._current_node.right.minimum()
            else:
                while self._current_node.parent is not None \
                        and self._current_node.parent.left is not self._current_node:
                    self._current_node = self._current_node.parent

                self._current_node = self._current_node.parent

            return ret_elem

    class _AVLPredIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            ret_elem = self._current_node.element

            if self._current_node.left is not None:
                self._current_node = self._current_node.left.maximum()
            else:
                while self._current_node.parent is not None \
                        and self._current_node.parent.right is not self._current_node:
                    self._current_node = self._current_node.parent

                self._current_node = self._current_node.parent

            return ret_elem

    def __init__(self, elems=None):
        self._tree = None  # Root of the tree
        self._elems = 0  # Number of elements in the tree

        if elems is not None:
            for i in elems:
                self.add(i)

    def __str__(self):
        """:returns: string representation of the tree"""
        return "{|" + ", ".join([str(x) for x in self]) + "|}"

    def __iter__(self):
        """:returns: forward iterator object"""
        return self._AVLSuccIterator(self._root.minimum())

    def __reversed__(self):
        """:returns: reversed iterator object"""
        return self._AVLPredIterator(self._root.maximum())

    def __len__(self):
        """:returns: number of elements in the tree"""
        return self._elems

    def __contains__(self, element):
        """:param element: value to be found
        :returns: ``true`` if value is present in the tree, otherwise ``false``"""
        return not self.empty() and self._find_node(element,
                                                    lambda n, e: n.element == e) is not None

    def empty(self):
        """:returns: `true`` if the tree is empty, otherwise ``false``"""
        return self._elems == 0

    def add(self, element):
        """Adds a new value to the tree.
        :param element: value to be added"""
        node_parent = self._find_node(element, lambda n, e: self._search(n, e) is None
                                      or self._search(n, e).element == e)

        if node_parent is None:
            new_node = self._AVLNode(element)
            self._root = new_node
            self._elems += 1
        else:
            the_node = self._search(node_parent, element)

            if the_node is None:
                new_node = self._AVLNode(element)

                if element < node_parent.element:
                    node_parent.left = new_node
                else:
                    node_parent.right = new_node

                self._balance(new_node)
                self._elems += 1

    def remove(self, element):
        """Removes given element from the tree if present.
        :param element: value to be removed
        :raises ValueError: if given value is not present"""
        the_node = self._find_node(element, lambda n, e: n.element == e)

        if the_node is None:
            raise ValueError(f"Value {element} is not present in the tree")

        self._delete_node(the_node)

    def clear(self):
        """Removes all elements from the tree."""
        self._root = None
        self._elems = 0

    @property
    def _root(self):
        """:returns: the root of the tree"""
        return self._tree

    @_root.setter
    def _root(self, node):
        """:param node: node that will become new root of the tree"""
        self._tree = node

        if node is not None:
            self._tree.parent = None

    @staticmethod
    def _is_left_child(node):
        """:returns: ``true`` if the node is left child, otherwise ``false``"""
        return node.parent is not None and node.parent.left is node

    @staticmethod
    def _is_right_child(node):
        """:returns: ``true`` if the node is right child, otherwise ``false``"""
        return node.parent is not None and node.parent.right is node

    @staticmethod
    def _search(node, element):
        """Determines the subtree where given value might be present.
        :param node: node
        :param element: value to find
        :returns: the node if it hold given value, otherwise left child if the value is less or
        right child if the value is greater"""
        return node.left if element < node.element else \
            node.right if element > node.element else node

    def _find_node(self, element, predicate):
        """Searches for node that satisfies given predicate with given value.
        :param element: value for predicate
        :param predicate: predicate for node and argument value
        :returns: node that satisfies the predicate if any, otherwise ``None``"""
        node = self._root

        while node is not None and not predicate(node, element):
            node = AVLTree._search(node, element)

        return node

    def _delete_node(self, node):
        """Deletes inner node from the tree.
        :param node: node to be removed"""
        if node.left is not None and node.right is not None:
            succ = node.right.minimum()
            succ.element, node.element = node.element, succ.element
            self._delete_node(succ)
        else:
            child = node.left if node.left is not None else node.right

            if node.parent is not None:
                node_parent = node.parent
                self._replace_node(node, child)
                self._balance(node_parent)
            else:
                self._root = child

            self._elems -= 1

    def _replace_node(self, node1, node2):
        """Replaces the subtree rootted in one node with subtree of another node.
        :param node1: root of the subtree to be replaced
        :param node2: root of the new subtree"""
        if self._is_left_child(node1):
            node1.parent.left = node2
        elif self._is_right_child(node1):
            node1.parent.right = node2
        else:
            self._root = node2

        node1.parent = None

    def _rotate(self, node):
        """Rotates the node along the edge to its parent.
        :param node: node to be rotated"""
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
        """Restores balancing on a path from given node to the root.
        :param node: node to start balancing from"""
        while node is not None:
            node.count_height()

            if self._count_balance(node) >= 2:
                if self._count_balance(node.left) > 0:
                    self._rotate(node.left)
                elif self._count_balance(node.left) < 0:
                    self._rotate(node.left.right)
                    self._rotate(node.left)
            elif self._count_balance(node) <= -2:
                if self._count_balance(node.right) < 0:
                    self._rotate(node.right)
                elif self._count_balance(node.right) > 0:
                    self._rotate(node.right.left)
                    self._rotate(node.right)

            node = node.parent

    @staticmethod
    def _count_balance(node):
        """Counts balance of the node.
        :param node: node
        :returns: value of balance"""
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        return left_height - right_height
