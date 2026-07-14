from chrono_core.adapters.comfyui import ComfyUIAdapter
from chrono_core.conditioning.resolver import ConditioningResolver


def test_conditioning_chain_zero_out():

    workflow = {

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
                "negative": ["2", 0]
            }
        }
    }


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    resolver = ConditioningResolver(
        graph
    )


    chain = resolver.resolve_chain(
        ["2", 0]
    )


    assert chain.contains(
        "ConditioningZeroOut"
    )



def test_conditioning_chain_normal():

    workflow = {

        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "beautiful landscape"
            }
        },

        "2": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["1", 0]
            }
        }
    }


    graph = ComfyUIAdapter.from_prompt(
        workflow
    )


    resolver = ConditioningResolver(
        graph
    )


    chain = resolver.resolve_chain(
        ["1", 0]
    )


    assert not chain.contains(
        "ConditioningZeroOut"
    )