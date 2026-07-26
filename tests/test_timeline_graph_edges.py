from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_edges():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps":20
        }
    )


    repo.add(
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


    edges = graph.edges()


    assert len(edges) == 1


    assert (
        edges[0]["from"]
        !=
        edges[0]["to"]
    )