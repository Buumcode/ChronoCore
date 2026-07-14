from chrono_core.report import WorkflowReport
from chrono_core.history import HistoryManager
from chrono_core.timeline import WorkflowTimeline



def test_timeline():

    history = HistoryManager()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps":20
        }
    )


    history.add(
        first
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps":30
        }
    )


    history.add(
        second
    )


    timeline = WorkflowTimeline(
        history
    )


    events = timeline.build()


    assert len(events) == 2


    assert (
        events[0]["type"]
        ==
        "created"
    )


    assert (
        events[1]["type"]
        ==
        "changed"
    )


    assert (
        events[1]["changes"]
        ["sampler"]
        ["to"]
        ["steps"]
        ==
        30
    )