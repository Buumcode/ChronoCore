from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_stream():

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


    repo.create_branch(
        "experiment"
    )


    timeline = repo.timeline()


    stream = timeline.stream()


    assert len(stream) == 2


    assert (
        stream[0]["type"]
        ==
        "snapshot_created"
    )


    assert (
        stream[1]["type"]
        ==
        "branch_created"
    )