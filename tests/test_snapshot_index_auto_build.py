from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_auto_build():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    result = (
        repo
        .snapshot_index()
        .find(
            sampler__steps=20
        )
    )


    assert result.count() == 1