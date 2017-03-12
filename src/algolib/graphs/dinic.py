# ALGORYTM DINICA: MAKSYMALNY PRZEP�YW
# -*- coding: utf-8 -*-
import queue

class FlowGraphDinic:
    _INF = float(1<<30)    # oznaczenie nieskończoności

    def __init__(self, n):
        """
        KONSTRUKTOR PUSTEGO GRAFU PRZEP�YWOWEGO
        :param n: liczba wierzchołków
        """
        self.__num_vertex = n    # liczba wierzchołków grafu
        self.__graphrepr = [ [] for i in range(n+1) ]    # sąsiedztwa grafu przep�ywowego
        self.__capacities = [ [self._INF]*(n+1) for i in range(n+1) ]    # macierz przeputowo�ci kraw�dzi

    def flow(self, source, target):
        """
        WYLICZANIE CA�O�CIOWEGO PRZEP�YWU W GRAFIE
        :param source: �r�d�o
        :param target: uj�cie
        :returns: maksymalny przep�yw sieci
        """
        self.__layer_graph = []    # lista sąsiedztwa grafu warstwowego
        max_flow = 0.0; is_flow_added = True

        while is_flow_added:
            self.__layer_graph = [ [] for i in range(self.__num_vertex+1) ]
            is_flow_added = self.__bfs(source, target)

            if is_flow_added:
                max_flow += self.__dfs(source, target, self._INF)

        return max_flow

    def __bfs(self, source, target):
        """
        ALGORYTM BFS TWORZ�CY GRAF WARSTWOWY
        :param source: �r�d�o
        :param target: uj�cie
        :returns: czy uda si� powi�kszy� przep�yw
        """
        vertex_layer = [None]*(self.__num_vertex+1); vertexlayer[source] = 0
        vertex_queue = queue.Queue(); vertex_queue.put(source)

        while not vertex_queue.empty():
            v = vertex_queue.get()

            if v == target:
                return True

            for nb in self.__graphrepr[v]:
                if self.__capacities[v][nb] > 0.0:
                    if vertex_layer[nb] is None:
                        vertex_layer[nb] = vertex_layer[v]+1
                        vertex_queue.put(nb)

                    if vertex_layer[nb] == vertex_layer[v]+1:
                        self.__layer_graph[v].append(nb)

        return False

    def __dfs(self, vertex, target, blocking_flow):
        """
        ALGORYTM DFS NA GRAFIE WARSTWOWYM WYZNACZAJ�CY PRZEP�YW BLOKUJ�CY DLA �CIE�EK
        :param vertex: aktualny wierzchołek
        :param target: uj�cie
        :param blocking_flow: stary przep�yw blokuj�cy
        :returns: nowy przep�yw blokuj�cy
        """
        if vertex == target or blocking_flow == 0.0:
            return blocking_flow

        new_blocking_flow = 0.0

        for neighbour in self.__layer_graph[vertex]:
            flow_add = self.__dfs( neighbour, target, min(self.__capacities[vertex][neighbour], blocking_flow) )
            blocking_flow -= flow_add
            new_blocking_flow += flow_add
            self.__capacities[vertex][neighbour] -= flow_add
            self.__capacities[neighbour][vertex] += +flow_add

            if blocking_flow == 0.0:
                break

        return new_blocking_flow

