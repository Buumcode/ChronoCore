from chrono_core.api.session import Session


def test_session_dependencies():

    workflow = {

        "1": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "hello"
            }
        },

        "2": {
            "class_type": "KSampler",
            "inputs": {
                "positive": ["1",0]
            }
        }
    }


    session = Session(workflow)


    assert {
        "from": "1",
        "to": "2"
    } in session.dependencies["edges"]