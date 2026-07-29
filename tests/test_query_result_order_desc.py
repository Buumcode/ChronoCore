from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_order_by_desc():

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
            "sampler.steps",
            descending=True,
        )
    )


    assert (
        result[0]["sampler"]["steps"]
        == 60
    )

    assert (
        result[1]["sampler"]["steps"]
        == 40
    )

    assert (
        result[2]["sampler"]["steps"]
        == 20
    )