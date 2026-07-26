from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_common_ancestor():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps":20
        }
    )

    first_snapshot = repo.add(
        first
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps":30
        }
    )

    second_snapshot = repo.add(
        second
    )


    graph = repo.timeline().graph()


    ancestor = graph.common_ancestor(
        first_snapshot.id,
        second_snapshot.id
    )


    assert ancestor is None or ancestor == first_snapshot.id