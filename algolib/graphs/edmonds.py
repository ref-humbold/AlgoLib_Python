# ALGORYTM EDMONDSA-KARPA: MAKSYMALNY PRZEPŁYW
# -*- coding: utf-8 -*-
import queue


class FlowGraphEdmonds:
    _INF = float(1 << 30)  # oznaczenie nieskończoności

    def __init__(self, n):
        """
        KONSTRUKTOR PUSTEGO GRAFU PRZEP�YWOWEGO
        :param n: liczba wierzchołków
        """
        self.__num_vertex = n  # liczba wierzchołków grafu
        self.__graphrepr = [[] for i in range(n + 1)]  # lista sąsiedztwa grafu przepływowego
        self.__capacities = [[self._INF] * (n + 1)
                             for i in range(n + 1)]  # macierz przeputowości krawędzi

    def count_flow(self, source, target):
        """
        WYLICZANIE CA�O�CIOWEGO PRZEP�YWU W GRAFIE
        :param source: �r�d�o
        :param target: uj�cie
        :returns: maksymalny przep�yw sieci
        """
        self.__augmenting_paths = []  # tablica poprzedników i minimalnych przepustowości ze źródła
        max_flow = 0.0
        is_flow_added = True

        while is_flow_added:
            self.__augmenting_paths = [(None, self._INF)] * (self.__num_vertex + 1)
            is_flow_added = self.__bfs(source, target)

            if is_flow_added:
                max_flow += self.__count_path_flow(source, target)

        return max_flow

    def __bfs(self, source, target):
        """
        ALGORYTM BFS ZNAJDUJ�CY �CIE�K� POWI�KSZAJ�C�
        :param source: �r�d�o
        :param target: uj�cie
        :return: czy uda si� powi�kszy� przep�yw
        """
        vertex_queue = queue.Queue()
        vertex_queue.put(source)
        self.__augmenting_paths[source] = (0, self._INF)

        while not vertex_queue.empty():
            w = vertex_queue.get()

            if w == target:
                return True

            for s in self.__graphrepr[w]:
                if self.__capacities[w][s] > 0 and self.__augmenting_paths[s][0] is None:
                    self.__augmenting_paths[s] = \
                        (w, min(self.__capacities[w][s], self.__augmenting_paths[w][1]))
                    vertex_queue.put(s)

        return False

    def __count_path_flow(self, source, target):
        """
        WYLICZANIE PRZEP�YWU NA �CIE�CE POWI�KSZAJ�CEJ
        :param source: �r�d�o
        :param target: uj�cie
        :returns: przep�yw na �cie�ce
        """
        w = target

        while w != source:
            s = self.__augmenting_paths[w][0]
            self.__capacities[s][w] -= self.__augmenting_paths[target][1]
            self.__capacities[w][s] += self.__augmenting_paths[target][1]
            w = s

        return self.__augmenting_paths[target][1]
