import json
import logging
import os

import requests
from services.api.api_post_i import APIPostI


class APIHandler(APIPostI):
    def post_data(self, url: str) -> None:
        with open(
            os.path.join(os.getcwd(), "source/logs/output/output.json"),
            "r",
            encoding="utf-8",
        ) as file:
            data_json = json.loads(file.read())

        response = requests.post(url, json=data_json)
        logging.info(f"Status da Requisição: {response.status_code}")
