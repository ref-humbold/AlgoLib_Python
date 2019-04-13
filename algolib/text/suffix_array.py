# -*- coding: utf-8 -*-
"""Suffix array structure"""
from queue import Queue


class SuffixArray:
    def __init__(self, text):
        # length of suffix array
        self._length = len(text)
        # text
        self._text = text
        # suffix array
        self._suf_arr = self._init_array()
        # inversed suffix array
        self._inv_arr = self._init_inv()
        # longest common prefices array
        self._lcp_arr = self._init_lcp()

    @property
    def text(self):
        return self._text

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._text[self._suf_arr[i]:]

    def index_at(self, i):
        if i < 0 or i >= self._length:
            raise IndexError("Suffix array index out of range")

        return self._suf_arr[i]

    def index_of(self, suf):
        if suf < 0 or suf >= self._length:
            raise IndexError("Text index out of range")

        return self._inv_arr[suf]

    def lcp(self, suf1, suf2):
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
        lng = 0

        for i in range(0, self._length):
            if self._inv_arr[i] >= 1:
                j = self._suf_arr[self._inv_arr[i] - 1]

                while i + lng < self._length and j + lng < self._length \
                        and self._text[i + lng] == self._text[j + lng]:
                    lng += 1

                arr[self._inv_arr[i]] = lng
                lng = 0 if lng == 0 else lng - 1

        return arr

    def _create_array(self, txt, k):
        if len(txt) < 2:
            return [0]

        lngs = (len(txt) // 3, (len(txt) + 1) // 3, (len(txt) + 2) // 3)
        lng02 = lngs[0] + lngs[2]
        txt12 = [i for i in range(0, len(txt) + lngs[2] - lngs[1]) if i % 3 != 0]

        SuffixArray._sort_by_keys(txt12, txt, 2, k)
        SuffixArray._sort_by_keys(txt12, txt, 1, k)
        SuffixArray._sort_by_keys(txt12, txt, 0, k)

        index = 0
        last = (k, k, k)
        txt_n12 = [0] * lng02

        for i in txt12:
            if last != (self._get_elem(txt, i), self._get_elem(txt, i + 1),
                        self._get_elem(txt, i + 2)):
                index += 1
                last = (self._get_elem(txt, i), self._get_elem(txt, i + 1),
                        self._get_elem(txt, i + 2))

            if i % 3 == 1:
                txt_n12[i // 3] = index
            else:
                txt_n12[i // 3 + lngs[2]] = index

        if index < lng02:
            sa12 = self._create_array(txt_n12, index + 1)

            for i, suf in enumerate(sa12):
                txt_n12[suf] = i + 1
        else:
            sa12 = [0] * lng02

            for i, ltr in enumerate(txt_n12):
                sa12[ltr - 1] = i

        sa0 = [3 * i for i in sa12 if i < lngs[2]]
        SuffixArray._sort_by_keys(sa0, txt, 0, k)

        return self._merge(txt, sa0, txt_n12, sa12)

    def _merge(self, txt0, sa0, txt12, sa12):
        sa_res = []
        lngs = (len(txt0) // 3, (len(txt0) + 1) // 3, (len(txt0) + 2) // 3)
        ix0 = 0
        ix12 = lngs[2] - lngs[1]

        while ix0 < len(sa0) and ix12 < len(sa12):
            pos12 = sa12[ix12] * 3 + 1 if sa12[ix12] < lngs[2] else (sa12[ix12] - lngs[2]) * 3 + 2
            pos0 = sa0[ix0]
            cond = (self._get_elem(txt0, pos12), self._get_elem(txt12, sa12[ix12] + lngs[2])) \
                <= (self._get_elem(txt0, pos0), self._get_elem(txt12, pos0 // 3)) \
                if sa12[ix12] < lngs[2] else \
                (self._get_elem(txt0, pos12), self._get_elem(txt0, pos12 + 1),
                 self._get_elem(txt12, sa12[ix12] - lngs[2] + 1)) \
                <= (self._get_elem(txt0, pos0), self._get_elem(txt0, pos0 + 1),
                    self._get_elem(txt12, pos0 // 3 + lngs[2]))

            if cond:
                sa_res.append(pos12)
                ix12 += 1
            else:
                sa_res.append(pos0)
                ix0 += 1

        while ix12 < len(sa12):
            sa_res.append(sa12[ix12] * 3 + 1 if sa12[ix12] < lngs[2]
                          else (sa12[ix12] - lngs[2]) * 3 + 2)
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
            buckets[SuffixArray._get_elem(keys, i + shift)].put(i)

        for elem in buckets:
            while not elem.empty():
                array[j] = elem.get()
                j += 1

    @staticmethod
    def _get_elem(array, i):
        return array[i] if i < len(array) else 0
