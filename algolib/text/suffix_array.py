# -*- coding: utf-8 -*-
"""Structure of suffix array."""
from collections import deque
from math import inf


class SuffixArray:
    def __init__(self, text: str):
        self._length = len(text)
        self._text = text
        self._suf_array = self._init_array()
        self._inv_array = self._init_inv()
        self._lcp_array = self._init_lcp()

    @property
    def text(self) -> str:
        return self._text

    def __len__(self):
        """Gets the length of this suffix array.

        :return: the length of suffix array"""
        return self._length

    def __getitem__(self, index: int) -> str:
        """Gets the text suffix at given index.

        :param index: the index in this suffix array
        :return: the text suffix at the index"""
        if index < 0 or index >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._text[self._suf_array[index]:]

    def index_at(self, index: int) -> int:
        """Searches for suffix in text for given index in this suffix array.

        :param index: the index in this suffix array
        :return: the index in text where suffix begins"""
        if index < 0 or index >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._suf_array[index]

    def index_of(self, index: int) -> int:
        """Searches for index in this suffix array for given text suffix.

        :param index: the index in text where suffix begins
        :return: the index of suffix in suffix array"""
        if index < 0 or index >= self._length:
            raise IndexError("Text index out of range")

        return self._inv_array[index]

    def lcp(self, suf1: int, suf2: int) -> int:
        """Computes length of the longest common prefix of given suffixes.

        :param suf1: the index in text where the first suffix begins
        :param suf2: the index in text where the second suffix begins
        :return: the length of longest common prefix"""
        if suf1 < 0 or suf1 >= self._length or suf2 < 0 or suf2 >= self._length:
            raise IndexError("Text index out of range")

        if suf1 == suf2:
            return self._length - suf1

        ix1 = min(self._inv_array[suf1], self._inv_array[suf2])
        ix2 = max(self._inv_array[suf1], self._inv_array[suf2])
        return min(self._lcp_array[i] for i in range(ix1 + 1, ix2 + 1))

    def _init_array(self):
        # Builds suffix array.
        return self._create_array(list(map(ord, self._text)))

    def _init_inv(self):
        # Builds inverted suffix array.
        arr = [0] * self._length

        for i in range(0, self._length):
            arr[self._suf_array[i]] = i

        return arr

    def _init_lcp(self):
        # Builds LCP array.
        arr = [0] * self._length
        length = 0

        for i in range(0, self._length):
            if self._inv_array[i] >= 1:
                j = self._suf_array[self._inv_array[i] - 1]

                while i + length < self._length and j + length < self._length \
                        and self._text[i + length] == self._text[j + length]:
                    length += 1

                arr[self._inv_array[i]] = length
                length = 0 if length == 0 else length - 1

        return arr

    def _create_array(self, txt):
        # Creates suffix array assuming sized alphabet.
        if len(txt) < 2:
            return [0]

        lengths = (len(txt) // 3, (len(txt) + 1) // 3, (len(txt) + 2) // 3)
        length02 = lengths[0] + lengths[2]
        indices12 = [i for i in range(0, len(txt) + lengths[2] - lengths[1]) if i % 3 != 0]

        SuffixArray._sort_indices(indices12, txt, 2)
        SuffixArray._sort_indices(indices12, txt, 1)
        SuffixArray._sort_indices(indices12, txt, 0)

        code = 0
        last = (inf, inf, inf)
        text12 = [0] * length02

        for i in indices12:
            elements = (self._get(txt, i), self._get(txt, i + 1), self._get(txt, i + 2))

            if last != elements:
                code += 1
                last = elements

            if i % 3 == 1:
                text12[i // 3] = code
            else:
                text12[i // 3 + lengths[2]] = code

        if code < length02:
            sa12 = self._create_array(text12)

            for i, suf in enumerate(sa12):
                text12[suf] = i + 1
        else:
            sa12 = [0] * length02

            for i, code in enumerate(text12):
                sa12[code - 1] = i

        sa0 = [3 * i for i in sa12 if i < lengths[2]]
        SuffixArray._sort_indices(sa0, txt, 0)
        return self._merge(txt, sa0, text12, sa12)

    def _merge(self, text0, sa0, text12, sa12):
        # Merges suffix arrays for two texts:
        # - text of thirds from indices giving 0 modulo 3
        # - text of thirds from indices giving 1 or 2 modulo 3
        sa_merged = []
        lengths = (len(text0) // 3, (len(text0) + 1) // 3, (len(text0) + 2) // 3)
        index0 = 0
        index12 = lengths[2] - lengths[1]

        while index0 < len(sa0) and index12 < len(sa12):
            pos12 = sa12[index12] * 3 + 1 if sa12[index12] < lengths[2] else \
                (sa12[index12] - lengths[2]) * 3 + 2
            pos0 = sa0[index0]

            if sa12[index12] < lengths[2]:
                cond = (self._get(text0, pos12), self._get(text12, sa12[index12] + lengths[2])) \
                       <= (self._get(text0, pos0), self._get(text12, pos0 // 3))
            else:
                cond = (self._get(text0, pos12), self._get(text0, pos12 + 1),
                        self._get(text12, sa12[index12] - lengths[2] + 1)) \
                       <= (self._get(text0, pos0), self._get(text0, pos0 + 1),
                           self._get(text12, pos0 // 3 + lengths[2]))

            if cond:
                sa_merged.append(pos12)
                index12 += 1
            else:
                sa_merged.append(pos0)
                index0 += 1

        while index12 < len(sa12):
            if sa12[index12] < lengths[2]:
                sa_merged.append(sa12[index12] * 3 + 1)
            else:
                sa_merged.append((sa12[index12] - lengths[2]) * 3 + 2)

            index12 += 1

        while index0 < len(sa0):
            sa_merged.append(sa0[index0])
            index0 += 1

        return sa_merged

    @staticmethod
    def _sort_indices(indices, values, shift):
        # Sorts specified array of shifted indices of specified keys from sized alphabet.
        buckets = {}
        j = 0

        for i in indices:
            val = SuffixArray._get(values, i + shift)

            if val not in buckets:
                buckets[val] = deque()

            buckets[val].append(i)

        for _, bucket in sorted(buckets.items(), key=lambda p: p[0]):
            while len(bucket) > 0:
                indices[j] = bucket.popleft()
                j += 1

    @staticmethod
    def _get(array, i):
        # Retrieves element from specified index or returns zero if index is out of range.
        return array[i] if i < len(array) else 0
