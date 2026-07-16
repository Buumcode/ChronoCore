from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_metric_summary():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.metric(
        "score",
        0.8
    )

    repo.add(
        first
    )


    second = WorkflowReport()

    second.metric(
        "score",
        1.0
    )

    repo.add(
        second
    )


    summary = repo.timeline().metric_summary()


    assert summary["score"]["count"] == 2

    assert summary["score"]["min"] == 0.8

    assert summary["score"]["max"] == 1.0

    assert summary["score"]["avg"] == 0.9