from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_refresh_same_count():

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


    # строим индекс

    result = index.find(
        sampler__steps=20
    )

    assert result.count() == 1


    # запоминаем старое состояние

    old_last_id = index._indexed_last_id


    # заменяем snapshot тем же количеством элементов

    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 40
        }
    )


    repo.history_manager._history = []


    repo.add(report)


    # количество snapshot теперь снова 1,
    # но данные изменились


    result = index.find(
        sampler__steps=40
    )


    assert result.count() == 1


    assert (
        index._indexed_last_id
        !=
        old_last_id
    )