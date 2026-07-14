from chrono_core.report import WorkflowReport
from chrono_core.history import WorkflowSnapshot



def test_snapshot():

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    snapshot = WorkflowSnapshot(
        report
    )


    data = snapshot.to_dict()


    assert "id" in data
    assert "created" in data
    assert data["report"]["sampler"]["steps"] == 20