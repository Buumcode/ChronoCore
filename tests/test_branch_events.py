from chrono_core.history import HistoryManager


def test_branch_events():

    history = HistoryManager()


    history.create_branch(
        "experiment"
    )


    history.checkout(
        "experiment"
    )


    events = history.events()


    assert len(events) == 2


    assert (
        events[0].type
        ==
        "branch_created"
    )


    assert (
        events[1].type
        ==
        "branch_checkout"
    )


    assert (
        events[1].payload["branch"]
        ==
        "experiment"
    )