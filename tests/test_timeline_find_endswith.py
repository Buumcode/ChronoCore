from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_find_endswith():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "model",
        "sdxl_v1.safetensors"
    )

    repo.add(report)


    report = WorkflowReport()

    report.add(
        "model",
        "flux_model.ckpt"
    )

    repo.add(report)


    result = repo.timeline().find(
        model__endswith=".safetensors"
    )


    assert len(result) == 1

    assert (
        result[0]["model"]
        ==
        "sdxl_v1.safetensors"
    )