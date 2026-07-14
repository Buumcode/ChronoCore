from chrono_core import Session


from chrono_core import Session


def test_public_api():

    workflow = {
        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello world"
            }
        },
        "2": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["1", 0],
                "negative": ["1", 0],
                "steps": 20,
                "cfg": 7,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0,
            }
        },
    }

    session = Session(workflow)

    assert session.prompts["positive"] == "hello world"