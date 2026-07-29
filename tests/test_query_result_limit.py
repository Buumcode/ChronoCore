from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_limit():

    repo = WorkflowRepository()


    for steps in [20, 40, 60]:

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
        .order_by(
            "sampler.steps"
        )
        .limit(2)
    )


    assert result.count() == 2

    assert (
        result[0]["sampler"]["steps"]
        == 20
    )

    assert (
        result[1]["sampler"]["steps"]
        == 40
    )