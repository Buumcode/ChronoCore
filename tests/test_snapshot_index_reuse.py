from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_reuse():

    repo = WorkflowRepository()

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    index = repo.snapshot_index()


    calls = []


    original_build = index.build


    def spy_build():

        calls.append(1)

        original_build()


    index.build = spy_build


    index.find(
        sampler__steps=20
    )

    index.find(
        sampler__steps=20
    )


    assert len(calls) == 1