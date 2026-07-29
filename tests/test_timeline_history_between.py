from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_history_between():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps":20
        }
    )

    first_snapshot = repo.add(
        first
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps":30
        }
    )

    second_snapshot = repo.add(
        second
    )


    third = WorkflowReport()

    third.add(
        "sampler",
        {
            "steps":40
        }
    )

    third_snapshot = repo.add(
        third
    )


    timeline = repo.timeline()


    history = timeline.history_between(
        first_snapshot.id,
        third_snapshot.id,
    )


    assert len(history) == 3

    assert (
        history[0]["snapshot"]
        ==
        first_snapshot.id
    )

    assert (
        history[2]["snapshot"]
        ==
        third_snapshot.id
    )