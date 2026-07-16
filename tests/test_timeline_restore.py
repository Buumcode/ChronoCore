from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_restore_checkpoint():

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


    restored = timeline.restore(
        0
    )


    assert (
        restored["sampler"]["steps"]
        ==
        20
    )