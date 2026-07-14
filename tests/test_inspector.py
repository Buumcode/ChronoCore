from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.inspector.inspector import Inspector


def test_inspector_basic():

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


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    inspector = Inspector()

    result = inspector.inspect(
        graph
    )
    
    data = result.to_dict()


    assert data["prompts"]["positive"] == (
        "1girl, red dress"
    )


    assert (
        "ConditioningZeroOut"
        in data["conditioning"]
    )
    
    assert data["sampler"]["type"] == "KSampler"
    assert data["sampler"]["steps"] == 20

    assert data["model"]["type"] == (
        "CheckpointLoaderSimple"
    )

    assert data["model"]["checkpoint"] == (
        "dreamshaperXL.safetensors"
    )