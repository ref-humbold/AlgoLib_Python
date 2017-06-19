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
        def count_balance(self):
            """Wyliczanie balansu wierzchołka.
            :returns: wartość balansu"""
            pass

        @abstractmethod
        def recount_height(self):
            """Wylicza wysokość wierzchołka."""
            pass

        @abstractmethod
        def minimum(self):
            """Wyszukiwanie minimum w swoim poddrzewie.
            :returns: węzeł z minimalną wartością w drzewie"""
            pass

        @abstractmethod
        def maximum(self):
            """Wyszukiwanie maksimum w drzewie.
            :param root: korzeń drzewa
            :returns: węzeł z maksymalną wartością w drzewie"""
            pass

    class _AVLNodeElement(_AVLNode):
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

            self.recount_height()

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, node):
            self.__right = node

            if self.__right is not None:
                self.__right.parent = self

            self.recount_height()

        @property
        def parent(self):
            return self.__parent

        @parent.setter
        def parent(self, node):
            self.__parent = node

        def count_balance(self):
            """meth: AVLTree._AVLNode.count_balance"""
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            return left_height - right_height

        def recount_height(self):
            """meth: AVLTree._AVLNode.recount_height"""
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            self.__height = max(left_height, right_height) + 1

        def minimum(self):
            """meth: AVLTree._AVLNode.minimum"""
            return self if self.__left is None else self.__left.minimum()

        def maximum(self):
            """meth: AVLTree._AVLNode.maximum"""
            return self if self.__right is None else self.__right.maximum()

    class _AVLNodeNull(_AVLNode):
        def __init__(self):
            # Ojciec węzła.
            self.__parent = None

        @property
        def element(self):
            raise AttributeError

        @element.setter
        def element(self, element):
            raise AttributeError

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
            return self.__parent

        @parent.setter
        def parent(self, node):
            self.__parent = node

        def count_balance(self):
            """meth: AVLTree._AVLNode.count_balance"""
            return 0

        def recount_height(self):
            """meth: AVLTree._AVLNode.recount_height"""
            pass

        def minimum(self):
            """meth: AVLTree._AVLNode.minimum"""
            raise AttributeError

        def maximum(self):
            """meth: AVLTree._AVLNode.maximum"""
            raise AttributeError

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

            while succ.height >= 0 and succ.element <= node.element:
                succ = succ.parent

            return succ

        def _predecessor(self, node):
            """Wyznaczanie poprzednika węzła w drzewie.
            :param node: węzeł
            :returns: wezeł z poprzednią wartością"""
            pred = node

            if pred.left is not None:
                return pred.left.maximum()

            while pred.height >= 0 and pred.element >= node.element:
                pred = pred.parent

            return pred

    class _AVLFwdIterator(_AVLIterator):
        def __init__(self, node):
            super().__init__(node)

        def __next__(self):
            if self._current_node.height < 0:
                raise StopIteration

            ret_elem = self._current_node.element
            self._current_node = self._successor(self._current_node)

            return ret_elem

    class _AVLRevIterator(_AVLIterator):
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
        self.__tree = AVLTree._AVLNodeNull()
        # Liczba elementów drzewa.
        self.__elems = 0

        if iterable is not None:
            for i in iterable:
                self.add(i)

    def __str__(self):
        """Tworzy tekstową reprezentację drzewa AVL
        :returns: tekstowa reprezentacja elementów"""
        return "{|" + ", ".join(map(str, self)) + "|}"

    def __iter__(self):
        """Tworzenie iteratora dla drzewa.
        :returns: obiekt iteratora"""
        return self._AVLFwdIterator(self.__get_root().minimum())

    def __reversed__(self):
        """Tworzenie odwróconego iteratora dla drzewa.
        :returns: obiekt odwróconego iteratora"""
        return self._AVLRevIterator(self.__get_root().maximum())

    def __len__(self):
        """Określanie liczby elementów drzewa.
        :returns: liczba elemenów drzewa"""
        return self.__elems

    def __contains__(self, element):
        """Sprawdzanie występowania elementu w drzewie.
        :param element: wartość do znalezienia
        :returns: czy wartość w drzewie"""
        if self.empty():
            return False

        node_parent = self.__find_node_parent(element)

        return True if node_parent is None else self.__get_subtree(node_parent, element) is not None

    def empty(self):
        """Określanie pustości drzewa.
        :returns: czy drzewo jest puste"""
        return self.__get_root() is None

    def add(self, element):
        """Dodawanie elementu do drzewa.
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self.__find_node_parent(element)
        the_node = None

        if node_parent is None:
            the_node = self.__get_root()
        else:
            the_node = self.__get_subtree(node_parent, element)

        if the_node is not None:
            return False

        new_node = AVLTree._AVLNodeElement(element)

        if node_parent is not None:
            if element > node_parent.element:
                node_parent.right = new_node
            else:
                node_parent.left = new_node

            self.__rebalance(new_node)
        else:
            self.__set_root(new_node)

        self.__elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa.
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        node_parent = self.__find_node_parent(element)
        the_node = None

        if node_parent is None:
            the_node = self.__get_root()
        else:
            the_node = self.__get_subtree(node_parent, element)

        if the_node is None:
            return False

        if node_parent is None:
            self.__delete_root(the_node)
        else:
            self.__delete_node(the_node)

        return True

    def clear(self):
        """Usuwanie wszystkich elementów z drzewa."""
        self.__set_root(None)
        self.__elems = 0

    def __get_root(self):
        """Pobieranie własciwego korzenia drzewa
        :returns: korzeń drzewa"""
        return self.__tree.parent

    def __set_root(self, node):
        """Ustawianie węzła jako korzeń drzewa
        :param node: węzeł"""
        if node is not None:
            node.parent = self.__tree

        self.__tree.parent = node

    def __is_root(self, node):
        """Sprawdzanie, czy węzeł jest korzeniem
        :param node: węzeł
        :returns: czy węzeł to korzeń"""
        return node.parent.height < 0

    def __is_left_son(self, node):
        """Sprawdzanie, czy węzeł jest lewym synem
        :param node: węzeł
        :returns: czy węzeł to lewy syn"""
        return False if self.__is_root(node) else node.parent.left is node

    def __is_right_son(self, node):
        """Sprawdzanie, czy węzeł jest prawym synem
        :param node: węzeł
        :returns: czy węzeł to prawy syn"""
        return False if self.__is_root(node) else node.parent.right is node

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
        tree_iter = self.__get_root()
        iter_parent = None

        while tree_iter is not None:
            if tree_iter.element == element:
                break
            else:
                iter_parent = tree_iter
                tree_iter = self.__get_subtree(tree_iter, element)

        return iter_parent

    def __delete_root(self, root):
        """Usuwanie elementu z korzenia drzewa.
        :param root: korzeń drzewa"""
        if root.left is not None and root.right is not None:
            self.__delete_node(root)
        elif root.left is not None and root.right is None:
            root.left.element, root.element = root.element, root.left.element
            self.__set_root(root.left)
            root.left = None
            self.__elems -= 1
        elif root.left is None and root.right is not None:
            root.right.element, root.element = root.element, root.right.element
            self.__set_root(root.right)
            root.right = None
            self.__elems -= 1
        else:
            self.clear()

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
            self.__rebalance(node_parent)
            self.__elems -= 1

    def __replace_subtree(self, node1, node2):
        """Zamiana poddrzewa ukorzenionego w danym węźle.
        :param node1: węzeł do zamiany
        :param node2: korzeń nowego poddrzewa"""
        if self.__is_root(node1):
            self.__set_root(node2)
        elif self.__is_left_son(node1):
            node1.parent.left = node2
        elif self.__is_right_son(node1):
            node1.parent.right = node2

        node1.parent = None

    def __rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem.
        :param node: węzeł do rotacji"""
        if self.__is_root(node):
            return

        upper_node = node.parent

        if self.__is_right_son(node):
            upper_node.right = node.left
            self.__replace_subtree(upper_node, node)
            node.left = upper_node
        elif self.__is_left_son(node):
            upper_node.left = node.right
            self.__replace_subtree(upper_node, node)
            node.right = upper_node

    def __rebalance(self, node):
        """Przywracanie balansowania na ścieżce od wierzchołka do korzenia.
        :param node: wierzchołek początkowy"""
        while node.height >= 0:
            node.recount_height()
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
