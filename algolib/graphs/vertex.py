# -*- coding: utf-8 -*-
"""Structure of graph vertex."""
from typing import Any


class Vertex:
    def __init__(self, id_: Any):
        self.id = id_

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Vertex({self.id!r})"

    def __str__(self):
        return f"Vertex({self.id})"

    def __eq__(self, vertex: "Vertex"):
        return self.id == vertex.id

    def __ne__(self, vertex: "Vertex"):
        return self.id != vertex.id

    def __lt__(self, vertex: "Vertex"):
        return self.id < vertex.id

    def __le__(self, vertex: "Vertex"):
        return self.id <= vertex.id

    def __gt__(self, vertex: "Vertex"):
        return self.id > vertex.id

    def __ge__(self, vertex: "Vertex"):
        return self.id >= vertex.id
