from ..history import HistoryManager
from ..storage import JsonHistoryStore
from ..timeline import WorkflowTimeline


class WorkflowRepository:
    """
    Фасад для работы с историей workflow.

    Координирует HistoryManager, BranchManager
    и Storage, не добавляя собственной бизнес-логики.
    """


    def __init__(self):

        self.history_manager = HistoryManager()


    def add(
        self,
        report,
        branch=None
    ):

        if branch is None:
            return self.history_manager.add(
                report
            )

        return self.history_manager.add(
            report,
            branch=branch
        )


    def latest(self):

        return self.history_manager.latest()
        

    def history(self):

        return self.history_manager.all()        


    def timeline(self):

        return WorkflowTimeline(
            self.history_manager
        ).build()


    def diff(
        self,
        old_id,
        new_id
    ):

        return self.history_manager.diff(
            old_id,
            new_id
        )


    def save(
        self,
        path
    ):

        store = JsonHistoryStore(
            path
        )

        store.save(
            self.history_manager
        )


    def load(
        self,
        path
    ):

        store = JsonHistoryStore(
            path
        )

        return store.load()


    def all(self):

        return self.history_manager.all()


    # Branch operations

    def create_branch(self, name):

        return self.history_manager.create_branch(name)


    def checkout(self, name):

        return self.history_manager.checkout(name)


    def current_branch(self):

        return self.history_manager.get_branch(
            self.history_manager.current_branch
        )


    def branches(self):

        return self.history_manager.list_branches()
