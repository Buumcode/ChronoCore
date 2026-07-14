from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.analyzers.dependencies import DependencyAnalyzer



def test_dependency_analysis():

    workflow = {

        "0": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": "model.safetensors"
            }
        },


        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello"
            }
        },


        "2": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["0", 0],
                "positive": ["1", 0]
            }
        }
    }


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    result = DependencyAnalyzer().analyze(
        graph
    )


    assert len(
        result["nodes"]
    ) == 3


    assert {
        "from": "0",
        "to": "2",
    } in result["edges"]


    assert {
        "from": "1",
        "to": "2",
    } in result["edges"]