from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_event_factory_keeps_schema():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    event = repo.timeline().build()[0]


    assert set(event.keys()) == {
        "type",
        "message",
        "snapshot",
    }