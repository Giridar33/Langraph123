import uuid

class GraphRunner:
    def __init__(self, graph):
        self.graph = graph

    def run(self, initial_state):
        state = initial_state
        node_name = self.graph.start
        log = []

        while node_name:
            node = self.graph.nodes[node_name]
            log.append(f"Running {node_name}")
            state = node.run(state)

            edge = self.graph.edges.get(node_name)

            if callable(edge):
                node_name = edge(state)
            else:
                node_name = edge

        return state, log
