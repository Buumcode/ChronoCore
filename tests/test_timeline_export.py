from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_export():

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


    exported = repo.timeline().export()


    assert exported["events"] == 1

    assert exported["snapshots"] == 1

    assert exported["metrics"]["score"]["avg"] == 0.9