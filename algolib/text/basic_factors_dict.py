# -*- coding: utf-8 -*-
"""Structure of basic factors dictionary using Karp-Miller-Rosenberg algorithm."""
from typing import Tuple


class BasicFactorsDict:
    def __init__(self, text: str):
        self._text = text
        self._factors = {}
        self._create()

    @property
    def text(self) -> str:
        return self._text

    def __repr__(self):
        return f"BasicFactorsDict({self._text!r})"

    __str__ = __repr__

    def __getitem__(self, slice_: slice) -> Tuple[int, int]:
        """Retrieves code of substring denoted by given slice.

        :param slice_: the slice of indices
        :return: the code of the substring"""
        if slice_.step is not None:
            raise ValueError("Slice step must be None")

        start = self._clip(slice_.start, 0)
        stop = self._clip(slice_.stop, len(self._text))

        if stop <= start:
            raise ValueError("The slice is empty")

        try:
            return self._factors[start, stop], 0
        except KeyError:
            n = self._max_length(stop - start)
            return self._factors[start, start + n], self._factors[stop - n, stop]

    def _create(self):
        # Builds basic factors dictionary using Karp-Miller-Rosenberg algorithm.
        current_length = 2
        code_value = self._extend(
                1, 0,
                (lambda i, _: self._ExtensionCode(ord(self._text[i]), 1 + ord(self._text[i]), i)))

        while current_length <= len(self._text):
            code_value = self._extend(
                    current_length, code_value, (lambda i, length: self._ExtensionCode(
                            self._factors[i, i + length // 2],
                            self._factors[i + length // 2, i + length], i)))
            current_length *= 2

    def _extend(self, length, code_value, func):
        # Encodes substring of given length using already counted factors.
        codes = [self._ExtensionCode(0, 0, -1)] + sorted(
                func(i, length) for i in range(len(self._text) - length + 1))

        for i in range(1, len(codes)):
            if codes[i] != codes[i - 1]:
                code_value += 1

            self._factors[codes[i].index, codes[i].index + length] = code_value

        return code_value

    def _clip(self, i, default):
        if i is None:
            return default

        index = i if i >= 0 else i + len(self._text)
        return max(0, min(index, len(self._text)))

    def _validate_slice_range(self, start, stop):
        if start <= 0 and stop < 0:
            return False

        if start > len(self._text) and stop >= len(self._text):
            return False

        return True

    @staticmethod
    def _max_length(n):
        prev = 0
        power = 1

        while power < n:
            prev = power
            power *= 2

        return prev

    class _ExtensionCode:
        def __init__(self, prefix_code, suffix_code, index):
            self.prefix_code = prefix_code
            self.suffix_code = suffix_code
            self.index = index

        def __eq__(self, other):
            return self.prefix_code == other.prefix_code and self.suffix_code == other.suffix_code

        def __ne__(self, other):
            return self.prefix_code != other.prefix_code or self.suffix_code != other.suffix_code

        def __lt__(self, other):
            return (
                    self.prefix_code < other.prefix_code or self.prefix_code == other.prefix_code
                    and self.suffix_code < other.suffix_code)
