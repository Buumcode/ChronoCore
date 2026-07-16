from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_history_of():

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
            "steps": 30
        }
    )

    repo.add(
        second
    )


    timeline = repo.timeline()


    history = timeline.history_of(
        "sampler.steps"
    )


    assert history == [
        20,
        30,
    ]