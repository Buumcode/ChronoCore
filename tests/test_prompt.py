from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.extractors.prompt import PromptExtractor


def test_zero_out_negative():

    workflow = {

        "1":{
            "class_type":"CLIPTextEncode",
            "inputs":{
                "text":"1girl, red dress"
            }
        },

        "2":{
            "class_type":"ConditioningZeroOut",
            "inputs":{
                "conditioning":["1",0]
            }
        },

        "3":{
            "class_type":"KSampler",
            "inputs":{
                "positive":["1",0],
                "negative":["2",0]
            }
        }
    }


    graph = ComfyUIAdapter.from_prompt(workflow)

    result = PromptExtractor().extract(graph)


    assert result["positive"] == "1girl, red dress"
    assert result["negative"] == ""