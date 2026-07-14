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