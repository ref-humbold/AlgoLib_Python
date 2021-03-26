# -*- coding: utf-8 -*-
"""Structure of trie tree"""


class Trie:
    def __init__(self):
        self._tree = self._TrieNode()
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, text: str):
        node = self._tree

        for character in text:
            node = node[character]

            if node is not None:
                return False

        return node.terminus

    def add(self, text: str):
        node = self._tree

        for character in text:
            node[character] = self._TrieNode()
            node = node[character]

        if not node.terminus:
            self._size += 1
            node.terminus = True

    def remove(self, text: str):
        self._remove_node(text, self._tree, 0)

    def discard(self, text: str):
        try:
            self.remove(text)
        except KeyError:
            pass

    def _remove_node(self, text: str, node: "Trie._TrieNode", i: int) -> bool:
        if i == len(text) and node.terminus:
            self._size -= 1
            node.terminus = False
        elif i < len(text):
            next_node = node[text[i]]

            if next_node is not None and self._remove_node(text, next_node, i + 1):
                del node[text[i]]

        return not node.terminus and node.empty()

    class _TrieNode:
        def __init__(self):
            self.terminus = False
            self._children = {}

        def __getitem__(self, char: str) -> "Trie._TrieNode":
            return self._children.get(char, None)

        def __setitem__(self, char: str, node: "Trie._TrieNode"):
            if char not in self._children:
                self._children[char] = node

        def __delitem__(self, char: str):
            del self._children[char]

        def empty(self) -> bool:
            return len(self._children) == 0
