from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_select():

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
        .select(
            "sampler.steps"
        )
    )


    assert result[0] == 20
    assert result[1] == 40
    assert result[2] == 60