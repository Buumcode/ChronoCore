from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_startswith():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "name": "Euler a Karras"
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "name": "DPM++ 2M"
        }
    )

    repo.add(report)


    result = repo.timeline().find(
        sampler__name__startswith="Euler"
    )


    assert len(result) == 1

    assert (
        result[0]["sampler"]["name"]
        ==
        "Euler a Karras"
    )