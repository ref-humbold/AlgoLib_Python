# -*- coding: utf-8 -*-
"""Structure of base words dictionary using Karp-Miller-Rosenberg algorithm"""
from typing import Tuple


class BaseWordsDict:
    def __init__(self, text: str):
        self._text = text
        self._factors = {}
        self._create()

    @property
    def text(self) -> str:
        return self._text

    def __str__(self):
        return f"BaseWordsDict({self._text}, {self._factors})"

    def __getitem__(self, slice_: slice) -> Tuple[int, int]:
        """Retrieves code of a substring denoted by slice.

        :param slice_: slice indices
        :return: the code of the substring"""
        if slice_.step is not None:
            raise IndexError("Slice step must be None")

        start = self._clip(slice_.start, 0)
        stop = self._clip(slice_.stop, len(self._text))

        if stop <= start:
            return 0, 0

        try:
            return self._factors[start, stop], 0
        except KeyError:
            n = self._max_length(stop - start)
            return self._factors[start, start + n], self._factors[stop - n, stop]

    def _create(self):
        # Builds a base words dictionary using Karp-Miller-Rosenberg algorithm
        current_length = 2
        code_value = self._extend(1, 0,
                                  lambda i, length: (ord(self._text[i]), 1 + ord(self._text[i]),
                                                     i, i + length))

        while current_length <= len(self._text):
            code_value = self._extend(current_length, code_value,
                                      lambda i, length: (self._factors[i, i + length // 2],
                                                         self._factors[i + length // 2, i + length],
                                                         i, i + length))
            current_length *= 2

    def _extend(self, length, code_value, func):
        # Encodes substring of specified length using already counted factors
        previous_code = (0, 0)
        codes = sorted(func(i, length) for i in range(len(self._text) - length + 1))

        for code in codes:
            code_pair = (code[0], code[1])

            if code_pair != previous_code:
                code_value += 1
                previous_code = code_pair

            self._factors[code[2], code[3]] = code_value

        return code_value

    def _clip(self, i, default):
        if i is None:
            return default

        if i < -len(self._text):
            return 0

        if i >= len(self._text):
            return len(self._text)

        return i % len(self._text)

    @staticmethod
    def _max_length(n):
        prev = 0
        power = 1

        while power < n:
            prev = power
            power *= 2

        return prev
