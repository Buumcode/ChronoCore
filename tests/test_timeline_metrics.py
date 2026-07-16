from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_metrics():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    report.metric(
        "score",
        0.9
    )


    repo.add(
        report
    )


    timeline = repo.timeline()


    metrics = timeline.metrics()


    assert len(metrics) == 1


    assert (
        metrics[0]["score"]
        ==
        0.9
    )