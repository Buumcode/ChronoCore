from chrono_core.repository import WorkflowRepository
from chrono_core.report import WorkflowReport


def test_snapshot_index_after_load(tmp_path):

    path = tmp_path / "history.json"


    repo = WorkflowRepository()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps": 20
        }
    )

    repo.add(report)


    # Создаём индекс и строим его

    index = repo.snapshot_index()

    result = index.find(
        sampler__steps=20
    )

    assert result.count() == 1


    # Сохраняем

    repo.save(
        path
    )


    # Загружаем

    restored = WorkflowRepository.load(
        path
    )


    restored_index = (
        restored
        .snapshot_index()
    )


    # Индекс новый, не восстановленный

    assert (
        restored_index._index
        ==
        {}
    )


    # Первый поиск должен восстановить работу

    result = restored_index.find(
        sampler__steps=20
    )


    assert result.count() == 1

    assert (
        restored_index._indexed_count
        ==
        1
    )