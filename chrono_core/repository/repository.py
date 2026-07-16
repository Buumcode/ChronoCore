from ..history import HistoryManager
from ..storage import JsonHistoryStore


class WorkflowRepository:
    """
    Фасад для работы с историей workflow.

    Координирует HistoryManager, BranchManager
    и Storage, не добавляя собственной бизнес-логики.
    """


    def __init__(self):

        self.history = HistoryManager()


    def add(self, report):

        return self.history.add(report)


    def latest(self):

        return self.history.latest()


    def all(self):

        return self.history.all()


    # Branch operations

    def create_branch(self, name):

        return self.history.create_branch(name)


    def checkout(self, name):

        return self.history.checkout(name)


    def current_branch(self):

        return self.history.get_branch(
            self.history.active_branch
        )


    def branches(self):

        return self.history.list_branches()


    # Persistence

    def save(self, path):

        store = JsonHistoryStore(path)

        store.save(self.history)


    def load(self, path):

        store = JsonHistoryStore(path)

        return store.load()