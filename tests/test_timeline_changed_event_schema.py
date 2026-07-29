from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_changed_event_schema():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(report)


    events = repo.timeline().build()


    assert len(events) == 2


    event = events[1]


    assert (
        event["type"]
        ==
        "changed"
    )


    assert (
        "snapshot"
        in event
    )


    assert (
        "changes"
        in event
    )