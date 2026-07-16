from chrono_core.history import HistoryManager
from chrono_core.report import WorkflowReport


def test_event_log_roundtrip():

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


    history.create_branch(
        "experiment"
    )


    data = (
        history.to_dict()
    )


    restored = (
        HistoryManager.from_dict(
            data
        )
    )


    events = restored.events()


    assert len(events) == 2


    assert (
        events[0].type
        ==
        "snapshot_created"
    )


    assert (
        events[1].type
        ==
        "branch_created"
    )


    assert (
        events[0].payload["snapshot"]
        ==
        snapshot.id
    )