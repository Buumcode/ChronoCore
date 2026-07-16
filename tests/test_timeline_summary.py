from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_summary():

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


    repo.create_branch(
        "experiment"
    )


    timeline = repo.timeline()


    summary = timeline.summary()


    assert summary["snapshots"] == 1

    assert summary["branches"] == 1

    assert summary["total"] == 2