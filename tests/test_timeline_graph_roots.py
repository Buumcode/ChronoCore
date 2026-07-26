from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_roots():

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
            "steps":40
        }
    )


    repo.add(
        second
    )


    graph = repo.timeline().graph()


    roots = graph.roots()


    assert (
        roots
        ==
        [
            first_snapshot.id
        ]
    )