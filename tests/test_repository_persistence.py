from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport

def test_repository_file_roundtrip(tmp_path):

    path = (
        tmp_path /
        "workflow.chrono"
    )


    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":40
        }
    )


    repo.add(
        report
    )


    repo.save(
        path
    )


    restored = (
        WorkflowRepository
        .load(path)
    )


    assert (
        restored.latest()
        .report["sampler"]["steps"]
        ==
        40
    )