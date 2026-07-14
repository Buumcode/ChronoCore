import json
from pathlib import Path

from ..report import WorkflowReport
from ..history import WorkflowSnapshot


class JsonHistoryStore:
    """
    JSON-хранилище истории workflow.
    """


    def __init__(
        self,
        path,
    ):

        self.path = Path(path)



    def save(
        self,
        history,
    ):

        data = {
            "snapshots": [
                snapshot.to_dict()
                for snapshot in history.all()
            ]
        }


        self.path.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8"
        )



    def load(
        self,
    ):

        if not self.path.exists():
            return []


        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )


        return data.get(
            "snapshots",
            []
        )