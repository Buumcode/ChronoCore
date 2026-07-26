class WorkflowTimelineGraph:

    def __init__(
        self,
        nodes=None,
        edges=None,
    ):

        self._nodes = nodes or []
        self._edges = edges or []


    def nodes(self):

        return list(
            self._nodes
        )


    def edges(self):

        return list(
            self._edges
        )
        
    def find_node(
        self,
        node_id,
    ):

        for node in self._nodes:

            if (
                node.get("id") == node_id
                or
                node.get("snapshot") == node_id
            ):
                return node

        return None   