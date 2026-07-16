from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_filter_type():

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


    events = timeline.filter(
        type="branch_created"
    )


    assert len(events) == 1


    assert (
        events[0]["type"]
        ==
        "branch_created"
    )
    
def test_timeline_filter_empty():

    repo = WorkflowRepository()


    timeline = repo.timeline()


    result = timeline.filter(
        type="unknown"
    )


    assert result == []        