from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport
from chrono_core.timeline.graph import WorkflowTimelineGraph


def test_timeline_graph():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    repo.add(
        report
    )


    graph = repo.timeline().graph()


    assert isinstance(
        graph,
        WorkflowTimelineGraph
    )


    assert len(
        graph.nodes()
    ) == 1