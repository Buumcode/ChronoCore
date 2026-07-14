from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.extractors.model import ModelExtractor


def test_model_extract():

    workflow = {

        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": "dreamshaperXL.safetensors"
            }
        }
    }


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    result = ModelExtractor().extract(
        graph
    )


    assert result["type"] == (
        "CheckpointLoaderSimple"
    )

    assert result["checkpoint"] == (
        "dreamshaperXL.safetensors"
    )