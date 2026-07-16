from .snapshot import WorkflowSnapshot
from ..branches import WorkflowBranch
from ..report import WorkflowReport


class HistoryManager:

    def __init__(self):

        main = WorkflowBranch(
            "main"
        )

        self.branches = {
            "main": main
        }

        self.current_branch = "main"

        # compatibility with old API
        self.active_branch = "main"

        self.snapshots = main.snapshots


    def _branch(self):

        return self.branches[
            self.current_branch
        ]


    def add(
        self,
        item,
        branch=None
    ):

        if isinstance(
            item,
            WorkflowReport
        ):

            item = WorkflowSnapshot(
                item
            )


        if branch is None:
            branch = self.current_branch


        if branch not in self.branches:

            self.create_branch(
                branch
            )


        self.branches[branch].add(
            item
        )


        if branch == self.current_branch:

            self.snapshots = (
                self.branches[branch].snapshots
            )


        return item


    def all(self):

        return self._branch().all()


    def latest(self):

        items = self.all()

        if not items:
            return None

        return items[-1]


    def get(
        self,
        snapshot_id,
    ):

        for snapshot in self.all():

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

        return self._branch().all()


    def checkout(
        self,
        name: str,
    ):

        if name not in self.branches:
            raise ValueError(
                f"Unknown branch: {name}"
            )


        self.current_branch = name
        self.active_branch = name

        self.snapshots = (
            self.branches[name].snapshots
        )

        return self.branches[name]