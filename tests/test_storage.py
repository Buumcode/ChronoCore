from chrono_core.report import WorkflowReport
from chrono_core.history import HistoryManager
from chrono_core.storage import JsonHistoryStore



def test_json_storage(tmp_path):

    history = HistoryManager()


    report = WorkflowReport()

    report.add(
        "sampler",
        {
            "steps":20
        }
    )


    history.add(
        report
    )


    file = tmp_path / "history.json"


    store = JsonHistoryStore(
        file
    )


    store.save(
        history
    )


    data = store.load()


    assert len(data) == 1

    assert (
        data[0]["report"]["sampler"]["steps"]
        ==
        20
    )