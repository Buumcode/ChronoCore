from chrono_core.api.session import Session


def test_session():

    workflow = {

        "0": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": "dreamshaperXL.safetensors"
            }
        },

        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "1girl, red dress"
            }
        },

        "2": {
            "class_type": "ConditioningZeroOut",
            "inputs": {
                "conditioning": ["1", 0]
            }
        },

        "3": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["1", 0],
                "negative": ["2", 0],
                "steps": 20,
                "cfg": 7,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0
            }
        }
    }

    session = Session(workflow)

    assert session.report["prompts"]["positive"] == (
        "1girl, red dress"
    )

    assert session.report["model"]["checkpoint"] == (
        "dreamshaperXL.safetensors"
    )

    assert session.report["sampler"]["steps"] == 20
    
    assert session.prompts["positive"] == (
        "1girl, red dress"
    )

    assert session.model["checkpoint"] == (
        "dreamshaperXL.safetensors"
    )

    assert session.sampler["steps"] == 20    