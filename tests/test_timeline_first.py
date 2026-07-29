from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_timeline_first():

    repo = WorkflowRepository()


    first = WorkflowReport()
    first.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(first)


    second = WorkflowReport()
    second.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(second)


    result = repo.timeline().first(
        sampler__steps=20
    )


    assert result is not None

    assert result["sampler"]["steps"] == 20