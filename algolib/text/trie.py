# -*- coding: utf-8 -*-
"""Structure of trie tree."""
from collections.abc import Container, Sized
from typing import Iterable, Optional


class Trie(Sized, Container):
    def __init__(self, texts: Optional[Iterable[str]] = None):
        self._tree = self._TrieNode()
        self._size = 0

        if texts is not None:
            for text in texts:
                self.add(text)

    def __len__(self):
        """Gets number of texts in this tree.

        :return: the number of texts"""
        return self._size

    def __contains__(self, text: object):
        """Checks whether given text belongs to this tree.

        :param text: the text
        :return: ``True`` if text is present in the trie tree, otherwise ``False``"""
        if not isinstance(text, str):
            raise TypeError(f"Type should be 'str', not '{type(text)}'")

        node = self._tree

        for character in text:
            node = node[character]

            if node is None:
                return False

        return node.terminus

    def add(self, text: str):
        """Adds new text to this tree.

        :param text: the new text """
        node = self._tree

        for character in text:
            node[character] = self._TrieNode()
            node = node[character]

        if not node.terminus:
            self._size += 1
            node.terminus = True

    def remove(self, text: str):
        """Removes given text from this tree.

        :param text: the text
        :raises KeyError: if the text is not present"""
        self._remove_node(text, self._tree, 0)

    def discard(self, text: str):
        """Removes given text from this tree, if present.

        :param text: the text"""
        try:
            self.remove(text)
        except KeyError:
            pass

    def clear(self):
        """Removes all texts from this tree."""
        self._tree = self._TrieNode()
        self._size = 0

    def _remove_node(self, text: str, node: "Trie._TrieNode", i: int) -> bool:
        # Removes node for character in text at specified index.
        if i == len(text):
            if not node.terminus:
                raise KeyError

            self._size -= 1
            node.terminus = False
        elif i < len(text):
            next_node = node[text[i]]

            if next_node is None:
                raise KeyError

            if self._remove_node(text, next_node, i + 1):
                del node[text[i]]

        return not node.terminus and node.empty()

    class _TrieNode:
        def __init__(self):
            self.terminus = False
            self._children = {}

        def __getitem__(self, char: str) -> "Trie._TrieNode":
            return self._children.get(char)

        def __setitem__(self, char: str, node: "Trie._TrieNode"):
            if char not in self._children:
                self._children[char] = node

        def __delitem__(self, char: str):
            del self._children[char]

        def empty(self) -> bool:
            return len(self._children) == 0
