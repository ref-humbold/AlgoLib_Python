# -*- coding: utf-8 -*-
"""AVL TREE STRUCTURE"""


class AVLTree:
    class _AVLNode:
        def __init__(self, element):
            # Wartość w węźle.
            self.__element = element
            # Wysokość węzła.
            self.__height = 1
            # Lewy syn węzła.
            self.__left = None
            # Prawy syn węzła.
            self.__right = None
            # Ojciec węzła.
            self.__parent = None

        @property
        def element(self):
            return self.__element

        @element.setter
        def element(self, element):
            self.__element = element

        @property
        def height(self):
            return self.__height

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, node):
            self.__left = node

            if self.__left is not None:
                self.__left.parent = self

            self.count_height()

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, node):
            self.__right = node

            if self.__right is not None:
                self.__right.parent = self

            self.count_height()

        @property
        def parent(self):
            return self.__parent

        @parent.setter
        def parent(self, node):
            self.__parent = node

        def is_left_son(self):
            """:returns: czy węzeł to lewy syn"""
            return self.parent is not None and self.parent.left is self

        def is_right_son(self):
            """:returns: czy węzeł to prawy syn"""
            return self.parent is not None and self.parent.right is self

        def count_height(self):
            """Wyliczanie wysokość wierzchołka."""
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            self.__height = max(left_height, right_height) + 1

        def minimum(self):
            """Wyszukiwanie minimum w swoim poddrzewie.
            :returns: węzeł z minimalną wartością w poddrzewie"""
            return self if self.__left is None else self.__left.minimum()

        def maximum(self):
            """Wyszukiwanie maksimum w swoim poddrzewie.
            :returns: węzeł z maksymalną wartością w poddrzewie"""
            return self if self.__right is None else self.__right.maximum()

    class _AVLSuccIterator:
        def __init__(self, node):
            self._current_node = node

        def __next__(self):
            if self._current_node is None:
                raise StopIteration

            ret_elem = self._current_node.element
            self._current_node = self.__successor(self._current_node)

            return ret_elem

        @staticmethod
        def __successor(node):
            """Wyznaczanie następnika węzła w drzewie.
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
            self._current_node = self.__predecessor(self._current_node)

            return ret_elem

        @staticmethod
        def __predecessor(node):
            """Wyznaczanie poprzednika węzła w drzewie.
            :param node: węzeł
            :returns: wezeł z poprzednią wartością"""
            pred = node

            if pred.left is not None:
                return pred.left.maximum()

            while pred is not None and not pred.is_right_son():
                pred = pred.parent

            return pred if pred is None else pred.parent

    def __init__(self, elems=None):
        # Korzeń drzewa.
        self.__tree = None
        # Liczba elementów drzewa.
        self.__elems = 0

        if elems is not None:
            for i in elems:
                self.add(i)

    def __str__(self):
        """:returns: tekstowa reprezentacja elementów drzewa"""
        return "{|" + ", ".join([str(x) for x in self]) + "|}"

    def __iter__(self):
        """:returns: obiekt iteratora"""
        return self._AVLSuccIterator(self.__root.minimum())

    def __reversed__(self):
        """:returns: obiekt odwróconego iteratora"""
        return self._AVLPredIterator(self.__root.maximum())

    def __len__(self):
        """:returns: liczba elemenów drzewa"""
        return self.__elems

    def __contains__(self, element):
        """:param element: wartość do znalezienia
        :returns: czy wartość w drzewie"""
        if self.empty():
            return False

        node_parent = self.__find_node_parent(element)

        return node_parent is None or AVLTree.__get_subtree(node_parent, element) is not None

    def empty(self):
        """:returns: czy drzewo jest puste"""
        return self.__elems == 0

    def add(self, element):
        """Dodawanie elementu do drzewa.
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self.__find_node_parent(element)
        the_node = self.__root if node_parent is None \
            else AVLTree.__get_subtree(node_parent, element)

        if the_node is not None:
            return False

        new_node = AVLTree._AVLNode(element)

        if node_parent is not None:
            if element < node_parent.element:
                node_parent.left = new_node
            else:
                node_parent.right = new_node

            self.__balance(new_node)
        else:
            self.__root = new_node

        self.__elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa.
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        node_parent = self.__find_node_parent(element)
        the_node = self.__root if node_parent is None \
            else AVLTree.__get_subtree(node_parent, element)

        if the_node is None:
            return False

        if node_parent is None:
            self.__delete_root(the_node)
        else:
            self.__delete_node(the_node)

        return True

    def clear(self):
        """Usuwanie wszystkich elementów z drzewa."""
        self.__root = None
        self.__elems = 0

    @property
    def __root(self):
        """:returns: wewnętrzny korzeń drzewa"""
        return self.__tree

    @__root.setter
    def __root(self, node):
        """:param node: węzeł, który zostanie wewnętrznym korzeniem"""
        self.__tree = node

        if node is not None:
            self.__tree.parent = None

    @staticmethod
    def __is_root(node):
        """:param node: węzeł
        :returns: czy węzeł to korzeń"""
        return node.parent is None

    @staticmethod
    def __get_subtree(node, element):
        """Wyznaczanie poddrzewa, w którym mógłby znależć się element.
        :param node: węzeł
        :param element: element
        :returns: korzeń poddrzewa, w którym znalazłby się element"""
        if element == node.element:
            return node
        elif element < node.element:
            return node.left
        else:
            return node.right

    def __find_node_parent(self, element):
        """Wyszukiwanie ojca węzła z daną wartością.
        :param element: wartość do znalezienia
        :returns: ojciec węzła z wartością"""
        tree_iter = self.__root
        iter_parent = None

        while tree_iter is not None and tree_iter.element != element:
            iter_parent = tree_iter
            tree_iter = AVLTree.__get_subtree(tree_iter, element)

        return iter_parent

    def __delete_root(self, root):
        """Usuwanie elementu z korzenia drzewa.
        :param root: korzeń drzewa"""
        if root.left is not None and root.right is not None:
            self.__delete_node(root)
        else:
            new_root = root.left if root.left is not None else root.right
            self.__root = new_root
            self.__elems -= 1

    def __delete_node(self, node):
        """Usuwanie elementu z węzła wewnętrznego drzewa.
        :param node: węzeł do usunięcia"""
        if node.left is not None and node.right is not None:
            succ = node.right.minimum()
            succ.element, node.element = node.element, succ.element
            self.__delete_node(succ)
        else:
            son = node.left if node.left is not None else node.right
            node_parent = node.parent

            self.__replace_subtree(node, son)
            self.__balance(node_parent)
            self.__elems -= 1

    def __replace_subtree(self, node1, node2):
        """Zamiana poddrzewa ukorzenionego w danym węźle.
        :param node1: węzeł do zamiany
        :param node2: korzeń nowego poddrzewa"""
        if AVLTree.__is_root(node1):
            self.__root = node2
        elif node1.is_left_son():
            node1.parent.left = node2
        elif node1.is_right_son():
            node1.parent.right = node2

        node1.parent = None

    def __rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem.
        :param node: węzeł do rotacji"""
        if AVLTree.__is_root(node):
            return

        upper_node = node.parent

        if node.is_right_son():
            upper_node.right = node.left
            self.__replace_subtree(upper_node, node)
            node.left = upper_node
        elif node.is_left_son():
            upper_node.left = node.right
            self.__replace_subtree(upper_node, node)
            node.right = upper_node

    def __balance(self, node):
        """Przywracanie balansowania na ścieżce od wierzchołka do korzenia.
        :param node: wierzchołek początkowy"""
        while node is not None:
            node.count_height()

            if AVLTree.__count_balance(node) >= 2:
                if AVLTree.__count_balance(node.left) > 0:
                    self.__rotate(node.left)
                elif AVLTree.__count_balance(node.left) < 0:
                    self.__rotate(node.left.right)
                    self.__rotate(node.left)
            elif AVLTree.__count_balance(node) <= -2:
                if AVLTree.__count_balance(node.right) < 0:
                    self.__rotate(node.right)
                elif AVLTree.__count_balance(node.right) > 0:
                    self.__rotate(node.right.left)
                    self.__rotate(node.right)

            node = node.parent

    @staticmethod
    def __count_balance(node):
        """Wyliczanie balansu wierzchołka.
        :param node: węzeł
        :returns: wartość balansu"""
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        return left_height - right_height
