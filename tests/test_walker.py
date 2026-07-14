from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.graph.walker import GraphWalker


def test_find_clip_source():

    workflow = {

        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello world"
            }
        },


        "2": {
            "class_type": "TextConcat",
            "inputs": {
                "text": ["1", 0]
            }
        },


        "3": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["2",0]
            }
        }
    }



    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    walker = GraphWalker(graph)



    node = walker.find_first(
        ["2",0],
        lambda n:
            n.class_type.startswith(
                "CLIPTextEncode"
            )
    )


    assert node is not None

    assert node.class_type == \
           "CLIPTextEncode"


    print(node)