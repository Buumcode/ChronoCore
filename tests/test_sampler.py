from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.extractors.sampler import SamplerExtractor


def test_sampler_extract():

    workflow = {

        "1": {
            "class_type": "KSampler",
            "inputs": {
                "steps": 25,
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


    result = SamplerExtractor().extract(
        graph
    )


    assert result["type"] == "KSampler"
    assert result["steps"] == 25
    assert result["cfg"] == 7
    assert result["sampler"] == "euler"