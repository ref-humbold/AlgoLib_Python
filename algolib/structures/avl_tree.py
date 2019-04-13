# -*- coding: utf-8 -*-
"""AVL TREE STRUCTURE"""


class AVLTree:
    class _AVLNode:
        def __init__(self, element):
            # Wartość w węźle
            self._element = element
            # Wysokość węzła
            self._height = 1
            # Lewy syn węzła
            self._left = None
            # Prawy syn węzła
            self._right = None
            # Ojciec węzła
            self._parent = None

        @property
        def element(self):
            return self._element

        @element.setter
        def element(self, element):
            self._element = element

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

        def is_left_son(self):
            """:returns: czy węzeł to lewy syn"""
            return self.parent is not None and self.parent.left is self

        def is_right_son(self):
            """:returns: czy węzeł to prawy syn"""
            return self.parent is not None and self.parent.right is self

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
            self._current_node = self._successor(self._current_node)

            return ret_elem

        @staticmethod
        def _successor(node):
            """Wyznaczanie następnika węzła w drzewie
            :param node: węzeł
            :returns: wezeł z następną wartością"""
            succ = node

            if succ.right is not None:
                return succ.right.minimum()

            while succ is not None and not succ.is_left_son():
                succ = succ.parent

            return succ if succ is None else succ.parent

    class _AVLPredIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            ret_elem = self._current_node.element
            self._current_node = self._predecessor(self._current_node)

            return ret_elem

        @staticmethod
        def _predecessor(node):
            """Wyznaczanie poprzednika węzła w drzewie
            :param node: węzeł
            :returns: wezeł z poprzednią wartością"""
            pred = node

            if pred.left is not None:
                return pred.left.maximum()

            while pred is not None and not pred.is_right_son():
                pred = pred.parent

            return pred if pred is None else pred.parent

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
        if self.empty():
            return False

        node_parent = self._find_node_parent(element)

        return node_parent is None or AVLTree._get_subtree(node_parent, element) is not None

    def empty(self):
        """:returns: czy drzewo jest puste"""
        return self._elems == 0

    def add(self, element):
        """Dodawanie elementu do drzewa
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self._find_node_parent(element)
        the_node = self._root if node_parent is None \
            else AVLTree._get_subtree(node_parent, element)

        if the_node is not None:
            return False

        new_node = AVLTree._AVLNode(element)

        if node_parent is not None:
            if element < node_parent.element:
                node_parent.left = new_node
            else:
                node_parent.right = new_node

            self._balance(new_node)
        else:
            self._root = new_node

        self._elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        node_parent = self._find_node_parent(element)
        the_node = self._root if node_parent is None \
            else AVLTree._get_subtree(node_parent, element)

        if the_node is None:
            return False

        if node_parent is None:
            self._delete_root(the_node)
        else:
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
    def _is_root(node):
        """:param node: węzeł
        :returns: czy węzeł to korzeń"""
        return node.parent is None

    @staticmethod
    def _get_subtree(node, element):
        """Wyznaczanie poddrzewa, w którym mógłby znależć się element
        :param node: węzeł
        :param element: element
        :returns: korzeń poddrzewa, w którym znalazłby się element"""
        if element == node.element:
            return node

        if element < node.element:
            return node.left

        return node.right

    def _find_node_parent(self, element):
        """Wyszukiwanie ojca węzła z daną wartością
        :param element: wartość do znalezienia
        :returns: ojciec węzła z wartością"""
        tree_iter = self._root
        iter_parent = None

        while tree_iter is not None and tree_iter.element != element:
            iter_parent = tree_iter
            tree_iter = AVLTree._get_subtree(tree_iter, element)

        return iter_parent

    def _delete_root(self, root):
        """Usuwanie elementu z korzenia drzewa
        :param root: korzeń drzewa"""
        if root.left is not None and root.right is not None:
            self._delete_node(root)
        else:
            new_root = root.left if root.left is not None else root.right
            self._root = new_root
            self._elems -= 1

    def _delete_node(self, node):
        """Usuwanie elementu z węzła wewnętrznego drzewa
        :param node: węzeł do usunięcia"""
        if node.left is not None and node.right is not None:
            succ = node.right.minimum()
            succ.element, node.element = node.element, succ.element
            self._delete_node(succ)
        else:
            son = node.left if node.left is not None else node.right
            node_parent = node.parent

            self._replace_subtree(node, son)
            self._balance(node_parent)
            self._elems -= 1

    def _replace_subtree(self, node1, node2):
        """Zamiana poddrzewa ukorzenionego w danym węźle
        :param node1: węzeł do zamiany
        :param node2: korzeń nowego poddrzewa"""
        if AVLTree._is_root(node1):
            self._root = node2
        elif node1.is_left_son():
            node1.parent.left = node2
        elif node1.is_right_son():
            node1.parent.right = node2

        node1.parent = None

    def _rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem
        :param node: węzeł do rotacji"""
        if AVLTree._is_root(node):
            return

        upper_node = node.parent

        if node.is_right_son():
            upper_node.right = node.left
            self._replace_subtree(upper_node, node)
            node.left = upper_node
        elif node.is_left_son():
            upper_node.left = node.right
            self._replace_subtree(upper_node, node)
            node.right = upper_node

    def _balance(self, node):
        """Przywracanie balansowania na ścieżce od wierzchołka do korzenia
        :param node: wierzchołek początkowy"""
        while node is not None:
            node.count_height()

            if AVLTree._count_balance(node) >= 2:
                if AVLTree._count_balance(node.left) > 0:
                    self._rotate(node.left)
                elif AVLTree._count_balance(node.left) < 0:
                    self._rotate(node.left.right)
                    self._rotate(node.left)
            elif AVLTree._count_balance(node) <= -2:
                if AVLTree._count_balance(node.right) < 0:
                    self._rotate(node.right)
                elif AVLTree._count_balance(node.right) > 0:
                    self._rotate(node.right.left)
                    self._rotate(node.right)

            node = node.parent

    @staticmethod
    def _count_balance(node):
        """Wyliczanie balansu wierzchołka
        :param node: węzeł
        :returns: wartość balansu"""
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        return left_height - right_height
