import json


def open_mock_json(model: str):
    with open(f"tests/mock_{model}.json") as file:
        return json.load(file)
