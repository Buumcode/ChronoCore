from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_checkpoint():


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


    checkpoints = timeline.checkpoints()


    assert len(checkpoints) == 2


    assert (
        checkpoints[0]["state"]["sampler"]["steps"]
        ==
        20
    )