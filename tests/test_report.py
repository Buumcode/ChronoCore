from chrono_core.report import WorkflowReport


def test_report_basic():

    report = WorkflowReport()


    report.add(
        "model",
        {
            "checkpoint": "test.safetensors"
        }
    )


    assert report.get(
        "model"
    )["checkpoint"] == (
        "test.safetensors"
    )


    data = report.to_dict()


    assert "model" in data