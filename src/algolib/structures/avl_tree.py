# -*- coding: utf-8 -*-
"""DRZEWO AVL"""
class AVLTree:
    class _AVLNode:
        def __init__(self, element):
            self.element = element    # Wartość w węźle.
            self.parent = None    # Ojciec węzła.
            self.__left = None    # Lewy syn węzła.
            self.__right = None    # Prawy syn węzła.
            self.__height = 0    # Wysokość węzła.

        @property
        def left(self):
            """Getter dla lewego syna węzła.
            :returns: lewy syn węzła"""
            return self.__left

        @left.setter
        def left(self, node):
            """Setter dla lewego syna węzła.
            :param node: nowy syn węzła"""
            self.__left = node

            if self.__left is not None:
                self.__left.parent = self

            self.count_height()

        @property
        def right(self):
            """Getter dla prwwego syna węzła.
            :returns: prawy syn węzła"""
            return self.__right

        @right.setter
        def right(self, node):
            """Zamiana prawego dziecka węzła.
            :param node: nowy syn węzła"""
            self.__right = node

            if self.__right is not None:
                self.__right.parent = self

            self.count_height()

        @property
        def height(self):
            """Getter dla wysokości węzła.
            :returns: wysokość węzła"""
            return self.__height

        @property
        def balance(self):
            """Wyliczanie balansu wierzchołka.
            :returns: wartość balansu"""
            left_height = 0 if self.__left is None else self.__left.height
            right_height = 0 if self.__right is None else self.__right.height

            return left_height-right_height

        def is_root(self):
            """Sprawdzanie, czy węzeł jest korzeniem
            :returns: czy węzeł to korzeń"""
            return self.parent is None

        def is_left_son(self):
            """Sprawdzanie, czy węzeł jest lewym synem
            :returns: czy węzeł to lewy syn"""
            return False if self.is_root() else self.parent.left is self

        def is_right_son(self):
            """Sprawdzanie, czy węzeł jest prawym synem
            :returns: czy węzeł to prawy syn"""
            return False if self.is_root() else self.parent.right is self

        def count_height(self):
            """Wylicza wysokość wierzchołka."""
            left_height = 0 if self.left is None else self.__left.height
            right_height = 0 if self.right is None else self.__right.height

            self.__height = max(left_height, right_height)+1

        def get_subtree(self, element):
            """Wyznaczanie korzenia drzewa, w którym mógłby znależć się element.
            :param element: element do testowania
            :returns: korzeń poddrzewa, w którym znalazłby się element"""
            if element == self.element:
                return self
            elif element < self.element:
                return self.left
            else:
                return self.right

        def minimum(self):
            """Wyszukiwanie minimum w swoim poddrzewie.
            :returns: węzeł z minimalną wartością w drzewie"""
            tree_iter = self

            while tree_iter is not None and tree_iter.left is not None:
                tree_iter = tree_iter.left

            return tree_iter

        def maximum(self):
            """Wyszukiwanie maksimum w drzewie.
            :param root: korzeń drzewa
            :returns: węzeł z maksymalną wartością w drzewie"""
            tree_iter = self

            while tree_iter is not None and tree_iter.right is not None:
                tree_iter = tree_iter.right

            return tree_iter

        def successor(self):
            """Wyznaczanie następnika węzła w drzewie.
            :returns: wezeł z następną wartością"""
            succ = self

            if self.__right is not None:
                return self.__right.minimum()

            while succ is not None and succ.element <= self.element:
                succ = succ.parent

            return succ

        def predecessor(self):
            """Wyznaczanie poprzednika węzła w drzewie.
            :returns: węzeł z poprzednią wartością"""
            pred = self

            if self.__left is not None:
                return self.__left.maximum()

            while pred is not None and pred.element >= self.element:
                pred = pred.parent

            return pred

    class _Iterator:
        def __init__(self, node):
            self.__current_node = node    # aktualny węzeł

        def __next__(self):
            """Zwraca kolejną wartość w drzewie."""
            if self.__current_node is None:
                raise StopIteration
            else:
                ret_elem = self.__current_node.element
                self.__current_node = self.__current_node.successor()

                return ret_elem

    def __init__(self):
        self.__tree = None    # korzeń drzewa
        self.__elems = 0    # liczba elementów drzewa

    def __str__(self):
        """Tworzy tekstową reprezentację drzewa AVL
        :returns: tekstowa reprezentacja elementów"""
        return "{["+", ".join( map(str, self) )+"]}"

    def __iter__(self):
        """Tworzenie iteratora dla drzewa.
        :returns: obiekt iteratora"""
        return self._Iterator(self.__tree.minimum())

    def __len__(self):
        """Określanie liczby elementów drzewa.
        :returns: liczba elemenów drzewa"""
        return self.__elems

    def __contains__(self, element):
        """Sprawdzanie występowania elementu w drzewie.
        :param element: wartość do znalezienia
        :returns: czy wartość w drzewie"""
        if self.__tree is None:
            return False

        node_parent = self.__find_node_parent(element)

        return True if node_parent is None else node_parent.get_subtree(element) is not None

    def empty(self):
        """Określanie pustości drzewa.
        :returns: czy drzewo jest puste"""
        return self.__tree  is None

    def add(self, element):
        """Dodawanie elementu do drzewa.
        :param element: wartość do dodania
        :returns: czy dodano nowy element"""
        node_parent = self.__find_node_parent(element)

        if node_parent is None:
            the_node = self.__tree
        else:
            the_node = node_parent.get_subtree(element)

        if the_node is not None:
            return False

        new_node = AVLTree._AVLNode(element)
        new_node.parent = node_parent

        if node_parent is not None:
            if element > node_parent.element:
                node_parent.right = new_node
            else:
                node_parent.left = new_node

            self.__rebalance(node_parent)
        else:
            self.__tree = new_node

        self.__elems += 1

        return True

    def remove(self, element):
        """Usuwanie elementu z drzewa.
        :param element: wartość do usunięcia
        :returns: czy element został usunięty"""
        node_parent = self.__find_node_parent(element)

        if node_parent is None:
            the_node = self.__tree
        else:
            the_node = node_parent.get_subtree(element)

        if the_node is None:
            return False

        if node_parent is None:
            self.__delete_root(the_node)
        else:
            self.__delete_node(the_node)

        return True

    def clear(self):
        """Usuwanie wszystkich elementów z drzewa."""
        self.__tree = None
        self.__elems = 0

    def __find_node_parent(self, element):
        """Wyszukiwanie ojca węzła z daną wartością.
        :param element: wartość do znalezienia
        :returns: ojciec węzła z wartością"""
        tree_iter = self.__tree
        iter_parent = None

        while tree_iter is not None:
            if tree_iter.element == element:
                break
            else:
                iter_parent = tree_iter
                tree_iter = tree_iter.get_subtree(element)

        return iter_parent

    def __delete_root(self, root):
        """Usuwanie elementu z korzenia drzewa.
        :param root: korzeń drzewa"""
        if root.left is not None and root.right is not None:
            self.__delete_node(root)
        elif root.left is not None and root.right is None:
            root.left.element, root.element = root.element, root.left.element
            root.left.parent = None
            root.left = None
            self.__elems -= 1
        elif root.left is None and root.right is not None:
            root.right.element, root.element = root.element, root.right.element
            root.right.parent = None
            root.right = None
            self.__elems -= 1
        else:
            self.clear()

    def __delete_node(self, node):
        """Usuwanie elementu z węzła wewnętrznego drzewa.
        :param node: węzeł do usunięcia"""
        if node.left is not None and node.right is not None:
            succ = node.successor()
            succ.element, node.element = node.element, succ.element
            self.__delete_node(succ)
        else:
            son = node.left if node.left is not None else node.right
            node_parent = node.parent

            self.__replace_subtree(node, son)
            self.__rebalance(node_parent)
            self.__elems -= 1

    def __replace_subtree(self, node, root):
        """Zamiana poddrzewa ukorzenionego w danym węźle
        :param node: węzeł do zamiany
        :param root: korzeń nowego poddrzewa"""
        if node.parent is not None:
            if node.is_left_son():
                node.parent.left = root
            else:
                node.parent.right = root

            node.parent = None

    def __rotate(self, node):
        """Rotowanie węzła wzdłuż krawędzi z jego ojcem.
        :param node: węzeł do rotacji"""
        node_parent = node.parent
        self.__replace_subtree(node_parent, node)

        if node.is_left_son():
            node_parent.right = node.left
            node.left = node_parent
        elif node.is_right_son():
            node_parent.left = node.right
            node.right = node_parent

    def __rebalance(self, node):
        """Przywracanie balansowania na ścieżce od wierzchołka do korzenia.
        :param node: wierzchołek początkowy"""
        node.count_height()
        new_balance = node.balance

        while node is not None and node.parent is not None:
            if new_balance >= 2:
                if node.left.balance > 0:
                    self.__rotate(node.left)
                elif node.left.balance < 0:
                    self.__rotate(node.left.right)
                    self.__rotate(node.left)
            elif new_balance <= -2:
                if node.right.balance < 0:
                    self.__rotate(node.right)
                elif node.right.balance > 0:
                    self.__rotate(node.right.left)
                    self.__rotate(node.right)

            node = node.parent
