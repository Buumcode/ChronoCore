from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_repository_query():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    repo.add(
        report
    )


    assert repo.latest() is not None


    assert len(
        repo.history()
    ) == 1