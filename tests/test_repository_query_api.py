from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_repository_query_api():

    repo = WorkflowRepository()


    report = WorkflowReport()


    report.add(
        "model",
        {
            "type":
            "CheckpointLoaderSimple",
            "checkpoint":
            "test.safetensors"
        }
    )


    report.add(
        "sampler",
        {
            "type":
            "KSampler",
            "steps":20
        }
    )


    repo.add(
        report
    )


    query = repo.query()


    assert len(
        query.samplers()
    ) == 1


    assert (
        query.samplers()[0]["steps"]
        ==
        20
    )