from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_changed_query():

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


    changes = timeline.changed(
        "sampler"
    )


    assert len(changes) == 1


    assert (
        changes[0]["from"]["steps"]
        ==
        20
    )

    assert (
        changes[0]["to"]["steps"]
        ==
        30
    )