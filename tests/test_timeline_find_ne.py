from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_ne():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(report)


    result = repo.timeline().find(
        sampler__steps__ne=20
    )


    assert len(result) == 1

    assert (
        result[0]["sampler"]["steps"]
        ==
        40
    )