# -*- coding: utf-8 -*-
"""Structure of suffix array"""
from collections import deque
from math import inf


class SuffixArray:
    def __init__(self, text):
        self._length = len(text)  # length of suffix array
        self._text = text  # text
        self._suf_array = self._init_array()  # suffix array
        self._inv_array = self._init_inv()  # inverted suffix array
        self._lcp_array = self._init_lcp()  # longest common prefixes array

    @property
    def text(self):
        """:return: text for suffix array"""
        return self._text

    def __len__(self):
        """:return: length of suffix array"""
        return self._length

    def __getitem__(self, i):
        """:param i: an index in suffix array
        :return: suffix"""
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._text[self._suf_array[i]:]

    def index_at(self, i):
        """:param i: an index in suffix array
        :return: index in text where the suffix begins"""
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._suf_array[i]

    def index_of(self, suf):
        """:param suf: an index in text denoting suffix
        :return: index of suffix in this array"""
        if suf < 0 or suf >= self._length:
            raise IndexError("Text index out of range")

        return self._inv_array[suf]

    def lcp(self, suf1, suf2):
        """Counts longest common prefix of two suffixes.

        :param suf1: an index in text denoting first suffix
        :param suf2: an index in text denoting second suffix
        :return: length of longest common prefix"""
        if suf1 < 0 or suf1 >= self._length or suf2 < 0 or suf2 >= self._length:
            raise IndexError("Text index out of range")

        if suf1 == suf2:
            return self._length - suf1

        ix1 = min(self._inv_array[suf1], self._inv_array[suf2])
        ix2 = max(self._inv_array[suf1], self._inv_array[suf2])
        return min(self._lcp_array[i] for i in range(ix1 + 1, ix2 + 1))

    def _init_array(self):
        # Builds a suffix array.
        return self._create_array(list(map(ord, self._text)))

    def _init_inv(self):
        # Builds an inverted suffix array.
        arr = [0] * self._length

        for i in range(0, self._length):
            arr[self._suf_array[i]] = i

        return arr

    def _init_lcp(self):
        # Builds the LCP array.
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

    def _create_array(self, text):
        # Creates a suffix array assuming a sized alphabet.
        if len(text) < 2:
            return [0]

        lengths = (len(text) // 3, (len(text) + 1) // 3, (len(text) + 2) // 3)
        lengths02 = lengths[0] + lengths[2]
        text12 = [i for i in range(0, len(text) + lengths[2] - lengths[1]) if i % 3 != 0]
        SuffixArray._sort_by_keys(text12, text, 2)
        SuffixArray._sort_by_keys(text12, text, 1)
        SuffixArray._sort_by_keys(text12, text, 0)
        index = 0
        last = (inf, inf, inf)
        text_new12 = [0] * lengths02

        for i in text12:
            if last != (self._get(text, i), self._get(text, i + 1), self._get(text, i + 2)):
                index += 1
                last = (self._get(text, i), self._get(text, i + 1), self._get(text, i + 2))

            if i % 3 == 1:
                text_new12[i // 3] = index
            else:
                text_new12[i // 3 + lengths[2]] = index

        if index < lengths02:
            sa12 = self._create_array(text_new12)

            for i, suf in enumerate(sa12):
                text_new12[suf] = i + 1
        else:
            sa12 = [0] * lengths02

            for i, ltr in enumerate(text_new12):
                sa12[ltr - 1] = i

        sa0 = [3 * i for i in sa12 if i < lengths[2]]
        SuffixArray._sort_by_keys(sa0, text, 0)
        return self._merge(text, sa0, text_new12, sa12)

    def _merge(self, text0, sa0, text12, sa12):
        # Merges suffix arrays for two texts:
        # - text of thirds from indices giving 0 modulo 3
        # - text of thirds from indices giving 1 or 2 modulo 3
        sa_merged = []
        lengths = (len(text0) // 3, (len(text0) + 1) // 3, (len(text0) + 2) // 3)
        ix0 = 0
        ix12 = lengths[2] - lengths[1]

        while ix0 < len(sa0) and ix12 < len(sa12):
            pos12 = sa12[ix12] * 3 + 1 if sa12[ix12] < lengths[2] else \
                (sa12[ix12] - lengths[2]) * 3 + 2
            pos0 = sa0[ix0]

            if sa12[ix12] < lengths[2]:
                cond = (self._get(text0, pos12), self._get(text12, sa12[ix12] + lengths[2])) \
                       <= (self._get(text0, pos0), self._get(text12, pos0 // 3))
            else:
                cond = (self._get(text0, pos12), self._get(text0, pos12 + 1),
                        self._get(text12, sa12[ix12] - lengths[2] + 1)) \
                       <= (self._get(text0, pos0), self._get(text0, pos0 + 1),
                           self._get(text12, pos0 // 3 + lengths[2]))

            if cond:
                sa_merged.append(pos12)
                ix12 += 1
            else:
                sa_merged.append(pos0)
                ix0 += 1

        while ix12 < len(sa12):
            if sa12[ix12] < lengths[2]:
                sa_merged.append(sa12[ix12] * 3 + 1)
            else:
                sa_merged.append((sa12[ix12] - lengths[2]) * 3 + 2)

            ix12 += 1

        while ix0 < len(sa0):
            sa_merged.append(sa0[ix0])
            ix0 += 1

        return sa_merged

    @staticmethod
    def _sort_by_keys(indices, keys, shift):
        # Sorts specified array of shifted indices of specified keys from a sized alphabet.
        buckets = {}
        j = 0

        for i in indices:
            k = SuffixArray._get(keys, i + shift)

            if k not in buckets:
                buckets[k] = deque()

            buckets[k].append(i)

        for bucket in map(lambda p: p[1], sorted(buckets.items(), key=lambda p: p[0])):
            while len(bucket) > 0:
                indices[j] = bucket.popleft()
                j += 1

    @staticmethod
    def _get(array, i):
        # Retrieves element from specified index or returns zero if index is out of range.
        return array[i] if i < len(array) else 0
