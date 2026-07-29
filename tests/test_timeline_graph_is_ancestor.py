from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_is_ancestor():

    repo = WorkflowRepository()


    first = repo.add(
        WorkflowReport()
    )

    second = repo.add(
        WorkflowReport()
    )

    third = repo.add(
        WorkflowReport()
    )


    graph = repo.timeline().graph()


    assert graph.is_ancestor(
        first.id,
        third.id,
    )

    assert graph.is_ancestor(
        second.id,
        third.id,
    )

    assert not graph.is_ancestor(
        third.id,
        first.id,
    )