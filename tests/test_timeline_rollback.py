from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_rollback():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps":20
        }
    )

    repo.add(
        first
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps":40
        }
    )

    repo.add(
        second
    )


    timeline = repo.timeline()


    restored = timeline.rollback(
        0
    )


    assert (
        restored["sampler"]["steps"]
        ==
        20
    )


    assert (
        len(repo.history())
        ==
        3
    )