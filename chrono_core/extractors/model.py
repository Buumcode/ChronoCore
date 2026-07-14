from ..graph.graph import Graph


class ModelExtractor:

    MODEL_LOADERS = (
        "CheckpointLoaderSimple",
        "CheckpointLoader",
    )

    def extract(self, graph: Graph):

        node = graph.find_first_type(
            *self.MODEL_LOADERS
        )

        if node is None:
            return None

        return {
            "type": node.class_type,
            "checkpoint": node.get_input(
                "ckpt_name"
            ),
        }