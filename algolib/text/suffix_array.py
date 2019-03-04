# -*- coding: utf-8 -*-
"""SUFFIX ARRAY IMPLEMENTATION"""


class SuffixArray:
    def __init__(self, text):
        self.__length = len(text)
        self.__text = text
        self.__suf_arr = self.__init_array()
        self.__inv_arr = self.__init_inv()
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
        if suf1 < 0 or suf1 >= length or suf2 < 0 or suf2 >= length:
            raise IndexError("Text index out of range")

        if suf1 == suf2:
            return length - suf1

        i1 = min(self.__inv_arr[suf1], self.__inv_arr[suf2])
        i2 = max(self.__inv_arr[suf1], self.__inv_arr[suf2])

        return min(self.__lcp_arr[i] for i in range(i1 + 1, i2 + 1))

    def __init_array(self):
        return self.__create_array(list(map(ord, txt)), 128)

    def __init_inv():
        arr = [0] * self.__length

        for i in range(0, self.__length):
            arr[self.__suf_arr[i]] = i

        return arr

    def __init_lcp():
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
