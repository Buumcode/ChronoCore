from chrono_core import (
    WorkflowRepository,
    WorkflowReport,
)


def test_public_usage_example():

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


    assert snapshot is not None


    latest = repo.latest()


    assert (
        latest.id
        ==
        snapshot.id
    )