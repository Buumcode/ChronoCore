from chrono_core.query import QueryResult
from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_returns_query_result():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)

    result = (
        repo
        .snapshot_index()
        .find(
            sampler__steps=20
        )
    )

    assert isinstance(
        result,
        QueryResult,
    )