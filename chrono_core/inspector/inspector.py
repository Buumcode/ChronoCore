from ..extractors.prompt import PromptExtractor
from ..extractors.sampler import SamplerExtractor
from ..conditioning.resolver import ConditioningResolver



class Inspector:
    """
    Главный анализатор workflow.

    Inspector не знает деталей ComfyUI.
    Он объединяет специализированные анализаторы.
    """


    def __init__(self):

        self.prompt_extractor = PromptExtractor()
        self.sampler_extractor = SamplerExtractor()



    def inspect(self, graph):

        result = {}


        # Prompt analysis

        prompts = self.prompt_extractor.extract(
            graph
        )

        result["prompts"] = prompts
        
        result["sampler"] = (
            self.sampler_extractor.extract(
                graph
            )
        )


        # Conditioning analysis

        conditioning = ConditioningResolver(
            graph
        )

        result["conditioning"] = self._inspect_conditioning(
            graph,
            conditioning
        )
        
        result["sampler"] = (
            self.sampler_extractor.extract(
                graph
            )
        )


        return result



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