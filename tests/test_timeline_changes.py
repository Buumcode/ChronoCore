from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_change_details():

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
            "steps":30
        }
    )


    repo.add(
        second
    )


    timeline = repo.timeline()


    events = timeline.build()


    changed = [
        event
        for event in events
        if event["type"] == "changed"
    ]


    assert len(changed) == 1


    assert (
        "sampler"
        in changed[0]["changes"]
    )
    
    change = (
        changed[0]
        ["changes"]
        ["sampler"]
    )

    assert len(repo.history()) == 2

    assert change["from"]["steps"] == 20

    assert change["to"]["steps"] == 30    