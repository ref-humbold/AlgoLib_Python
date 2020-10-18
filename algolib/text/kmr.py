# -*- coding: utf-8 -*-
"""Base words dictionary structure using Karp-Miller-Rosenberg algorithm"""


class BaseWordsDict:
    def __init__(self, text):
        self._text = text
        self._factors = {}
        self._create()

    @property
    def text(self):
        return self._text

    def __str__(self):
        return f"BaseWordsDict({self._factors})"

    def __getitem__(self, item):
        if item[0] == item[1]:
            return 0, 0

        try:
            return self._factors[item], 0
        except KeyError:
            n = self._max_length(item[1] - item[0])
            return self._factors[item[0], item[0] + n], self._factors[item[1] - n, item[1]]

    def _create(self):
        # Builds a base words dictionary using Karp-Miller-Rosenberg algorithm
        code_value = self._extend(1, 0, self._from_single)
        length = 2

        while length <= len(self._text):
            code_value = self._extend(length, code_value, self._from_shorter)
            length *= 2

    def _extend(self, length, code_value, func):
        # Encodes substring of specified length using already counted factors
        previous_code = (0, 0)
        codes = sorted(func(i, length) for i in range(len(self._text) - length + 1))

        for code in codes:
            if code[0] != previous_code[0] or code[1] != previous_code[1]:
                code_value += 1
                previous_code = (code[0], code[1])

            self._factors[code[2], code[3]] = code_value

        return code_value

    def _from_single(self, i, length):
        return ord(self._text[i]), 1 + ord(self._text[i]), i, i + length

    def _from_shorter(self, i, length):
        return self._factors[i, i + length // 2], self._factors[i + length // 2,
                                                                i + length], i, i + length

    @staticmethod
    def _max_length(n):
        prev = 0
        power = 1

        while power < n:
            prev = power
            power *= 2

        return prev
