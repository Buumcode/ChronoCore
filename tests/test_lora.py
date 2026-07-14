from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.extractors.lora import LoRAExtractor


def test_lora_extract():

    workflow = {

        "1": {
            "class_type": "LoraLoader",
            "inputs": {
                "lora_name": "detail_slider.safetensors",
                "strength_model": 0.8,
                "strength_clip": 1.0
            }
        }

    }

    graph = ComfyUIAdapter.from_prompt(
        workflow
    )

    result = LoRAExtractor().extract(
        graph
    )

    assert len(result) == 1

    assert result[0]["name"] == (
        "detail_slider.safetensors"
    )

    assert result[0]["strength_model"] == 0.8

    assert result[0]["strength_clip"] == 1.0