from chrono_core.report import WorkflowReport
from chrono_core.history import HistoryManager



def test_history_manager():

    history = HistoryManager()


    report1 = WorkflowReport()

    report1.add(
        "sampler",
        {
            "steps":20
        }
    )


    first = history.add(
        report1
    )


    report2 = WorkflowReport()

    report2.add(
        "sampler",
        {
            "steps":30
        }
    )


    second = history.add(
        report2
    )


    assert len(
        history.all()
    ) == 2


    assert (
        history.latest().id
        ==
        second.id
    )


    diff = history.diff(
        first.id,
        second.id
    )


    assert (
        diff["changed"]
        ["sampler"]
        ["to"]
        ["steps"]
        ==
        30
    )