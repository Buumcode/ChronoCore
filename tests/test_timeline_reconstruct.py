from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_reconstruct_state():

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


    state = timeline.reconstruct(
        1
    )


    assert (
        state["sampler"]["steps"]
        ==
        40
    )