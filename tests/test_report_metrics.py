from chrono_core.report import WorkflowReport


def test_report_metrics():

    report = WorkflowReport()


    report.add(
        "sampler",
        {
            "steps": 20
        }
    )


    report.metric(
        "score",
        0.85
    )


    data = report.to_dict()


    assert (
        data["metrics"]["score"]
        ==
        0.85
    )