# -*- coding: utf-8 -*-
"""Suffix array structure"""
from queue import Queue


class SuffixArray:
    def __init__(self, text):
        self._length = len(text)  # length of suffix array
        self._text = text  # text
        self._suf_arr = self._init_array()  # suffix array
        self._inv_arr = self._init_inv()  # inverted suffix array
        self._lcp_arr = self._init_lcp()  # longest common prefixes array

    @property
    def text(self):
        """:return: text for suffix array"""
        return self._text

    def __len__(self):
        """:return: length of suffix array"""
        return self._length

    def __getitem__(self, i):
        """:param i: index in suffix array
        :return: suffix"""
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._text[self._suf_arr[i]:]

    def index_at(self, i):
        """:param i: index in suffix array
        :return: index in text where the suffix begins"""
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._suf_arr[i]

    def index_of(self, suf):
        """:param suf: index in text denoting suffix
        :return: index of suffix in this array"""
        if suf < 0 or suf >= self._length:
            raise IndexError("Text index out of range")

        return self._inv_arr[suf]

    def lcp(self, suf1, suf2):
        """Counts longest common prefix of two suffixes.

        :param suf1: index in text denoting first suffix
        :param suf2: index in text denoting second suffix
        :return: length of longest common prefix"""
        if suf1 < 0 or suf1 >= self._length or suf2 < 0 or suf2 >= self._length:
            raise IndexError("Text index out of range")

        if suf1 == suf2:
            return self._length - suf1

        ix1 = min(self._inv_arr[suf1], self._inv_arr[suf2])
        ix2 = max(self._inv_arr[suf1], self._inv_arr[suf2])
        return min(self._lcp_arr[i] for i in range(ix1 + 1, ix2 + 1))

    def _init_array(self):
        return self._create_array(list(map(ord, self._text)), 128)

    def _init_inv(self):
        arr = [0] * self._length

        for i in range(0, self._length):
            arr[self._suf_arr[i]] = i

        return arr

    def _init_lcp(self):
        arr = [0] * self._length
        length = 0

        for i in range(0, self._length):
            if self._inv_arr[i] >= 1:
                j = self._suf_arr[self._inv_arr[i] - 1]

                while i + length < self._length and j + length < self._length \
                        and self._text[i + length] == self._text[j + length]:
                    length += 1

                arr[self._inv_arr[i]] = length
                length = 0 if length == 0 else length - 1

        return arr

    def _create_array(self, txt, k):
        if len(txt) < 2:
            return [0]

        lengths = (len(txt) // 3, (len(txt) + 1) // 3, (len(txt) + 2) // 3)
        lengths02 = lengths[0] + lengths[2]
        txt12 = [i for i in range(0, len(txt) + lengths[2] - lengths[1]) if i % 3 != 0]
        SuffixArray._sort_by_keys(txt12, txt, 2, k)
        SuffixArray._sort_by_keys(txt12, txt, 1, k)
        SuffixArray._sort_by_keys(txt12, txt, 0, k)
        index = 0
        last = (k, k, k)
        txt_n12 = [0] * lengths02

        for i in txt12:
            if last != (self._get(txt, i), self._get(txt, i + 1), self._get(txt, i + 2)):
                index += 1
                last = (self._get(txt, i), self._get(txt, i + 1), self._get(txt, i + 2))

            if i % 3 == 1:
                txt_n12[i // 3] = index
            else:
                txt_n12[i // 3 + lengths[2]] = index

        if index < lengths02:
            sa12 = self._create_array(txt_n12, index + 1)

            for i, suf in enumerate(sa12):
                txt_n12[suf] = i + 1
        else:
            sa12 = [0] * lengths02

            for i, ltr in enumerate(txt_n12):
                sa12[ltr - 1] = i

        sa0 = [3 * i for i in sa12 if i < lengths[2]]
        SuffixArray._sort_by_keys(sa0, txt, 0, k)
        return self._merge(txt, sa0, txt_n12, sa12)

    def _merge(self, txt0, sa0, txt12, sa12):
        sa_res = []
        lengths = (len(txt0) // 3, (len(txt0) + 1) // 3, (len(txt0) + 2) // 3)
        ix0 = 0
        ix12 = lengths[2] - lengths[1]

        while ix0 < len(sa0) and ix12 < len(sa12):
            pos12 = sa12[ix12] * 3 + 1 if sa12[ix12] < lengths[2] else \
                (sa12[ix12] - lengths[2]) * 3 + 2
            pos0 = sa0[ix0]

            if sa12[ix12] < lengths[2]:
                cond = (self._get(txt0, pos12), self._get(txt12, sa12[ix12] + lengths[2])) \
                       <= (self._get(txt0, pos0), self._get(txt12, pos0 // 3))
            else:
                cond = (self._get(txt0, pos12), self._get(txt0, pos12 + 1),
                        self._get(txt12, sa12[ix12] - lengths[2] + 1)) \
                       <= (self._get(txt0, pos0), self._get(txt0, pos0 + 1),
                           self._get(txt12, pos0 // 3 + lengths[2]))

            if cond:
                sa_res.append(pos12)
                ix12 += 1
            else:
                sa_res.append(pos0)
                ix0 += 1

        while ix12 < len(sa12):
            if sa12[ix12] < lengths[2]:
                sa_res.append(sa12[ix12] * 3 + 1)
            else:
                sa_res.append((sa12[ix12] - lengths[2]) * 3 + 2)

            ix12 += 1

        while ix0 < len(sa0):
            sa_res.append(sa0[ix0])
            ix0 += 1

        return sa_res

    @staticmethod
    def _sort_by_keys(array, keys, shift, k):
        buckets = [Queue() for i in range(k)]
        j = 0

        for i in array:
            buckets[SuffixArray._get(keys, i + shift)].put(i)

        for elem in buckets:
            while not elem.empty():
                array[j] = elem.get()
                j += 1

    @staticmethod
    def _get(array, i):
        return array[i] if i < len(array) else 0
