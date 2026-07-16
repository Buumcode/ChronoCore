from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_report():

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


    timeline_report = repo.timeline().report()


    assert timeline_report["events"] == 1

    assert timeline_report["snapshots"] == 1

    assert timeline_report["branches"] == [
        "main"
    ]

    assert (
        timeline_report["metrics"]["score"]["avg"]
        ==
        0.9
    )