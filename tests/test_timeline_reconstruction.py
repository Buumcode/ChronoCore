from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_snapshot_at():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(
        first
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(
        second
    )


    timeline = repo.timeline()


    snapshot = timeline.snapshot_at(
        0
    )


    assert (
        snapshot["sampler"]["steps"]
        ==
        20
    )