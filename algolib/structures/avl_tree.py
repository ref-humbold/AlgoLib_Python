# -*- coding: utf-8 -*-
"""AVL tree structure"""


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
            left_height = 0 if self._left is None else self._left.height
            right_height = 0 if self._right is None else self._right.height
            self._height = max(left_height, right_height) + 1

        def minimum(self):
            return self if self._left is None else self._left.minimum()

        def maximum(self):
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
        """:return: string representation of the tree"""
        return f"{{|{', '.join(str(x) for x in self)}|}}"

    def __iter__(self):
        """:return: a forward iterator object"""
        return self._AVLSuccIterator(self._root.minimum())

    def __reversed__(self):
        """:return: a reversed iterator object"""
        return self._AVLPredIterator(self._root.maximum())

    def __len__(self):
        """:return: number of elements in this tree"""
        return self._elems

    def __contains__(self, element):
        """:param element: element to be found
        :return: ``true`` if value is present in this tree, otherwise ``false``"""
        return not self.empty() \
               and self._find_node(element, lambda n, e: n.element == e) is not None

    def empty(self):
        """:return: ``true`` if this tree is empty, otherwise ``false``"""
        return self._elems == 0

    def add(self, element):
        """Adds a new value to this tree.

        :param element: value to be added"""
        node_parent = self._find_node(
                element, lambda n, e: self._search(n, e) is None or self._search(n, e).element == e)

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
        """Removes specified element from this tree if present.

        :param element: element to be removed
        :raises ValueError: if the element is not present"""
        the_node = self._find_node(element, lambda n, e: n.element == e)

        if the_node is None:
            raise ValueError(f"Value {element} is not present in the tree")

        self._delete_node(the_node)

    def clear(self):
        """Removes all elements from this tree."""
        self._root = None
        self._elems = 0

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
        return node.parent is not None and node.parent.left is node

    @staticmethod
    def _is_right_child(node):
        return node.parent is not None and node.parent.right is node

    @staticmethod
    def _search(node, element):
        return node.left if element < node.element else \
            node.right if element > node.element else node

    def _find_node(self, element, predicate):
        node = self._root

        while node is not None and not predicate(node, element):
            node = AVLTree._search(node, element)

        return node

    def _delete_node(self, node):
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
        if self._is_left_child(node1):
            node1.parent.left = node2
        elif self._is_right_child(node1):
            node1.parent.right = node2
        else:
            self._root = node2

        node1.parent = None

    def _rotate(self, node):
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
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height
        return left_height - right_height
