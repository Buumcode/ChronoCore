from ..repository import WorkflowRepository


class WorkflowSerializer:
    """
    Сериализация объектов ChronoCore.
    """

    FORMAT = "chrono_core"
    VERSION = 1


    def dump(
        self,
        repository
    ):

        return {
            "format": self.FORMAT,
            "version": self.VERSION,
            "repository": repository.to_dict(),
        }


    def load(
        self,
        data
    ):

        if data.get("format") != self.FORMAT:
            raise ValueError(
                "Invalid ChronoCore format"
            )


        return WorkflowRepository.from_dict(
            data["repository"]
        )