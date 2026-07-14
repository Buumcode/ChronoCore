class WorkflowBranch:
    """
    Ветка развития workflow.

    Хранит последовательность Snapshot,
    принадлежащих одному эксперименту.
    """


    def __init__(
        self,
        name: str,
    ):

        self.name = name
        self.snapshots = []


    def add(
        self,
        snapshot,
    ):

        self.snapshots.append(
            snapshot
        )


    def latest(self):

        if not self.snapshots:
            return None

        return self.snapshots[-1]


    def size(self):

        return len(
            self.snapshots
        )


    def all(self):

        return list(
            self.snapshots
        )