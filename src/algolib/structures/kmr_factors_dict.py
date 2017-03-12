# -*- coding: utf-8 -*-
"""SŁOWNIK PODSŁÓW BAZOWYCH Z ALGORYTMEM KARPA-MILLERA-ROSENBERGA"""
class KMRFactorsDict:
    def __init__(self, text):
        self.__text = text    # słowo
        self.__factors = {}    # słownik podsłów bazowych

    @property
    def factors(self):
        """Getter dla słownika.
        :returns: słownik podsłów bazowych"""
        return self.__factors

    @property
    def text(self):
        """Getter dla słowa.
        :returns: słowo"""
        return self.__text

    def kmr(self):
        """Budowa słownika podsłów bazowych."""
        self.__sign_letters()
        ln = 2

        while ln <= len(self.__text):
            self.__double_length(ln)
            ln <<= 1

    def __sign_letters(self):
        """Budowa podsłów złożonych z pojedynczych znaków."""
        code_value = 0; letters = sorted(self.__text)
        self.__factors[ letters[0] ] = code_value

        for i in range( 1, len(letters) ):
            if letters[i] != letters[i-1]:
                code_value += 1
                self.__factors[ letters[i] ] = code_value

    def __double_length(self, new_length):
        """Budowa nowych podsłów o podwojonej długości.
        :param new_length: nowa długość podsłów"""
        code_value = 0
        code_prev = lambda i: self.__factors[ self.__text[i:i+new_length//2] ]
        code_next = lambda i: self.__factors[ self.__text[i+new_length//2:i+new_length] ]
        codes = sorted([(code_prev(i), code_next(i), i) for i in range(len(self.__text)-new_length+1)])
        self.__factors[ self.__text[codes[0][2]:codes[0][2]+new_length] ] = code_value

        for i in range( 1, len(codes) ):
            if codes[i] != codes[i-1]:
                substr = self.__text[codes[i][2]:codes[i][2]+new_length]
                code_value += 1
                self.__factors[substr] = code_value

