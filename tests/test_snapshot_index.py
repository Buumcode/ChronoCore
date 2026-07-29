from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    snapshot = repo.add(
        report
    )


    index = repo.snapshot_index()


    result = index.find(
        sampler__steps=20
    )


    assert len(result) == 1

    assert (
        result[0].id
        ==
        snapshot.id
    )