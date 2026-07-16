from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_compare_branches():

    repo = WorkflowRepository()


    first = WorkflowReport()

    first.add(
        "sampler",
        {
            "steps": 20
        }
    )


    repo.add(
        first
    )


    repo.create_branch(
        "experiment"
    )


    repo.checkout(
        "experiment"
    )


    second = WorkflowReport()

    second.add(
        "sampler",
        {
            "steps": 40
        }
    )


    repo.add(
        second
    )


    timeline = repo.timeline()


    diff = timeline.compare_branches(
        "main",
        "experiment"
    )


    assert (
        "sampler"
        in diff["changed"]
    )


    assert (
        diff["changed"]["sampler"]["from"]["steps"]
        ==
        20
    )


    assert (
        diff["changed"]["sampler"]["to"]["steps"]
        ==
        40
    )