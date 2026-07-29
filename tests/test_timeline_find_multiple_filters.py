from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_multiple_filters():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 30
        }
    )

    report.add(
        "model",
        "SDXL Turbo"
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 30
        }
    )

    report.add(
        "model",
        "Flux"
    )

    repo.add(report)


    result = repo.timeline().find(
        sampler__steps__gte=30,
        model__contains="SDXL",
    )


    assert len(result) == 1

    assert (
        result[0]["model"]
        ==
        "SDXL Turbo"
    )