from ..extractors.prompt import PromptExtractor
from ..extractors.sampler import SamplerExtractor
from ..extractors.model import ModelExtractor
from ..extractors.lora import LoRAExtractor
from ..conditioning.resolver import ConditioningResolver
from ..report import WorkflowReport



class Inspector:
    """
    Главный анализатор workflow.

    Inspector не знает деталей ComfyUI.
    Он объединяет специализированные анализаторы.
    """


    def __init__(self):

        self.prompt_extractor = PromptExtractor()
        self.sampler_extractor = SamplerExtractor()
        self.model_extractor = ModelExtractor()
        self.lora_extractor = LoRAExtractor()



    def inspect(self, graph):

        report = WorkflowReport()

        report.add(
            "prompts",
            self.prompt_extractor.extract(graph)
        )

        report.add(
            "sampler",
            self.sampler_extractor.extract(graph)
        )

        report.add(
            "model",
            self.model_extractor.extract(graph)
        )
        
        report.add(
            "loras",
            self.lora_extractor.extract(graph)
        )

        conditioning = ConditioningResolver(
            graph
        )

        report.add(
            "conditioning",
            self._inspect_conditioning(
                graph,
                conditioning
            )
        )

        return report



    def _inspect_conditioning(
        self,
        graph,
        resolver
    ):

        result = []


        for node in graph.all_nodes():

            for value in node.inputs.values():

                chain = resolver.resolve_chain(
                    value
                )

                if chain.contains(
                    "ConditioningZeroOut"
                ):

                    result.append(
                        "ConditioningZeroOut"
                    )


        return list(set(result))