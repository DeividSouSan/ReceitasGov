import json
import os
import requests
import logging

def post_to_api(url: str) -> None:
    base_path = os.getcwd()
    
    with open(f"{base_path}/output/output.json", 'r', encoding='utf-8') as file:
        data_json = json.loads(file.read())
        
    response = requests.post(url, json=data_json)
    
    logging.info(f"Status da Requisição: {response.status_code}")