import json
import logging
import os

import requests


def save_data(url: str) -> None:

    with open(
        os.path.join(os.getcwd(), "source/output/output.json"), "r", encoding="utf-8"
    ) as file:
        data_json = json.loads(file.read())

    response = requests.post(url, json=data_json)
    logging.info(f"Status da Requisição: {response.status_code}")
