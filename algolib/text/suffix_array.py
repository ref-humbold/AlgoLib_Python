# -*- coding: utf-8 -*-
"""Suffix array structure"""
from queue import Queue


class SuffixArray:
    def __init__(self, text):
        # length of suffix array
        self.__length = len(text)
        # text
        self.__text = text
        # suffix array
        self.__suf_arr = self.__init_array()
        # inversed suffix array
        self.__inv_arr = self.__init_inv()
        # longest common prefices array
        self.__lcp_arr = self.__init_lcp()

    @property
    def text(self):
        return self.__text

    def __len__(self):
        return self.__length

    def __getitem__(self, i):
        if i < 0 or i >= self.__length:
            raise IndexError("Suffix array index out of range")

        return self.__text[self.__suf_arr[i]:]

    def index_at(self, i):
        if i < 0 or i >= self.__length:
            raise IndexError("Suffix array index out of range")

        return self.__suf_arr[i]

    def index_of(self, suf):
        if suf < 0 or suf >= self.__length:
            raise IndexError("Text index out of range")

        return self.__inv_arr[suf]

    def lcp(self, suf1, suf2):
        if suf1 < 0 or suf1 >= self.__length or suf2 < 0 or suf2 >= self.__length:
            raise IndexError("Text index out of range")

        if suf1 == suf2:
            return self.__length - suf1

        i1 = min(self.__inv_arr[suf1], self.__inv_arr[suf2])
        i2 = max(self.__inv_arr[suf1], self.__inv_arr[suf2])

        return min(self.__lcp_arr[i] for i in range(i1 + 1, i2 + 1))

    def __init_array(self):
        return self.__create_array(list(map(ord, self.__text)), 128)

    def __init_inv(self):
        arr = [0] * self.__length

        for i in range(0, self.__length):
            arr[self.__suf_arr[i]] = i

        return arr

    def __init_lcp(self):
        arr = [0] * self.__length
        ln = 0

        for i in range(0, self.__length):
            if self.__inv_arr[i] >= 1:
                j = self.__suf_arr[self.__inv_arr[i] - 1]

                while i + ln < self.__length and j + ln < self.__length \
                        and self.__text[i + ln] == self.__text[j + ln]:
                    ln += 1

                arr[self.__inv_arr[i]] = ln
                ln = 0 if ln == 0 else ln - 1

        return arr

    def __create_array(self, t, k):
        if len(t) < 2:
            return [0]

        n2 = (len(t) + 2) // 3
        n1 = (len(t) + 1) // 3
        n0 = len(t) // 3
        n02 = n0 + n2
        t12 = [i for i in range(0, len(t) + n2 - n1) if i % 3 != 0]

        self.__sort_by_keys(t12, t, 2, k)
        self.__sort_by_keys(t12, t, 1, k)
        self.__sort_by_keys(t12, t, 0, k)

        ix = 0
        last0 = k
        last1 = k
        last2 = k
        tn12 = [0] * n02

        for i in t12:
            if self.__get_elem(t, i) != last0 or self.__get_elem(t, i + 1) != last1 \
                    or self.__get_elem(t, i + 2) != last2:
                ix += 1
                last0 = self.__get_elem(t, i)
                last1 = self.__get_elem(t, i + 1)
                last2 = self.__get_elem(t, i + 2)

            if i % 3 == 1:
                tn12[i // 3] = ix
            else:
                tn12[i // 3 + n2] = ix

        if ix < n02:
            sa12 = self.__create_array(tn12, ix + 1)

            for i in range(0, len(sa12)):
                tn12[sa12[i]] = i + 1
        else:
            sa12 = [0] * n02

            for i in range(0, len(tn12)):
                sa12[tn12[i] - 1] = i

        sa0 = [3 * i for i in sa12 if i < n2]
        self.__sort_by_keys(sa0, t, 0, k)

        return self.__merge(t, sa0, tn12, sa12)

    def __merge(self, t0, sa0, t12, sa12):
        sa = []
        n2 = (len(t0) + 2) // 3
        n1 = (len(t0) + 1) // 3
        i0 = 0
        i12 = n2 - n1

        while i0 < len(sa0) and i12 < len(sa12):
            pos12 = sa12[i12] * 3 + 1 if sa12[i12] < n2 else (sa12[i12] - n2) * 3 + 2
            pos0 = sa0[i0]
            cond = (self.__get_elem(t0, pos12), self.__get_elem(t12, sa12[i12] + n2)) \
                <= (self.__get_elem(t0, pos0), self.__get_elem(t12, pos0 // 3)) \
                if sa12[i12] < n2 else \
                (self.__get_elem(t0, pos12), self.__get_elem(t0, pos12 + 1),
                 self.__get_elem(t12, sa12[i12] - n2 + 1)) \
                <= (self.__get_elem(t0, pos0), self.__get_elem(t0, pos0 + 1),
                    self.__get_elem(t12, pos0 // 3 + n2))

            if cond:
                sa.append(pos12)
                i12 += 1
            else:
                sa.append(pos0)
                i0 += 1

        while i12 < len(sa12):
            sa.append(sa12[i12] * 3 + 1 if sa12[i12] < n2 else (sa12[i12] - n2) * 3 + 2)
            i12 += 1

        while i0 < len(sa0):
            sa.append(sa0[i0])
            i0 += 1

        return sa

    def __sort_by_keys(self, v, keys, shift, k):
        buckets = [Queue() for i in range(k)]
        j = 0

        for i in v:
            buckets[self.__get_elem(keys, i + shift)].put(i)

        for e in buckets:
            while not e.empty():
                v[j] = e.get()
                j += 1

    def __get_elem(self, v, i):
        return v[i] if i < len(v) else 0
