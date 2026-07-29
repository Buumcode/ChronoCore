from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_build():

    repo = WorkflowRepository()

    for steps in [20, 40, 60]:

        report = WorkflowReport()

        report.add(
            "sampler",
            {
                "steps": steps
            }
        )

        repo.add(report)

    index = repo.snapshot_index()

    index.build()

    assert len(index._index) > 0