from ..graph.graph import Graph


class PromptExtractor:


    def extract(self, graph: Graph):

        positive = ""
        negative = ""

        for node in graph.all_nodes():

            pos = node.get_input("positive")
            neg = node.get_input("negative")


            if pos:
                text = self._resolve_conditioning(
                    pos,
                    graph
                )

                if text:
                    positive = text


            if neg:
                text = self._resolve_conditioning(
                    neg,
                    graph
                )

                negative = text


        return {
            "positive": positive,
            "negative": negative,
        }


    def _resolve_conditioning(
        self,
        link,
        graph
    ):

        if not isinstance(link, list):
            return ""


        node = graph.get(link[0])

        if node is None:
            return ""


        # главное правило
        if node.is_type(
            "ConditioningZeroOut"
        ):
            return ""


        # обычный CLIP
        if node.class_type.startswith(
            "CLIPTextEncode"
        ):

            text = node.get_input(
                "text"
            )

            if isinstance(text, str):
                return text


        return ""