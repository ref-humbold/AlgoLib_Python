# -*- coding: utf-8 -*-
"""Algorithm for computing diameter of a tree."""
from typing import Tuple

from ..tree_graph import TreeGraph
from ..vertex import Vertex


def count_diameter(tree: TreeGraph) -> float:
    """Computes length of diameter of given tree graph.

    :param tree: the tree graph
    :return: the length of the tree diameter"""
    root = max(tree.vertices, key=tree.output_degree, default=None)

    return 0.0 if root is None else _dfs(tree, root, root)[1]


def _dfs(tree: TreeGraph, vertex: Vertex, parent: Vertex) -> Tuple[float, float]:
    path_from = 0.0
    path_subtree = 0.0
    path_through = 0.0

    for edge in tree.adjacent_edges(vertex):
        neighbour = edge.get_neighbour(vertex)

        if neighbour != parent:
            weight = tree.properties[edge].weight
            result_from, result_subtree = _dfs(tree, neighbour, vertex)

            path_through = max(path_through, path_from + result_from + weight)
            path_subtree = max(path_subtree, result_subtree)
            path_from = max(path_from, result_from + weight)

    return path_from, max(path_through, path_subtree)
