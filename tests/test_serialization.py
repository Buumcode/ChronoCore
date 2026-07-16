from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport
from chrono_core.serialization import WorkflowSerializer


def test_repository_serialization():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )

    repo.add(
        report
    )


    serializer = WorkflowSerializer()

    data = serializer.dump(
        repo
    )


    restored = serializer.load(
        data
    )


    assert len(
        restored.history()
    ) == 1


    assert (
        restored.latest()
        .report["sampler"]["steps"]
        ==
        20
    )
    
    def test_snapshot_id_roundtrip():

        repo = WorkflowRepository()

        report = WorkflowReport()

        report.add(
            "sampler",
            {
                "steps":20
            }
        )

        repo.add(report)


        original_id = (
            repo.latest().id
        )


        serializer = WorkflowSerializer()

        restored = serializer.load(
            serializer.dump(repo)
        )


        assert (
            restored.latest().id
            ==
            original_id
        )

    def test_branch_roundtrip():

        repo = WorkflowRepository()

        repo.create_branch(
            "experiment"
        )


        serializer = WorkflowSerializer()

        restored = serializer.load(
            serializer.dump(repo)
        )


        assert (
            "experiment"
            in restored.branches()
        )        