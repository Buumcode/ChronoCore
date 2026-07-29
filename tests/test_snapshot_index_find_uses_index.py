from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_find_uses_index():

    repo = WorkflowRepository()

    for steps in [10, 20, 30]:

        report = WorkflowReport()

        report.add(
            "sampler",
            {
                "steps": steps
            }
        )

        repo.add(report)


    index = repo.snapshot_index()

    index.build()


    # удаляем возможность fallback-поиска
    # если find() пойдёт через timeline,
    # тест упадёт

    index.repository.timeline = lambda: None


    result = index.find(
        sampler__steps=20
    )


    assert result.count() == 1

    assert (
        result.first()
        .report
        .to_dict()["sampler"]["steps"]
        ==
        20
    )