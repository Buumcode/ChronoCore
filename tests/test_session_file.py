import json

from chrono_core import Session


def test_session_from_file(tmp_path):

    workflow = {
        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello world"
            }
        }
    }

    file = tmp_path / "workflow.json"

    file.write_text(
        json.dumps(workflow),
        encoding="utf-8"
    )

    session = Session.from_file(file)

    assert session.prompts["positive"] == "hello world"