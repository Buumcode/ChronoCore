from chrono_core import (
    WorkflowRepository,
    WorkflowReport,
)


def test_public_serialization_roundtrip(
    tmp_path
):

    path = tmp_path / "history.json"


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


    repo.save(
        path
    )


    restored = WorkflowRepository.load(
        path
    )


    assert (
        restored.latest().id
        ==
        snapshot.id
    )