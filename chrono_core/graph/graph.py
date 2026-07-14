from .node import Node


class Graph:

    def __init__(self):
        self.nodes: dict[str, Node] = {}

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def get(self, node_id: str):
        return self.nodes.get(str(node_id))

    def __contains__(self, node_id):
        return str(node_id) in self.nodes

    def all_nodes(self):
        return self.nodes.values()