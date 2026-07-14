import json

from chrono_core.io import WorkflowLoader


def test_load_workflow(tmp_path):

    workflow = {
        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello"
            }
        }
    }

    file = tmp_path / "workflow.json"

    file.write_text(
        json.dumps(workflow),
        encoding="utf-8"
    )

    loaded = WorkflowLoader.load(file)

    assert loaded == workflow