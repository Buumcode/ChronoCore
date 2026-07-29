from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_order_by():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    result = repo.timeline().find()


    ordered = result.order_by(
        "sampler.steps"
    )


    assert (
        ordered[0]["sampler"]["steps"]
        ==
        20
    )


    assert (
        ordered[1]["sampler"]["steps"]
        ==
        40
    )