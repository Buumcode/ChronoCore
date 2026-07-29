from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_contains():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "model",
        "SDXL Turbo"
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "model",
        "Flux"
    )

    repo.add(report)


    result = repo.timeline().find(
        model__contains="SDXL"
    )


    assert len(result) == 1

    assert (
        result[0]["model"]
        ==
        "SDXL Turbo"
    )