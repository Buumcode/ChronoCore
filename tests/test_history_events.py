from chrono_core.history import HistoryManager
from chrono_core.report import WorkflowReport


def test_history_creates_events():

    history = HistoryManager()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    snapshot = history.add(
        report
    )


    events = history.events()


    assert len(
        events
    ) == 1


    assert (
        events[0].type
        ==
        "snapshot_created"
    )


    assert (
        events[0].payload["snapshot"]
        ==
        snapshot.id
    )