from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_graph_find_node():

    repo = WorkflowRepository()

    report = WorkflowReport()
    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    snapshot = repo.add(
        report
    )

    graph = repo.timeline().graph()

    node = graph.find_node(
        snapshot.id
    )

    assert node is not None
    assert node["id"] == snapshot.id