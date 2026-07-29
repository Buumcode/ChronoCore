from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_merge_conflicts():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    repo.create_branch(
        "experiment"
    )


    repo.checkout(
        "experiment"
    )


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(report)


    conflicts = repo.timeline().merge_conflicts(
        "main",
        "experiment",
    )


    assert "sampler" in conflicts