import json
import logging
import os

import requests


class ApiHandler:
    def __init__(self, url: str):
        self.url = url

    def post_data(self) -> None:
        with open(
            os.path.join(os.getcwd(), "source/logs/output/output.json"),
            "r",
            encoding="utf-8",
        ) as file:
            data_json = json.loads(file.read())

        response = requests.post(self.url, json=data_json)
        logging.info(f"Status da Requisição: {response.status_code}")
