from chrono_core.api import Session



def test_session_history(tmp_path):

    workflow = {
        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello"
            }
        }
    }


    session = Session(
        workflow
    )


    assert len(
        session.history.all()
    ) == 1


    file = tmp_path / "history.json"


    session.save_history(
        file
    )


    data = session.load_history(
        file
    )


    assert len(data) == 1

    assert (
        data[0]["report"]["prompts"]["positive"]
        ==
        "hello"
    )