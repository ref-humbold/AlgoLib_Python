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
            """Wyliczanie wysokość wierzchołka"""
            left_height = 0 if self._left is None else self._left.height
            right_height = 0 if self._right is None else self._right.height

            self._height = max(left_height, right_height) + 1

        def minimum(self):
            """Wyszukiwanie minimum w swoim poddrzewie
            :returns: węzeł z minimalną wartością w poddrzewie"""
            return self if self._left is None else self._left.minimum()

        def maximum(self):
            """Wyszukiwanie maksimum w swoim poddrzewie
            :returns: węzeł z maksymalną wartością w poddrzewie"""
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
        # Korzeń drzewa
        self._tree = None
        # Liczba elementów drzewa
        self._elems = 0

        if elems is not None:
            for i in elems:
                self.add(i)

    def __str__(self):
        """:returns: tekstowa reprezentacja elementów drzewa"""
        return "{|" + ", ".join([str(x) for x in self]) + "|}"

    def __iter__(self):
        """:returns: obiekt iteratora"""
        return self._AVLSuccIterator(self._root.minimum())

    def __reversed__(self):
        """:returns: obiekt odwróconego iteratora"""
        return self._AVLPredIterator(self._root.maximum())

    def __len__(self):
        """:returns: liczba elemenów drzewa"""
        return self._elems

    def __contains__(self, element):
        """:param element: wartość do znalezienia
        :returns: czy wartość w drzewie"""
        return not self.empty() and self._find_node(element,
                                                    lambda n, e: n.element == e) is not None

    def empty(self):
        """:returns: czy drzewo jest puste"""
        return self._elems == 0

    def add(self, element):
        """Dodawanie elementu do drzewa
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self._find_node(element, lambda n, e: self._search(n, e) is None
                                                            or self._search(n, e).element == e)

        if node_parent is None:
            new_node = self._AVLNode(element)
            self._root = new_node
            self._elems += 1

            return True

        the_node = self._search(node_parent, element)

        if the_node is not None:
            return False

        new_node = self._AVLNode(element)

        if element < node_parent.element:
            node_parent.left = new_node
        else:
            node_parent.right = new_node

        self._balance(new_node)
        self._elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        the_node = self._find_node(element, lambda n, e: n.element == e)

        if the_node is None:
            return False

        self._delete_node(the_node)

        return True

    def clear(self):
        """Usuwanie wszystkich elementów z drzewa"""
        self._root = None
        self._elems = 0

    @property
    def _root(self):
        """:returns: wewnętrzny korzeń drzewa"""
        return self._tree

    @_root.setter
    def _root(self, node):
        """:param node: węzeł, który zostanie wewnętrznym korzeniem"""
        self._tree = node

        if node is not None:
            self._tree.parent = None

    @staticmethod
    def _search(node, element):
        """Wyznaczanie poddrzewa, w którym mógłby znależć się element
        :param node: węzeł
        :param element: element
        :returns: korzeń poddrzewa, w którym znalazłby się element"""
        return node.left if element < node.element else \
            node.right if element > node.element else node

    @staticmethod
    def _is_left_child(node):
        """:returns: czy węzeł to lewy syn"""
        return node.parent is not None and node.parent.left is node

    @staticmethod
    def _is_right_child(node):
        """:returns: czy węzeł to prawy syn"""
        return node.parent is not None and node.parent.right is node

    @staticmethod
    def _count_balance(node):
        """Wyliczanie balansu wierzchołka
        :param node: węzeł
        :returns: wartość balansu"""
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        return left_height - right_height

    def _find_node(self, element, predicate):
        """Wyszukiwanie ojca węzła z daną wartością
        :param element: wartość do znalezienia
        :returns: ojciec węzła z wartością"""
        node = self._root

        while node is not None and not predicate(node, element):
            node = AVLTree._search(node, element)

        return node

    def _delete_node(self, node):
        """Usuwanie elementu z węzła wewnętrznego drzewa
        :param node: węzeł do usunięcia"""
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
        """Zamiana poddrzewa ukorzenionego w danym węźle
        :param node1: węzeł do zamiany
        :param node2: korzeń nowego poddrzewa"""
        if self._is_left_child(node1):
            node1.parent.left = node2
        elif self._is_right_child(node1):
            node1.parent.right = node2
        else:
            self._root = node2

        node1.parent = None

    def _rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem
        :param node: węzeł do rotacji"""
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
        """Przywracanie balansowania na ścieżce od wierzchołka do korzenia
        :param node: wierzchołek początkowy"""
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
