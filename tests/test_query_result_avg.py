from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_query_result_avg():

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


    value = (
        repo.timeline()
        .find()
        .select(
            "sampler.steps"
        )
        .avg()
    )


    assert value == 40