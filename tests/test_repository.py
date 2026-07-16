from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_repository():

    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {"steps": 20}
    )


    snapshot = repo.add(report)


    assert len(repo.all()) == 1

    assert repo.latest().id == snapshot.id

    assert (
        repo.latest().report["sampler"]["steps"]
        ==
        20
    )


def test_repository_branches():

    repo = WorkflowRepository()


    repo.create_branch("experiment")

    repo.checkout("experiment")


    assert "experiment" in repo.branches()

    assert repo.current_branch().name == "experiment"