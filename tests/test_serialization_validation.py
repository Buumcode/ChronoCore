import pytest

from chrono_core.serialization import WorkflowSerializer


def test_invalid_format():

    serializer = WorkflowSerializer()


    data = {
        "format": "other",
        "version": 1,
        "repository": {}
    }


    with pytest.raises(
        ValueError
    ):

        serializer.load(
            data
        )



def test_invalid_version():

    serializer = WorkflowSerializer()


    data = {
        "format": "chrono_core",
        "version": 999,
        "repository": {}
    }


    with pytest.raises(
        ValueError
    ):

        serializer.load(
            data
        )



def test_missing_repository():

    serializer = WorkflowSerializer()


    data = {
        "format": "chrono_core",
        "version": 1
    }


    with pytest.raises(
        ValueError
    ):

        serializer.load(
            data
        )