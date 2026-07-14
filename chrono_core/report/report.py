class WorkflowReport:
    """
    Универсальный результат анализа workflow.

    Хранит семантическую информацию,
    полученную Inspector.
    """


    def __init__(self):

        self.data = {}


    def add(
        self,
        key: str,
        value,
    ):
        self.data[key] = value


    def get(
        self,
        key: str,
        default=None,
    ):
        return self.data.get(
            key,
            default
        )


    def to_dict(self):

        return self.data


    def __repr__(self):

        return (
            f"<WorkflowReport "
            f"{list(self.data.keys())}>"
        )