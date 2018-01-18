# -*- coding: utf-8 -*-
"""DRZEWO AVL"""
from abc import ABCMeta, abstractmethod


class AVLTree:
    class _AVLNode(metaclass=ABCMeta):
        @property
        @abstractmethod
        def element(self):
            pass

        @element.setter
        @abstractmethod
        def element(self, element):
            pass

        @property
        @abstractmethod
        def height(self):
            pass

        @property
        @abstractmethod
        def left(self):
            pass

        @left.setter
        @abstractmethod
        def left(self, node):
            pass

        @property
        @abstractmethod
        def right(self):
            pass

        @right.setter
        @abstractmethod
        def right(self, node):
            pass

        @property
        @abstractmethod
        def parent(self):
            pass

        @parent.setter
        @abstractmethod
        def parent(self, node):
            pass

        @abstractmethod
        def is_left_son(self):
            """Sprawdzanie, czy węzeł jest lewym synem.
            :returns: czy węzeł to lewy syn"""

        @abstractmethod
        def is_right_son(self):
            """Sprawdzanie, czy węzeł jest prawym synem.
            :returns: czy węzeł to prawy syn"""

        @abstractmethod
        def count_balance(self):
            """Wyliczanie balansu wierzchołka.
            :returns: wartość balansu"""
            pass

        @abstractmethod
        def count_height(self):
            """Wylicza wysokość wierzchołka."""
            pass

        @abstractmethod
        def minimum(self):
            """Wyszukiwanie minimum w swoim poddrzewie.
            :returns: węzeł z minimalną wartością w poddrzewie"""
            pass

        @abstractmethod
        def maximum(self):
            """Wyszukiwanie maksimum w swoim poddrzewie.
            :returns: węzeł z maksymalną wartością w poddrzewie"""
            pass

    class _AVLInnerNode(_AVLNode):
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
            return self.parent is not None and self.parent.left is self

        def is_right_son(self):
            return self.parent is not None and self.parent.right is self

        def count_balance(self):
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            return left_height - right_height

        def count_height(self):
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            self.__height = max(left_height, right_height) + 1

        def minimum(self):
            return self if self.__left is None else self.__left.minimum()

        def maximum(self):
            return self if self.__right is None else self.__right.maximum()

    class _AVLRootNode(_AVLNode):
        def __init__(self):
            # Wewnętrzne wierzchołki.
            self.__inner = None

        @property
        def element(self):
            return None

        @element.setter
        def element(self, element):
            pass

        @property
        def height(self):
            return -1

        @property
        def left(self):
            return None

        @left.setter
        def left(self, node):
            pass

        @property
        def right(self):
            return None

        @right.setter
        def right(self, node):
            pass

        @property
        def parent(self):
            return self.__inner

        @parent.setter
        def parent(self, node):
            self.__inner = node

            if self.__inner is not None:
                self.__inner.parent = self

        def is_left_son(self):
            return False

        def is_right_son(self):
            return False

        def count_balance(self):
            return 0

        def count_height(self):
            pass

        def minimum(self):
            return self

        def maximum(self):
            return self

    class _AVLIterator:
        def __init__(self, node):
            # Aktualny węzeł.
            self._current_node = node

        def __next__(self):
            pass

        def _successor(self, node):
            """Wyznaczanie następnika węzła w drzewie.
            :param node: węzeł
            :returns: wezeł z następną wartością"""
            succ = node

            if succ.right is not None:
                return succ.right.minimum()

            while succ.height > 0 and not succ.is_left_son():
                succ = succ.parent

            return succ if succ.height <= 0 else succ.parent

        def _predecessor(self, node):
            """Wyznaczanie poprzednika węzła w drzewie.
            :param node: węzeł
            :returns: wezeł z poprzednią wartością"""
            pred = node

            if pred.left is not None:
                return pred.left.maximum()

            while pred.height > 0 and not pred.is_right_son():
                pred = pred.parent

            return pred if pred.height < 0 else pred.parent

    class _AVLSuccIterator(_AVLIterator):
        def __init__(self, node):
            super().__init__(node)

        def __next__(self):
            if self._current_node.height < 0:
                raise StopIteration

            ret_elem = self._current_node.element
            self._current_node = self._successor(self._current_node)

            return ret_elem

    class _AVLPredIterator(_AVLIterator):
        def __init__(self, node):
            super().__init__(node)

        def __next__(self):
            if self._current_node.height < 0:
                raise StopIteration

            ret_elem = self._current_node.element
            self._current_node = self._predecessor(self._current_node)

            return ret_elem

    def __init__(self, iterable=None):
        # Korzeń drzewa.
        self.__tree = AVLTree._AVLRootNode()
        # Liczba elementów drzewa.
        self.__elems = 0

        if iterable is not None:
            for i in iterable:
                self.add(i)

    def __str__(self):
        """:returns: tekstowa reprezentacja drzewa elementów"""
        return "{|" + ", ".join(map(str, self)) + "|}"

    def __iter__(self):
        """:returns: obiekt iteratora"""
        return self._AVLSuccIterator(self.__get_inner_root().minimum())

    def __reversed__(self):
        """:returns: obiekt odwróconego iteratora"""
        return self._AVLPredIterator(self.__get_inner_root().maximum())

    def __len__(self):
        """:returns: liczba elemenów drzewa"""
        return self.__elems

    def __contains__(self, element):
        """:param element: wartość do znalezienia
        :returns: czy wartość w drzewie"""
        if self.empty():
            return False

        node_parent = self.__find_node_parent(element)

        return node_parent is None or self.__get_subtree(node_parent, element) is not None

    def empty(self):
        """:returns: czy drzewo jest puste"""
        return self.__get_inner_root() is None

    def add(self, element):
        """Dodawanie elementu do drzewa.
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self.__find_node_parent(element)
        the_node = self.__get_inner_root() if node_parent is None \
            else self.__get_subtree(node_parent, element)

        if the_node is not None:
            return False

        new_node = AVLTree._AVLInnerNode(element)

        if node_parent is not None:
            if element > node_parent.element:
                node_parent.right = new_node
            else:
                node_parent.left = new_node

            self.__balance(new_node)
        else:
            self.__set_inner_root(new_node)

        self.__elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa.
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        node_parent = self.__find_node_parent(element)
        the_node = self.__get_inner_root() if node_parent is None \
            else self.__get_subtree(node_parent, element)

        if the_node is None:
            return False

        if node_parent is None:
            self.__delete_root(the_node)
        else:
            self.__delete_node(the_node)

        return True

    def clear(self):
        """Usuwanie wszystkich elementów z drzewa."""
        self.__set_inner_root(None)
        self.__elems = 0

    def __get_inner_root(self):
        """:returns: wewnętrzny korzeń drzewa"""
        return self.__tree.parent

    def __set_inner_root(self, node):
        """:param node: węzeł, który zostanie wewnętrznym korzeniem"""
        self.__tree.parent = node

    def __is_inner_root(self, node):
        """Sprawdzanie, czy węzeł jest wewnętrznym korzeniem.
        :param node: węzeł
        :returns: czy węzeł to korzeń"""
        return node.parent.height < 0

    def __get_subtree(self, node, element):
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
        tree_iter = self.__get_inner_root()
        iter_parent = None

        while tree_iter is not None and tree_iter.element != element:
            iter_parent = tree_iter
            tree_iter = self.__get_subtree(tree_iter, element)

        return iter_parent

    def __delete_root(self, root):
        """Usuwanie elementu z korzenia drzewa.
        :param root: korzeń drzewa"""
        if root.left is not None and root.right is not None:
            self.__delete_node(root)
        else:
            new_root = root.left if root.left is not None else root.right
            self.__set_inner_root(new_root)
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
        if self.__is_inner_root(node1):
            self.__set_inner_root(node2)
        elif node1.is_left_son(node1):
            node1.parent.left = node2
        elif node1.is_right_son(node1):
            node1.parent.right = node2

        node1.parent = None

    def __rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem.
        :param node: węzeł do rotacji"""
        if self.__is_inner_root(node):
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
        while node.height > 0:
            node.count_height()
            new_balance = node.count_balance()

            if new_balance >= 2:
                if node.left.count_balance() > 0:
                    self.__rotate(node.left)
                elif node.left.count_balance() < 0:
                    self.__rotate(node.left.right)
                    self.__rotate(node.left)
            elif new_balance <= -2:
                if node.right.count_balance() < 0:
                    self.__rotate(node.right)
                elif node.right.count_balance() > 0:
                    self.__rotate(node.right.left)
                    self.__rotate(node.right)

            node = node.parent
