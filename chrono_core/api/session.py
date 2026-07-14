from ..adapters.comfyui import ComfyUIAdapter
from ..inspector.inspector import Inspector


class Session:
    """
    Публичная точка входа в ChronoCore.

    Session строит граф, запускает анализ
    и хранит готовый отчёт.
    """

    def __init__(self, workflow):

        self.graph = ComfyUIAdapter.from_prompt(
            workflow
        )

        self.inspector = Inspector()

        self.report = self.inspector.inspect(
            self.graph
        )
        
    @property
    def prompts(self):
        return self.report["prompts"]


    @property
    def model(self):
        return self.report["model"]


    @property
    def sampler(self):
        return self.report["sampler"]


    @property
    def conditioning(self):
        return self.report["conditioning"]


    @property
    def loras(self):
        return self.report.get(
            "loras",
            []
        )        