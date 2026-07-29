from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_gte():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 30
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
        sampler__steps__gte=30
    )


    assert len(result) == 2