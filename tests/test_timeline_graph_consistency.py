from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_graph_consistency():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    first = repo.add(
        report
    )


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    second = repo.add(
        report
    )


    graph = (
        repo
        .timeline()
        .graph()
    )


    assert len(graph.nodes()) == 2


    assert (
        graph.nodes()[0]["id"]
        ==
        first.id
    )


    assert (
        graph.nodes()[1]["id"]
        ==
        second.id
    )


    assert len(graph.edges()) == 1


    assert (
        graph.edges()[0]["from"]
        ==
        first.id
    )


    assert (
        graph.edges()[0]["to"]
        ==
        second.id
    )