from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_usage():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    index = repo.snapshot_index()

    index.build()


    assert (
        "sampler.steps"
        in index._index
    )


    assert (
        20
        in index._index["sampler.steps"]
    )