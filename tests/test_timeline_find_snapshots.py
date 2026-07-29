from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_snapshots():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    second = repo.add(report)


    timeline = repo.timeline()


    result = timeline.find_snapshots(
        sampler__steps=40
    )


    assert len(result) == 1

    assert (
        result[0].id
        ==
        second.id
    )