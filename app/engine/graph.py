from typing import Callable, Dict, Any

class Node:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return self.func(state)


class Graph:
    def __init__(self, nodes, edges, start):
        self.nodes = nodes
        self.edges = edges
        self.start = start
