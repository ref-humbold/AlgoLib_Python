# -*- coding: utf-8 -*-
"""BFS DLA TABLICY"""
import queue

class Table:
    _EMPTY_CELL = None    # oznaczenie pustej komórki

    def __init__(self, n, m):
        self.__rows = n    # liczba wierszy
        self.__columns = m    # liczba kolumn
        self.__table = [[self._EMPTY_CELL]*m for i in range(n)]    # tablica

    def bfs(self, source):
        """Algorytm BFS.
        :param source: współrzędne początkowej komórki"""
        cell_queue = queue.Queue()
        cell_queue.put(source)
        self.__table[source[0]][source[1]] = 0

        while not cell_queue.empty():
            xcell, ycell = cell_queue.get()

            if xcell > 0 and self.__table[xcell-1][ycell] is self._EMPTY_CELL:
                self.__table[xcell-1][ycell] = self.__table[xcell][ycell]+1
                cell_queue.put((xcell-1, ycell))

            if xcell < self.__rows-1 and self.__table[xcell+1][ycell] is self._EMPTY_CELL:
                self.__table[xcell+1][ycell] = self.__table[xcell][ycell]+1
                cell_queue.put((xcell+1, ycell))

            if ycell > 0 and self.__table[xcell][ycell-1] is self._EMPTY_CELL:
                self.__table[xcell][ycell-1] = self.__table[xcell][ycell]+1
                cell_queue.put((xcell, ycell-1))

            if ycell < self.__columns-1 and self.__table[xcell][ycell+1] is self._EMPTY_CELL:
                self.__table[xcell][ycell+1] = self.__table[xcell][ycell]+1
                cell_queue.put((xcell, ycell+1))
