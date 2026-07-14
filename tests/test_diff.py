from chrono_core.report import WorkflowReport
from chrono_core.diff import WorkflowDiff



def test_workflow_diff():

    old = WorkflowReport()

    old.add(
        "sampler",
        {
            "steps": 20
        }
    )


    new = WorkflowReport()

    new.add(
        "sampler",
        {
            "steps": 30
        }
    )


    diff = WorkflowDiff()


    result = diff.compare(
        old,
        new
    )


    assert "sampler" in (
        result["changed"]
    )


    assert (
        result["changed"]
        ["sampler"]
        ["from"]
        ["steps"]
        ==
        20
    )


    assert (
        result["changed"]
        ["sampler"]
        ["to"]
        ["steps"]
        ==
        30
    )