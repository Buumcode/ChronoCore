from chrono_core.branches import WorkflowBranch
from chrono_core.history.snapshot import WorkflowSnapshot


def test_branch():


    branch = WorkflowBranch(
        "lora-experiment"
    )


    first = WorkflowSnapshot(
        {
            "sampler": {
                "steps":20
            }
        }
    )


    second = WorkflowSnapshot(
        {
            "sampler": {
                "steps":30
            }
        }
    )


    branch.add(
        first
    )

    branch.add(
        second
    )


    assert branch.name == (
        "lora-experiment"
    )


    assert branch.size() == 2


    assert branch.latest() == second


    assert (
        branch.all()[0]
        ==
        first
    )