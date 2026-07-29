from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_distinct():

    repo = WorkflowRepository()


    for steps in [20, 20, 40]:

        report = WorkflowReport()

        report.add(
            "sampler",
            {
                "steps": steps
            }
        )

        repo.add(report)


    result = (
        repo.timeline()
        .find()
        .select(
            "sampler.steps"
        )
        .distinct()
    )


    assert result.count() == 2

    assert result[0] == 20
    assert result[1] == 40