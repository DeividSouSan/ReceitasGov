import json
import os
import requests
import logging

def send_post_request(url: str, log: bool = False):
    with open(f"{os.getcwd()}/output/output.json", 'r', encoding='utf-8') as f:
        data_json = json.loads(f.read())
        
    response = requests.post(url, json=data_json)
    
    logging.info(f"Status da Requisição: {response.status_code}")