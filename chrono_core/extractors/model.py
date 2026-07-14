from ..graph.graph import Graph


class ModelExtractor:
    """
    Извлекает информацию о загруженной модели.
    """


    MODEL_LOADERS = {
        "CheckpointLoaderSimple",
        "CheckpointLoader",
    }


    def extract(self, graph: Graph):

        for node in graph.all_nodes():

            if node.class_type in self.MODEL_LOADERS:

                return {
                    "type": node.class_type,
                    "checkpoint": node.get_input(
                        "ckpt_name"
                    ),
                }


        return None