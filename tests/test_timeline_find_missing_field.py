from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_missing_field():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "model",
        "SDXL"
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "lora",
        {
            "name": "detail"
        }
    )

    repo.add(report)


    result = repo.timeline().find(
        lora__name__contains="detail"
    )


    assert len(result) == 1

    assert (
        result[0]["lora"]["name"]
        ==
        "detail"
    )