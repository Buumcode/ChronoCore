from ..graph.graph import Graph


class SamplerExtractor:
    """
    Извлекает параметры sampler-узла.

    Не знает о конкретном workflow.
    Ищет только семантически важные данные.
    """

    SAMPLER_TYPES = {
        "KSampler",
        "KSamplerAdvanced",
    }


    def extract(self, graph: Graph):

        node = graph.find_first_type(
            "KSampler",
            "KSamplerAdvanced"
        )

        if node is None:
            return None

        return {
            "type": node.class_type,
            "steps": node.get_input("steps"),
            "cfg": node.get_input("cfg"),
            "sampler": node.get_input("sampler_name"),
            "scheduler": node.get_input("scheduler"),
            "denoise": node.get_input("denoise"),
        }