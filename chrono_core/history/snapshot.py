from datetime import datetime, UTC
import uuid


class WorkflowSnapshot:
    """
    Снимок состояния workflow.

    Хранит результат анализа
    в определённый момент.
    """


    def __init__(
        self,
        report,
    ):

        self.id = str(
            uuid.uuid4()
        )

        self.created = (
            datetime.now(UTC)
        )

        self.report = report



    def compare(
        self,
        other,
    ):

        from ..diff import WorkflowDiff


        return WorkflowDiff().compare(
            self.report,
            other.report
        )



    def to_dict(self):

        return {
            "id": self.id,
            "created": self.created.isoformat(),
            "report": self.report.to_dict(),
        }