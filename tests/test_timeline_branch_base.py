from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_branch_base():

    repo = WorkflowRepository()


    base = repo.add(
        WorkflowReport()
    )


    repo.create_branch(
        "experiment"
    )

    repo.checkout(
        "experiment"
    )


    repo.add(
        WorkflowReport()
    )


    timeline = repo.timeline()


    branch_base = timeline.branch_base(
        "main",
        "experiment",
    )


    assert branch_base == base.id