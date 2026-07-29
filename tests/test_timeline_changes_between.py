from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_changes_between():

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
            "steps":40
        }
    )

    second_snapshot = repo.add(
        second
    )


    timeline = repo.timeline()


    changes = timeline.changes_between(
        first_snapshot.id,
        second_snapshot.id,
    )

#   print(first.to_dict())
#   print(second.to_dict())
#   print(changes)

    assert (
        changes["changed"]["sampler"]["from"]["steps"]
        ==
        20
    )

    assert (
        changes["changed"]["sampler"]["to"]["steps"]
        ==
        40
    )