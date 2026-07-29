import chrono_core


def test_public_api():

    assert hasattr(
        chrono_core,
        "WorkflowRepository"
    )

    assert hasattr(
        chrono_core,
        "WorkflowTimeline"
    )

    assert chrono_core.__version__ == "1.0.0"