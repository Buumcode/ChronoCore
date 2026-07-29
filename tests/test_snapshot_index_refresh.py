from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_refresh():

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


    first = index.find(
        sampler__steps=20
    )


    assert first.count() == 1


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )

    repo.add(report)


    second = index.find(
        sampler__steps=40
    )


    assert second.count() == 1