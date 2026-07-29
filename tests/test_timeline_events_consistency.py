from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_events_are_separate():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    timeline = repo.timeline()


    built = timeline.build()

    streamed = timeline.stream()


    assert (
        built[0]["type"]
        ==
        "created"
    )


    assert (
        streamed[0]["type"]
        ==
        "snapshot_created"
    )