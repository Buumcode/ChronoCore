from chrono_core.events import WorkflowEventLog


def test_event_log():

    log = WorkflowEventLog()


    event = log.add(
        "snapshot_created",
        {
            "snapshot": "123"
        }
    )


    assert len(
        log.all()
    ) == 1


    assert (
        log.latest().type
        ==
        "snapshot_created"
    )