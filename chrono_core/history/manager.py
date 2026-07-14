from .snapshot import WorkflowSnapshot
from ..branches import WorkflowBranch
from ..report import WorkflowReport


class HistoryManager:

    def __init__(self):

        self.branches = {
            "main": WorkflowBranch(
                "main"
            )
        }

        self.active_branch = "main"

        # compatibility
        self.snapshots = (
            self.branches["main"].snapshots
        )


    def add(
        self,
        item,
        branch="main"
    ):


        if isinstance(
            item,
            WorkflowReport
        ):

            item = WorkflowSnapshot(
                item
            )


        if branch not in self.branches:

            self.create_branch(
                branch
            )


        self.branches[branch].add(
            item
        )


        if branch == "main":

            self.snapshots = (
                self.branches["main"].snapshots
            )


        return item


    def all(self):

        return list(
            self.snapshots
        )


    def latest(self):

        if not self.snapshots:
            return None

        return self.snapshots[-1]



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
        
    def create_branch(
        self,
        name: str,
    ):

        if name in self.branches:
            return self.branches[name]


        branch = WorkflowBranch(
            name
        )

        self.branches[name] = branch

        return branch  

    def get_branch(
        self,
        name: str,
    ):

        return self.branches.get(
            name
        )

    def list_branches(self):

        return list(
            self.branches.keys()
        ) 

    @property
    def items(self):

        return self.branches[
            self.active_branch
        ].all()        