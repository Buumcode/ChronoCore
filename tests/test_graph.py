from chrono_core.adapters.comfyui import ComfyUIAdapter


def test_graph_queries():

    workflow = {

        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {}
        },

        "2": {
            "class_type": "LoraLoader",
            "inputs": {}
        },

        "3": {
            "class_type": "LoraLoader",
            "inputs": {}
        }
    }

    graph = ComfyUIAdapter.from_prompt(
        workflow
    )

    model = graph.find_first_type(
        "CheckpointLoaderSimple"
    )

    assert model.class_type == (
        "CheckpointLoaderSimple"
    )

    loras = graph.find_all_types(
        "LoraLoader"
    )

    assert len(loras) == 2