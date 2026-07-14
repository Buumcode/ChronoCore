from ..graph.graph import Graph


class LoRAExtractor:
    """
    Извлекает информацию о LoRA,
    используемых в workflow.
    """

    LORA_LOADERS = {
        "LoraLoader",
        "LoraLoaderModelOnly",
    }

    def extract(self, graph: Graph):

        loras = []

        for node in graph.all_nodes():

            if node.class_type not in self.LORA_LOADERS:
                continue

            loras.append(
                {
                    "type": node.class_type,
                    "name": node.get_input("lora_name"),
                    "strength_model": node.get_input(
                        "strength_model"
                    ),
                    "strength_clip": node.get_input(
                        "strength_clip"
                    ),
                }
            )

        return loras