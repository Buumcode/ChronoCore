from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_count():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(
        report
    )


    result = repo.timeline().find(
        sampler__steps=20
    )


    assert result.count() == 1