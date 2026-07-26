from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_leaves():

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


    second_snapshot = repo.add(
        second
    )


    graph = repo.timeline().graph()


    leaves = graph.leaves()


    assert (
        leaves
        ==
        [
            second_snapshot.id
        ]
    )