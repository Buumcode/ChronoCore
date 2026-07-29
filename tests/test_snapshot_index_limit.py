from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_order_by():

    repo = WorkflowRepository()

    for steps in [40, 20, 60]:

        report = WorkflowReport()

        report.add(
            "sampler",
            {
                "steps": steps
            }
        )

        repo.add(report)

    result = (
        repo
        .snapshot_index()
        .find()
        .limit(1)
    )

    assert result.count() == 1