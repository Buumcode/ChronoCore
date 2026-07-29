from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_in():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "name": "Euler a"
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "name": "Flux"
        }
    )

    repo.add(report)


    result = repo.timeline().find(
        sampler__name__in=[
            "Euler a",
            "DPM++ 2M",
        ]
    )


    assert len(result) == 1

    assert (
        result[0]["sampler"]["name"]
        ==
        "Euler a"
    )