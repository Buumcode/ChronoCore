from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.analyzers.statistics import WorkflowStatistics



def test_statistics():

    workflow = {

        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello"
            }
        },

        "2": {
            "class_type": "LoraLoader",
            "inputs": {
                "model": ["1",0]
            }
        },

        "3": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["1",0]
            }
        }

    }


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    result = WorkflowStatistics().analyze(
        graph
    )


    assert result["nodes"] == 3

    assert (
        result["node_types"]["KSampler"]
        == 1
    )

    assert result["has_lora"] is True