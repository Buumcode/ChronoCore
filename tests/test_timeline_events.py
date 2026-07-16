from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_events():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    repo.add(
        report
    )


    timeline = repo.timeline()


    events = timeline.events()


    assert len(events) == 1

    assert (
        events[0]["type"]
        ==
        "snapshot_created"
    )