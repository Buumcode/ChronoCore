from .snapshot import WorkflowSnapshot


class HistoryManager:
    """
    Хранилище WorkflowSnapshot.

    Аналог истории изменений workflow.
    """


    def __init__(self):

        self.snapshots = []



    def add(
        self,
        report,
    ):

        snapshot = WorkflowSnapshot(
            report
        )

        self.snapshots.append(
            snapshot
        )

        return snapshot



    def latest(self):

        if not self.snapshots:
            return None

        return self.snapshots[-1]



    def all(self):

        return list(
            self.snapshots
        )



    def get(
        self,
        snapshot_id,
    ):

        for snapshot in self.snapshots:

            if snapshot.id == snapshot_id:
                return snapshot

        return None



    def diff(
        self,
        old_id,
        new_id,
    ):

        old = self.get(
            old_id
        )

        new = self.get(
            new_id
        )

        if old is None or new is None:
            return None


        return old.compare(
            new
        )