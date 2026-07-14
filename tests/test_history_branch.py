from chrono_core.history import HistoryManager
from chrono_core.history.snapshot import WorkflowSnapshot


def test_history_branch():


    history = HistoryManager()


    first = WorkflowSnapshot(
        {
            "sampler":{
                "steps":20
            }
        }
    )


    second = WorkflowSnapshot(
        {
            "sampler":{
                "steps":40
            }
        }
    )


    history.add(
        first
    )


    history.create_branch(
        "experiment"
    )


    history.add(
        second,
        branch="experiment"
    )


    assert history.list_branches() == [
        "main",
        "experiment"
    ]


    assert (
        history.get_branch(
            "main"
        ).size()
        ==
        1
    )


    assert (
        history.get_branch(
            "experiment"
        ).size()
        ==
        1
    )