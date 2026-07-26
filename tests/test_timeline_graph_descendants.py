from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_descendants():

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


    third = WorkflowReport()

    third.add(
        "sampler",
        {
            "steps":40
        }
    )

    third_snapshot = repo.add(
        third
    )


    graph = repo.timeline().graph()


    descendants = graph.descendants(
        first_snapshot.id
    )


    assert descendants == [
        second_snapshot.id,
        third_snapshot.id,
    ]