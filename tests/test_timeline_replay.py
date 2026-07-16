from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_replay():

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


    replay = timeline.replay()


    assert len(replay) == 2


    assert (
        replay[0]["state"]["sampler"]["steps"]
        ==
        20
    )


    assert (
        replay[1]["state"]["sampler"]["steps"]
        ==
        40
    )