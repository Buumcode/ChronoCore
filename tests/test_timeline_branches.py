from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_branch_history():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(
        first
    )


    repo.create_branch(
        "experiment"
    )


    repo.checkout(
        "experiment"
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps": 40
        }
    )


    repo.add(
        second
    )


    timeline = repo.timeline()


    history = timeline.branch_history(
        "experiment"
    )


    assert len(history) == 1