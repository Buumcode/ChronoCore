from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_event_schema():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    events = repo.timeline().build()


    assert len(events) == 1


    event = events[0]


    assert (
        event["type"]
        ==
        "created"
    )


    assert (
        "snapshot"
        in event
    )


    assert (
        "message"
        in event
    )