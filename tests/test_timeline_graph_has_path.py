from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_has_path():

    repo = WorkflowRepository()


    first = WorkflowReport()
    first_snapshot = repo.add(first)


    second = WorkflowReport()
    second_snapshot = repo.add(second)


    graph = repo.timeline().graph()


    assert graph.has_path(
        first_snapshot.id,
        second_snapshot.id,
    )


    assert not graph.has_path(
        second_snapshot.id,
        first_snapshot.id,
    )