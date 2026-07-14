from ..graph.graph import Graph
from ..graph.walker import GraphWalker

from .text import (
    is_text_node,
    extract_text,
)


class PromptExtractor:


    def extract(self, graph: Graph):

        result = {
            "positive": "",
            "negative": "",
        }


        walker = GraphWalker(graph)


        for node in graph.all_nodes():

            positive = node.get_input(
                "positive"
            )

            negative = node.get_input(
                "negative"
            )


            if positive:

                result["positive"] = (
                    self._extract_from_link(
                        positive,
                        walker
                    )
                )


            if negative:

                result["negative"] = (
                    self._extract_from_link(
                        negative,
                        walker
                    )
                )


        return result



    def _extract_from_link(
        self,
        link,
        walker: GraphWalker,
    ):

        if not isinstance(link, list):
            return ""


        first = walker.get_link_node(
            link
        )

        if first is None:
            return ""


        if first.is_type(
            "ConditioningZeroOut"
        ):
            return ""


        node = walker.find_first(
            link,
            is_text_node
        )


        if node:
            return extract_text(node)


        return ""